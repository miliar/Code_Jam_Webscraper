#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
	//FILE*f1=freopen ("w12.in", "r", stdin);
	//FILE*f2=freopen ("ouw12.txt", "w", stdout);
	int t,s,x,p,n,y,counte[12],i;
  cin>>t;
  for(s=1;s<=t;s++)
  {
	cin>>n;
    printf("Case #%d: ",s);
    if(n==0)
    {
      printf("INSOMNIA\n");  
    }
    else
    {
		for(i=0;i<10;i++)
		counte[i]=0;
       x=0; p=1;
       while(x!=10)
       {
         y=p*n;
         while(y!=0)
         {
            if(counte[y%10]!=1)
            {counte[y%10]=1;x++;}
            y=y/10;
         }
         p++;
       }
       p--;
       printf("%d\n",p*n);
    }
  }
 return 0;
}
