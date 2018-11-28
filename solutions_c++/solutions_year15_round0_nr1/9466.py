#include <fstream>
#include<iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;
int main (void){
        freopen ("A-large.in","r",stdin);
        freopen ("output.txt","w",stdout);
        int t,i,j;
        cin>>t;
        for(i=0;i<t;i++)
        {
            int l;
            cin>>l;
             string s;
             cin>>s;
             int sum=0,need=0;
             for(j=0;j<=l;j++)
             {
                 if(s[j]>48)
                 {
                     if(sum>=j)
                     {
                         sum=sum+(s[j]-48);
                     }
                     else
                     {
                         need=need+(j-sum);
                         sum=sum+(s[j]-48)+(j-sum);
                     }
                 }
             }
             cout <<"Case #"<<(i+1)<<": "<<need<<"\n";
        }
    
}