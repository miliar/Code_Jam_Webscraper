#include<cstdio>
#include<cstring>
#include<algorithm>
#include<vector>
#include<string>
#include<iostream>
#include<queue>
#include<cmath>
#include<map>
#include<stack>
#include<bitset>
#include<string.h>
#include<stdlib.h>
#include<set>
using namespace std;

void dfs(){
    
}

int main()
{
    freopen("/Users/shitian/Desktop/gcj/gcj/A-large.in", "r", stdin);
    freopen("/Users/shitian/Desktop/gcj/gcj/out.txt", "w", stdout);
    map<int,string>ma;
    ma[0]="ZERO";
    ma[1]="ONE";
    ma[2]="TWO";
    ma[3]="THREE";
    ma[4]="FOUR";
    ma[5]="FIVE";
    ma[6]="SIX";
    ma[7]="SEVEN";
    ma[8]="EIGHT";
    ma[9]="NINE";

    int tcase;
    cin>>tcase;
    for(int tca=1;tca<=tcase;tca++){
        cout<<"Case #"<<tca<<": ";
        
        string s;
        cin>>s;
        map<char,int>m;
        for(int i=0;i<s.length();i++){
            m[s[i]]++;
        }
        vector<int>v;
        int zero=m['Z'];
        for(int i=0;i<zero;i++){
            v.push_back(0);
            for(int j=0;j<ma[0].length();j++){
                m[ma[0][j]]--;
            }
        }
        int two=m['W'];
        for(int i=0;i<two;i++){
            v.push_back(2);
            for(int j=0;j<ma[2].length();j++){
                m[ma[2][j]]--;
            }
        }
        int six=m['X'];
        for(int i=0;i<six;i++){
            v.push_back(6);
            for(int j=0;j<ma[6].length();j++){
                m[ma[6][j]]--;
            }
        }
        int four=m['U'];
        for(int i=0;i<four;i++){
            v.push_back(4);
            for(int j=0;j<ma[4].length();j++){
                m[ma[4][j]]--;
            }
        }
        int eight=m['G'];
        for(int i=0;i<eight;i++){
            v.push_back(8);
            for(int j=0;j<ma[8].length();j++){
                m[ma[8][j]]--;
            }
        }
        int seven=m['S'];
        for(int i=0;i<seven;i++){
            v.push_back(7);
            for(int j=0;j<ma[7].length();j++){
                m[ma[7][j]]--;
            }
        }
        int five=m['F'];
        for(int i=0;i<five;i++){
            v.push_back(5);
            for(int j=0;j<ma[5].length();j++){
                m[ma[5][j]]--;
            }
        }
        int one=m['O'];
        for(int i=0;i<one;i++){
            v.push_back(1);
            for(int j=0;j<ma[1].length();j++){
                m[ma[1][j]]--;
            }
        }
        int three=m['T'];
        for(int i=0;i<three;i++){
            v.push_back(3);
            for(int j=0;j<ma[3].length();j++){
                m[ma[3][j]]--;
            }
        }
        int nine=m['I'];
        for(int i=0;i<nine;i++){
            v.push_back(9);
            for(int j=0;j<ma[9].length();j++){
                m[ma[9][j]]--;
            }
        }
        sort(v.begin(),v.end());
        for(int i=0;i<v.size();i++){
            cout<<v[i];
        }
        cout<<endl;
    }
    return 0;
}