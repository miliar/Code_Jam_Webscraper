#include<bits/stdc++.h>
using namespace std;

int main()
{  
	int T, n, x, ten=1;
	bitset<10> dp;
	int flag=0;
	scanf("%d",&T);
	int i=0;
	while(T)
	{  T--;
		i++;
	   scanf("%d",&n);
	   if(n==0) {printf("CASE #%d: INSOMNIA\n",i); continue; }
	   dp.reset();
	   flag=0;
	   x=0;
	   while(flag<10)
	   {  x=x+n;  
		  ten=1;
	      for(ten=1;ten<=x;ten*=10)
	        if(!dp[(x/ten)%10]) {dp[(x/ten)%10]=1; flag++;}
	      // cout<<x<<endl;
	   }   
	   printf("CASE #%d: %d\n",i,x);
    }	
}
