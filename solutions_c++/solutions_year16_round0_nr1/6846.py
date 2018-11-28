#include<bits/stdc++.h>

#define ll 		long long
#define sc(n)	scanf("%d",&n)
#define scll(n)	scanf("%lld",&n)

 using namespace std;

 int main()
 {
 	ll n,temp, atemp;
 	int test, ans,tno = 0,cnt,times,ld;
 	sc(test);
 	while(test--)
 	{
 		tno++;
 		cnt = 0;
 		times = 0;
 		scll(n);
 		if(n==0)
 			atemp = 0;
 		else
 		{
 			temp = n;
	 		int dig[10];
	 		for(int i=0;i<10;i++)
 				dig[i] = 0;
	 		while(1)
	 		{
	 			times++;
	 			temp = n * times;
	 			atemp = temp;
	 			while(temp)
	 			{
	 				ld = temp%10;
	 				if(!dig[ld])
	 				{
	 					dig[ld] = 1;
	 					cnt++;
	 				}
	 				temp = temp/10;
	 				if(cnt>=10)
	 				{
	 					break;
	 				}
	 			}
	 			if(cnt>=10)
	 					break;
	 		}
 		}
 		if(!atemp)
 			printf("Case #%d: INSOMNIA\n",tno);
 		else
 			printf("Case #%d: %lld\n",tno,atemp);
 	}
 }