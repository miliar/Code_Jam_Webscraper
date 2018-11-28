#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
#define ll long long
#define forr(i,n) for(int i=0;i<n;i++)
#define s(n) scanf("%d",&n)
#define p(n) printf("%d\n",n)
int main(){
    int t;s(t);
    char str[1009];
    forr(j,t){
        int s_max;s(s_max);
        scanf("%s",str);
        int len = s_max+1;
        int ans=0;
        int audi = 0 ;
        forr(i,len){
            if(str[i]!='0' && audi<i){
                ans+=(i-audi);
                audi+=(i-audi);
            }
            if(str[i]!='0'){
                audi+=(str[i]-'0');
            }
        }
        printf("Case #%d: ",j+1);
        p(ans);
    }
}
