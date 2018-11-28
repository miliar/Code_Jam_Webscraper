#include<iostream>
#include<stdio.h>
using namespace std;
#define ll long long
int main(){
     int t,a,b,k;
     freopen("B-small-attempt1.in","r",stdin);
     freopen("yxout","w",stdout);
     cin>>t;
     for(int tt=1;tt<=t;tt++){
        cin>>a>>b>>k;
        int ans=0;
        for(int i=0;i<a;i++){
            for(int j=0;j<b;j++){
                int x=i&j;
                if(x>-1&&x<k)ans++;
            }
        }
        printf("Case #%d: %d\n",tt,ans);
     }
     return 0;
}
