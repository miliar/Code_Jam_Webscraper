#include<bits/stdc++.h>
#define scan(n) scanf("%d",&n)
#define scanll(n) scanf("%lld",&n)
#define For(i,a,b) for(i=a;i<b;i++)
#define fill(a,b) memset(a,b,sizeof(a))
#define swap(a,b) a=a+b;b=a-b;a=a-b;
#define ll long long int
#define pb push_back
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
#define MAX 1000000007
using namespace std;
int abs(int s)
{
	if(s<0)
	s=-s;
	return s;

}
struct point {
	int x;
	int y;
};
int sq(int x)
{
	return x*x;
}
int main()
{
	f_in("A-large.in");
	f_out("A-large1.txt");
	int test,n,i,t;
	scan(test);
	for(t=1;t<=test;t++)
	{
	cout<<"Case #"<<t<<": ";
		scan(n);
		int arr[n+1],res,counter;
		res=counter=0;
		for(i=1;i<=n;i++)
		{
			scan(arr[i]);
			res=res+arr[i];
		}
		if(res%2)
		{
			int m1 = 0,k=0;
			for(i=1;i<=n;i++)
			{
				if(arr[i]>m1)
				{
					m1=arr[i];
					k=i;
				}
			}
			char ch = k+64;
			arr[k]--;
			counter++;
			cout<<ch<<" ";
		}
		while(counter<res)
		{
			int m1,m2,k,l;
			m1=m2=k=l=0;
			for(i=1;i<=n;i++)
			{
				if(arr[i]>m1)
				{
					m2=m1;
					m1=arr[i];
					l=k;
					k=i;
				}
				else if(arr[i]>m2)
				{
					m2=arr[i];
					l=i;
				}
			}
				counter+=2;
				char c1=k+64,c2=l+64;
				cout<<c1<<c2<<" ";
				arr[k]--;
				arr[l]--;	
			
		}
			cout<<endl;
	}
 	return 0;
}


