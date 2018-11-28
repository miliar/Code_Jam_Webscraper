
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~//           Author : Sarvesh Mahajan                             
//               IIIT,Hyderabad                                   
//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define For(i,a,b) for(i=a;i<b;i++)
#define loop(i,b) for(i=0;i<b;i++)
#define Loop(i,b) for(i=1;i<=b;i++)
#define pi(n) printf("%d ",n)
#define si(n) scanf("%d",&n)
const int MOD=1e9+7;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef long long LL;
int arr[10],arr2[10];
int main()
{
int n,t,m,l,k,ans,i,j,res=0,fl,f,x,ss,ct;
//t=1;
si(t);
int T=t;
Loop(t,T)
{
	ct=0;
	si(f);
	loop(i,4)
	{
		loop(j,4)
		{
			si(x);
			if(i == f-1)
				arr[ct++]=x;
		}
	}
	ct=0;

	si(ss);
	loop(i,4)
	{
		loop(j,4)
		{
			si(x);
			if(i == ss-1)
				arr2[ct++]=x;
		}
	}
	res=0;
	int val;


	loop(i,4)
	{
		loop(j,4)
		{
			if(arr[i] == arr2[j])
			{
				val=arr[i];
				res++;
			}
		}
	}
	printf("Case #%d: ",t);

	if(res == 1)
		printf("%d\n",val);
	else if(res>1)
		puts("Bad magician!");
	else puts("Volunteer cheated!");







			


}
return 0;
}
