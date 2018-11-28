#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <set>
#include <fstream>
using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define REMOVE(Itr,n) (Itr).erase(remove((Itr).begin(),(Itr).end(),n),(Itr).end())
#define PB_VEC(Itr1,Itr2) (Itr1).insert((Itr1).end(),(Itr2).begin(),(Itr2).end())
typedef long long ll;


bool judge(string s){
    REP(i,s.size())if(s[i]!='+')return false;
    return true;
}

string flip(string s, int n){
    for(int i=0;i<n;i++){
        if(s[i]=='-')s[i]='+';
        else s[i]='-';
    }
    return s;
}

int main(){
    ifstream ifs("/Users/kurodakousaku/Desktop/c練習/practice/practice/B.txt");
    string str;
    ifs>>str;
    int T = stoi(str);
    
    for(int q=0;q<T;q++){
        ifs>>str;
        int count=0;
        while(!judge(str)){
            int point=(int)str.size()-1;
            while(str[point]=='+')point--;
            str = flip(str,point+1);
            count++;
        }
        
        cout << "Case #"<<q+1<<": "<<count<<endl;
        
    }
    
    return 0;
}
