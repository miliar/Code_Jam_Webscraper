#include<iostream>
//#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#define mod 1000000007

using namespace std;

long long s[40]={1,2,3,11,22,101,111,121,202,212,1001,1111,2002,10001,10101,10201,11011,11111,11211,20002,20102,100001,101101,110011,111111,200002,1000001,1001001,1002001,1010101,1011101,1012101,1100011,1101011,1102011,1110111,1111111,2000002,2001002};

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,i,j,k,m,n,c=0,f;
    scanf("%d", &t);


	while(t--) 
	{
        long long a,b;
        scanf("%lld%lld", &a, &b);

		m=sqrt(a); 
		n=sqrt(b); 
		if(a!=(m*m)) ++m;
		j=k=0;
		for(i=0;i<39;++i)
		{
			if(m<=s[i])
			
			{
				j=i;
				break;
			}
		}
		f=0;
		for(i=0;i<39;++i)
		{
			if(n<s[i])
			{
				k=i;
				f=1;
				break;
			}
		}
		if(f==0)
		        k=39;


		printf("Case #%d: %d\n",++c,k-j);
		//fprintf("Case #%d: %d\n",++c,k-j);
    }
	
//getch();
return 0;

}


