#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
bool prime[100000011];
ll pp[5761456];
ll arr[13];
char brr[100];
//ll brr[13];
ll size;
FILE * pFile;

ll num(string str)
{
	ll count=0;
	memset(arr,0,sizeof(arr));
	//memset(brr,0,sizeof(brr));
	ll flag=0;
	for(ll j=2;j<=10;j++)
	{
		
		ll sum=0,i;
		ll n=str.size();
		ll mul=1;
		for(i=0;i<n;i++)
		{
			sum=sum+(str[i]-'0')*mul;
			mul*=j;
		}	
		for(i=0;i<size;i++)
		{
			if(sum<=pp[i])
			{
				flag=1;
				break;
			}
			//cout<<"kk"<<endl;
			if(sum%pp[i]==0)
			{
				//brr[j]=sum;
				arr[j]=pp[i];
				count++;
				break;
			}
			
		}
		if(flag==1)
		break;
	}
	
	if(count==9)
	{
		reverse(str.begin(),str.end());
		ll n=str.size();
		for(ll i=0;i<n;i++)
		{
			brr[i]=str[i];
		}
		fprintf (pFile, "%s ",brr);
		for(ll j=2;j<=10;j++)
		{
			fprintf (pFile, "%lld ",arr[j]);
		}
		fprintf (pFile, "\n");
		return 1;
	}
	return 0;
}
int main()
{
	pFile = fopen ("output.txt","w");
	ll t,i,j;
	ll n,m;
	cin>>t;
	cin>>n>>m;
	prime[1]=1;
	ll k=0;
	for(i=2;i*i<100000010;i++)
	{
		for(j=i*2;j<100000010;j+=i)
		{
			if(prime[j]==0)
			{
				prime[j]=1;
			}
		}
	}
	for(i=2;i<100000010;i++)
	{
		if(prime[i]==0)
		{
		
			pp[k++]=i;
			//cout<<i<<endl;
		}
	}
	
	size=k;
	
	ll s=n-2;
	string str="";
	ll count=0;
	fprintf (pFile, "Case #1:\n");
	for(i=0;i<(1<<s);i++)
	{
		str="1";
		for(j=0;j<s;j++)
		{
			if(i&(1<<j))
			{
				str+="1";
			}
			else
			str+="0";
		}
		str+="1";
		//cout<<str<<endl;
		//reverse(str.begin(),str.end());
		if(num(str))
		{
			count+=1;
		}
		if(count==m)
		break;
	}
	
}
