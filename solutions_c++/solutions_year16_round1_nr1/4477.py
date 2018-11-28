#include <iostream>
#include <cstdio>
#include <vector>
#include <bits/stdc++.h>
#include <algorithm>
#include <queue>
#include <cstring>
#define PB push_back
using namespace std ;
long long m,ll;
map<long long,int>name;
int main(){
   freopen("A-large (1).in","r",stdin);
    freopen("out.o","w",stdout);
    int test,u=1;
    cin>>test;
    while(test--){
     string str,str2;
     cin>>str;
     for(int i=0;str[i];i++){
        if(i==0)str2=str2+str[i];
        else{
            if(str2[0]<=str[i])str2=str[i]+str2;
            else str2=str2+str[i];

        }
     }
     printf("Case #%d: ",u++);
     cout<<str2<<endl;
    }
return 0;
}
