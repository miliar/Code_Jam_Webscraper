#include<bits/stdc++.h>
#define gc getchar
#define pc putchar
#define pii pair<int,int>
using namespace std;
inline void rdl(int &x)
{
	x=0;
	bool check=false;
	register int c;
	do{
		c=gc();
		if(c=='-')
		check=true;
	}while(c<48 || c>57);
	for(;c>47 && c<58;c=gc()){
		x=(x<<1)+(x<<3)+c-48;
	}
	if(check)
	x=-x;
}
inline void rd(int &x)
{
	x=0;
	bool check=false;
	register int c=gc();
	for(;c<48 || c>57;c=gc());
	for(;c>47 && c<58;c=gc()){
		x=(x<<1)+(x<<3)+c-48;
	}

}
inline void pd(int x)
{
	char c[11];
	bool check=false;
	int k=-1;
	if(x<0)
	check=true,x=-x;
	do
	{
		c[++k]=x%10+48;
		x/=10;
	}while(x);
	if(check)
	c[++k]='-';
	while(k>=0)
	pc(c[k--]);
	pc('\n');
}
inline void pdl(long long int x)
{
	char c[21];
	bool check=false;
	int k=-1;
	if(x<0)
	check=true,x=-x;
	do
	{
		c[++k]=x%10+48;
		x/=10;
	}while(x);
	if(check)
	c[++k]='-';
	while(k>=0)
	pc(c[k--]);
	pc('\n');
}
bool cmp(int  a,int b)
{
	return a>b;
}
int arr[10001];
int main()
{
		ifstream cin("R1L.in");
		ofstream cout("R1AL.txt");
		int n,t,ind=1,i,j,k,mx;
		long long int ans=0,ans1=0;
		cin>>t;
		while(t--)
		{
			mx=-100;
			ans=ans1=0;
			cin>>n;
			cin>>arr[0];
			for(i=1;i<n;i++)
			cin>>arr[i],k=arr[i-1]-arr[i],mx=max(mx,k);
			
			for(i=1;i<n;i++)
			{
				if(arr[i]<arr[i-1])
				ans+=(arr[i-1]-arr[i]);
				
			}
			n--;
			for(i=0;i<n;i++)
			{
				if(mx>0)
				{
				
				if(arr[i]<mx)
					{
						ans1+=arr[i];
					}
				else
				ans1+=mx;	
				}
				else
				break;
			}
			
				cout<<"Case #"<<ind++<<": "<<ans<<" "<<ans1<<endl;
		}
		
		
	
	
	
}
