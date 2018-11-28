#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char multiplyQ(char s, char t, bool& flag){
    
    if(s==t){
        flag = !flag;
        return '1';
    }
    else if(s=='1'){
        return t;
    }
    else if(t=='1'){
        return s;
    }
    else if(s=='i' && t=='j'){
        return 'k';
    }
    else if(s=='j' && t=='k'){
        return 'i';
    }
    else if(s=='k' && t=='i'){
        return 'j';
    }
    else if(s=='j' && t=='i'){
        flag = !flag;
        return 'k';
    }
    else if(s=='k' && t=='j'){
        flag = !flag;
        return 'i';
    }
    else if(s=='i' && t=='k'){
        flag = !flag;
        return 'j';
    }
    return '1';
}

char reduceStr(string &str, int start, int end, bool& flag){
    char res = '1';
    
    for(int i=start;i<=end;++i){
        res = multiplyQ(res, str[i], flag);
    }
    return res;
}



bool validReduceUtil(string &inputStr, int idx, int count, bool flag){
    int len = inputStr.length();
    
    if(count == 2){
        if(reduceStr(inputStr, idx, len-1, flag) =='k'){
            if(flag){
                return true;
            }
        }
        return false;
    }
    
    
    
    else if(count == 0){                       //'i'
        for(int i=0; i<len; ++i){
            if(reduceStr(inputStr, 0, i, flag)=='i' && flag){
                if(validReduceUtil(inputStr, i+1, count+1, flag)){
                    return true;
                }
            }
        }
    }
    else if(count == 1){                  //'j'
        for(int i=idx; i<len; ++i){
            if(reduceStr(inputStr, idx, i, flag)=='j' && flag){
                if(validReduceUtil(inputStr, i+1, count+1, flag)){
                    return true;
                }
            }
        }
    }
    
    return false;
}

bool validReduce(string inputStr){
    bool flag = true;
    return validReduceUtil(inputStr, 0, 0, flag);
}



int main(int argc, const char* argv[]){
    ifstream infile;
    int testcasenum;
    ofstream outfile;
   
    infile.open("C-small-attempt0.in");
    outfile.open("C-small-attempt0.out");
    
    infile >> testcasenum;
    for(int i=0; i< testcasenum; i++) {
        int l, x;
        string input;
        infile >> l >> x;
        infile >> input;
    
        
        string attachStr ="";
        for(int j=0;j<x;++j){
            attachStr.append(input);
        }
        
        string res = validReduce(attachStr)==true? "YES" : "NO";
        outfile<<"Case #"<<i+1<<": "<<res<< endl;
    }
    
    infile.close();
    outfile.close();
    return 0;
}
