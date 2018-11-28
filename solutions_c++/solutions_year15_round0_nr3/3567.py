#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
map<pair<ll,ll>,ll> m;
map<char,ll>m1;
map<pair<ll,ll>,ll>::iterator it;
ll sum[100000];
ll arr[100000];
ll brr[100000];
int main()
{
	ifstream fin("input.in");
	ofstream fout("output.txt");
	m[make_pair(1,1)]=1;
	m[make_pair(1,3)]=3;
	m[make_pair(1,5)]=5;
	m[make_pair(1,7)]=7;
	m[make_pair(1,2)]=2;
	m[make_pair(1,4)]=4;
	m[make_pair(1,6)]=6;
	m[make_pair(1,8)]=8;
	m[make_pair(2,1)]=2;
	m[make_pair(2,3)]=4;
	m[make_pair(2,5)]=6;
	m[make_pair(2,7)]=8;
	m[make_pair(2,2)]=1;
	m[make_pair(2,4)]=3;
	m[make_pair(2,6)]=5;
	m[make_pair(2,8)]=7;
	m[make_pair(3,1)]=3;
	m[make_pair(3,3)]=2;
	m[make_pair(3,5)]=7;
	m[make_pair(3,7)]=6;
	m[make_pair(3,2)]=4;
	m[make_pair(3,4)]=1;
	m[make_pair(3,6)]=8;
	m[make_pair(3,8)]=5;
	m[make_pair(4,1)]=4;
	m[make_pair(4,3)]=1;
	m[make_pair(4,5)]=8;
	m[make_pair(4,7)]=5;
	m[make_pair(4,2)]=3;
	m[make_pair(4,4)]=2;
	m[make_pair(4,6)]=7;
	m[make_pair(4,8)]=6;
	m[make_pair(5,1)]=5;
	m[make_pair(5,3)]=8;
	m[make_pair(5,5)]=2;
	m[make_pair(5,7)]=3;
	m[make_pair(5,2)]=6;
	m[make_pair(5,4)]=7;
	m[make_pair(5,6)]=1;
	m[make_pair(5,8)]=4;
	m[make_pair(6,1)]=6;
	m[make_pair(6,3)]=7;
	m[make_pair(6,5)]=1;
	m[make_pair(6,7)]=4;
	m[make_pair(6,2)]=5;
	m[make_pair(6,4)]=8;
	m[make_pair(6,6)]=2;
	m[make_pair(6,8)]=3;
	m[make_pair(7,1)]=7;
	m[make_pair(7,3)]=5;
	m[make_pair(7,5)]=4;
	m[make_pair(7,7)]=2;
	m[make_pair(7,2)]=8;
	m[make_pair(7,4)]=6;
	m[make_pair(7,6)]=3;
	m[make_pair(7,8)]=1;
	m[make_pair(8,1)]=8;
	m[make_pair(8,3)]=6;
	m[make_pair(8,5)]=3;
	m[make_pair(8,7)]=1;
	m[make_pair(8,2)]=7;
	m[make_pair(8,4)]=5;
	m[make_pair(8,6)]=4;
	m[make_pair(8,8)]=2;
	m1['i']=3;
	m1['j']=5;
	m1['k']=7;

	ll t;
	fin>>t;
	ll dd=0;
	while(t--)
	{
		dd++;
		ll l,x;
		ll flag=0;
		fin>>l>>x;
		string str;
		string str1="";
		fin>>str;
		for(ll i=0;i<x;i++)
		{
			str1+=str;
		}
		
		arr[0]=m1[str1[0]];
		ll k=0;
		ll ind=0;
		for(ll i=0;i<l*x;i++)
		{
			arr[i]=m1[str1[i]];
		}
		/*for(ll i=0;i<l*x;i++)
		{
			cout<<arr[i]<<" ";
		}*/
		brr[0]=arr[0];
		if(arr[0]==3)
		{
			sum[k++]=0;
		}
		for(ll i=1;i<l*x;i++)
		{
			brr[i]=m[make_pair(brr[i-1],arr[i])];
			
			if(brr[i]==3)
			{
				sum[k++]=i;
			}
			if(brr[i]==7)
			{
				ind=i;
			}
		}
		//cout<<endl;
	/*for(ll i=0;i<l*x;i++)
		{
			cout<<brr[i]<<" ";
		}
		cout<<endl;
	for(ll i=0;i<k;i++)
		{
			cout<<sum[i]<<" ";
		}*/
		if(brr[l*x-1]!=2)
		{
			flag=0;
		}
		else
		{
		
		for(ll i=0;i<k;i++)
		{
			if(sum[i]<ind)
			{
				flag=1;
				break;
				
			}
			
		}
	}
	
	if(flag==1)
	{
	    fout<<"Case #"<<dd<<": "<<"YES"<<endl;	
	}	
	else
	{
		fout<<"Case #"<<dd<<": "<<"NO"<<endl;
	}
		
	}
	return 0;
}
