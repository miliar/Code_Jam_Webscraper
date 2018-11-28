#include<iostream>
#include "bits/stdc++.h"
// coolboy95
using namespace std;

int main()
{
 int t,k=1;
 scanf("%d",&t);
 while(t--)
 {
 	 int x,r,c,tp;
 	scanf("%d %d %d",&x,&r,&c);
 	tp=r*c;
 	if(x==1)
 	{
 	 printf("Case #%d: GABRIEL\n",k);
 	}
 	else if(x==2)
 	{
 	 if(tp%2==0)
 	 printf("Case #%d: GABRIEL\n",k);
 	 else printf("Case #%d: RICHARD\n",k);
 	}
 	else if(x==3)
 	{
 	 if(tp%3==0)
 	 {
 	 if(tp==6 || tp==9 || tp==12 || tp==15)
 	 printf("Case #%d: GABRIEL\n",k);
 	 else printf("Case #%d: RICHARD\n",k);
 	 }
 	 else printf("Case #%d: RICHARD\n",k);
 	}
 	else if(x==4)
 	{
 	 if(tp%4==0)
 	 {
 	 if(tp==12 || tp==16)
 	 printf("Case #%d: GABRIEL\n",k);
 	 else printf("Case #%d: RICHARD\n",k);
 	 }
 	 else printf("Case #%d: RICHARD\n",k);
 	}
 	k++;
 }
 return 0;
}