#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<string>
#include<algorithm>
#include<queue>
#include <deque>
#include <bits/stdc++.h>
typedef unsigned long long int ulli;
typedef unsigned long int uli;
typedef long long int lli;
typedef long int li;
using namespace std;


int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        string s;
        cin>>s;
        deque<char> myd;
        myd.push_front(s[0]);
        for(int j=1;j<s.length();j++){
            if(s[j]>=myd[0]){
                myd.push_front(s[j]);
            }
            else{
                myd.push_back(s[j]);
            }
        }

        printf("Case #%d: ",i);
        for(int j=0;j<s.length();j++){
            printf("%c",myd[j]);
        }
        printf("\n");

    }
return 0;
}
