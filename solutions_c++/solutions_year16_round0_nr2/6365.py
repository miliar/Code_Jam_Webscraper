#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("revenge of the pancakes.txt","w",stdout);
    int t;
    cin>>t;
    for(int i = 1; i <= t; i++){
        string s;
        cin>> s;
        int ls;
        for(int j = 0; j < s.size(); j++){
            if(s[j] == '-')ls = j;
        }
       // cout<<ls<<endl;
        int cnt = 0, take = ls, cntp = 0;
        //for(int i = 0; i<= ls; i++)cout<<s[i];
        for(int j = 0; j < s.size(); j++){if(s[j] == '+') cntp++;}
        if(cntp == s.size()){printf("Case #%i: 0\n", i);continue;}
        cntp = 0;
        while(1){
            //    if(ls == 0)break;
            for(int j = 0; j <= ls; j++){
                if(s[j] == '+')s[j] = '-';
                else s[j] = '+';
               // cout<<s[j];
            }
            cnt++;
            for(int j = 0; j < s.size(); j++){if(s[j] == '+')cntp++;if(s[j] == '-')ls = j;}
            //cout<<ls<<"  "<<take<<" "<<cntp<<endl;
            //if(take == ls){break;}
           // cout<<cntp<<" "<<ls<<endl;
            if(cntp == s.size() and take == ls)break;
            cntp = 0;
            take = ls;
            //cout<<ls<<" "<<take<<endl;
        }
        cntp=0;
        printf("Case #%i: %i\n", i, cnt);
    }
}
