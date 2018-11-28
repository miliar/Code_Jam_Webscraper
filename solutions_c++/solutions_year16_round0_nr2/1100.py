#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string.h>
using namespace std;
char b[555],c[555];
int solve()
    {
    int n;
    for(n=0;b[n];n++)c[n] = '+';
    c[n] = 0;
   // printf("%s\n",c);
    int ans = 0;
   string result;
    while(1){
   if(strcmp(b,c)==0)return ans;
        int i,j,k;
        for(j=n-1;j>=0;j--)if(b[j]=='-')break;
        for(i=0;;i++)if(b[i]=='-')break;else b[i] = '-';
           // printf("- are at %d and %d\n",i,j);
            
            if(i>0)ans++;
            reverse(b,b+j+1);
            ans++;
            for(i=0;i<=j;i++)
            if(b[i]=='-')b[i] = '+'; else b[i] = '-';
           // printf("after changing %s\n",b);
            
    }
   // return 555;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int t,ca;
    scanf("%d",&t);
    for(ca=1;ca<=t;ca++)
        {
        scanf("%s",b);
        printf("Case #%d: %d\n",ca,solve());
    }
    return 0;
}
