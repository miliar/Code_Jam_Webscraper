#include<bits/stdc++.h>
using namespace std;
 
typedef long long int lli;
   
#define pc(x) putchar_unlocked(x);
#define gc() getchar_unlocked();
#define ITR(x,c) for(__typeof(c.begin()) x=c.begin();x!=c.end();x++)
#define F(i, a,b) for( i=a;i<b;i++)
#define ZERO(a) memset(a,0,sizeof(a))
#define M 1000000007
#define pi 3.14159265358
#define pb push_back 
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)

int main()
{freopen("A.in","r",stdin);
freopen("google.txt","w",stdout);

int t;
sl(t);
while(t--)
{lli n,j,i,k,l;
sl(n);
sl(j);
lli x=pow(2,14);
lli arr[11];
arr[2]=pow(2,15)+1;
arr[3]=pow(3,15)+1;
arr[4]=pow(4,15)+1;
arr[5]=pow(5,15)+1;
arr[6]=pow(6,15)+1;
arr[7]=pow(7,15)+1;
arr[8]=pow(8,15)+1;
arr[9]=pow(9,15)+1;
arr[10]=pow(10,15)+1;
map<lli,vector<lli> >mp;
for(i=0;i<x;i++)
{for(l=2;l<=10;l++)
{
lli y=arr[l];	

	for(k=0;k<14;k++)
	{
		if(i&(1<<k))
		{
			y+=pow(l,k+1);
			}
			}
			int flag=0;
			for(k=2;k<=sqrt(y);k++)
			{if(y%k==0)
			{
				flag=1;
				break;}
				}
				if(!flag)
				break;
				else mp[i].pb(k);
			}
			if(l==11)
			j--;
			else mp.erase(i);
			if(j==0)
			break;
			
}
cout<<"Case #1:\n";
ITR(it,mp)
{
	int arr1[16];
	ZERO(arr1);
	arr1[15]=1;
	arr1[0]=1;
	i=14;
	
	lli a=it->first;
	while(a)
	{if(a%2==1)
	arr1[i]=1;
	else arr1[i]=0;
	i--;
	a=a/2;
	
		}
		F(i,0,16)
		cout<<arr1[i];
		cout<<" ";	
	for(i=0;i<mp[it->first].size();i++)
	{
		cout<<mp[it->first][i]<<" ";
		}
		cout<<"\n";
}	
}

return 0;
    }    
