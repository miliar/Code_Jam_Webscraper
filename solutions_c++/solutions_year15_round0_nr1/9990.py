#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main() { int t;
     scanf("%d",&t);
     for(int j=1;j<=t; j++ )
     { int x,n,c=0,ans=0;
      scanf("%d",&n);  // int a[n+1];
      string s;  cin>> s;
      for(int i=0; i<=n; i++)
       { x=s[i]-'0' ;
         if(x!=0 && c<i) { ans=ans+i-c; c=c+x+i-c ;}
         else c=c+x;
       
       }
       printf("Case #%d: %d\n",j,ans);  
     
     }
     
	return 0;
}
