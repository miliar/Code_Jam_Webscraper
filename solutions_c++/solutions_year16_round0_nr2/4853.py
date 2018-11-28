#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <cmath> 

using namespace std;
void flip(string &s,int pos){
    string sub1,sub2;
    sub1 = s.substr(0,pos+1);
    if(pos+1 < s.size()) sub2 = s.substr(pos+1);
    reverse(sub1.begin(),sub1.end());
    for(int i=0;i<sub1.size();i++){
        if(sub1[i] == '+') sub1[i] = '-';
        else if(sub1[i] == '-') sub1[i] = '+';
    }
    s = sub1 + sub2;
}
int solve(string s){
    vector<int> v(s.size(),0);
    string temp = s;
    int count = 0;
    for(int i=0;i<v.size();i++){
        for(int j=0;j<v.size();j++){
            if(j<v.size()-i-1){
                v[j] = 0;    
            }
            else{
                v[j] = 1;
            }
        }

        count = 0;
        do{
            count = 0;
            s = temp;
            for(int j=0;j<v.size();j++){
                if (v[j] == 1){
                    flip(s,j);
                    count++;
                }    
            }
            for(int j=0;j<s.size();j++){
                if(s[j] == '-'){
                    break;
                }
                else if(j == s.size()-1){
                    return count;
                }
            }
        }while(next_permutation(v.begin(),v.end()));
    }
     
}

int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,lastpos = -1, count;
    string s;
    cin >> t;
    for(int q=0;q<t;q++){
        cout << "Case #" << q+1 << ": ";
        cin >> s;
        lastpos = -1;
        for(int j=s.size()-1;j>=0;j--){
            if(s[j] == '-'){
                lastpos = j;
                break;
            }
        }
        if(lastpos == -1){
            cout << "0" <<endl;
            continue;
        }
        count = solve(s);
        cout << count << endl;
    }


    return 0;
}