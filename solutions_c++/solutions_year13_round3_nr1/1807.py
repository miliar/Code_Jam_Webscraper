#include <iostream>
#include <string>
#include <stdio.h>
#include <sstream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <cmath>
#include <cstring>

using namespace std;

vector<string>SubstringGenerate(string str);
map<string,int>mp;
int main()
{
        freopen("a.txt", "r", stdin);
    freopen("a.out", "w", stdout);
    string str;
    vector<string>store;
    int i, j, k, t, X, O, T, Dot,cas=1,cnt;
    scanf("%d",&t);
    while(t-- && cin>>str>>k)
    {
        mp.clear();
        store=SubstringGenerate(str);cnt=0;
       // cout<<store.size()<<endl;
        for(i=0;i<store.size();i++){
            //cout<<store[i]<<endl;
            if(store[i].size()>=k && mp[store[i]]==0){
                O=0;
                //mp[store[i]]=1;
                for(j=0;j<store[i].size();j++)
                 {
                     if(store[i][j]!='a' && store[i][j]!='e' && store[i][j]!='i' && store[i][j]!='o' && store[i][j]!='u')
                        O++;
                     else
                        O =0;
                     if(O>=k) {cnt++; break;}
                 }
            }
        }
            printf("Case #%d: %d\n",cas++,cnt);
    }
}

vector<string>SubstringGenerate(string str)
{
    int i,j,len;
    vector<string>store;

    len=str.size();
    for(i=0;i<len;i++)
    {
        for(j=i;j<len;j++)
            store.push_back(str.substr(i,j-i+1));
    }
    return store;
}
