#include<bits/stdc++.h>
#define lli long long int
#define gc getchar_unlocked
#define MOD 1000000007
using namespace std;


void scan(lli &x)
{
    register lli c = gc();
    x = 0;
    lli neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

lli min3(lli a,lli b,lli c)
{
	return min(a,min(b,c));
}

lli min4(lli a,lli b,lli c,lli d)
{
	return min(a,min(b,min(c,d)));
}

lli min5(lli a,lli b,lli c,lli d,lli e)
{
	return min(a,min(b,min(c,min(d,e))));
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output2.txt","w",stdout);
	lli t,n,cou,temp;
	string str,ans;
	cin>>t;
	for(lli test=1;test<=t;test++)
	{
		ans="";
		lli arr[27]={0};
		cin>>str;
		lli len=str.length();
		for(lli i=0;i<len;i++)
		{
			arr[str[i]-'A']++;
		}
		cou=min4(arr[25],arr[4],arr[17],arr[14]);
		if(cou!=0)
		{
			arr[25]-=cou;
			arr[4]-=cou;
			arr[17]-=cou;
			arr[14]-=cou;
		}
		for(lli i=0;i<cou;i++)	
			ans+="0";

		cou=min3(arr[19],arr[22],arr[14]);
		if(cou!=0)
		{
			arr[19]-=cou;
			arr[22]-=cou;
			arr[14]-=cou;
		}
		for(lli i=0;i<cou;i++)	
			ans+="2";

		cou=min5(arr[4],arr[8],arr[6],arr[7],arr[19]);
		if(cou!=0)
		{
			arr[4]-=cou;
			arr[8]-=cou;
			arr[6]-=cou;
			arr[19]-=cou;
			arr[7]-=cou;
		}
		for(lli i=0;i<cou;i++)	
			ans+="8";

		cou=min4(arr[5],arr[14],arr[20],arr[17]);
		if(cou!=0)
		{
			arr[5]-=cou;
			arr[14]-=cou;
			arr[20]-=cou;
			arr[17]-=cou;
		}
		for(lli i=0;i<cou;i++)	
			ans+="4";

		
		temp=arr[4]/2;
		cou=min4(arr[19],arr[7],arr[17],temp);
		if(cou!=0)
		{
			arr[19]-=cou;
			arr[7]-=cou;
			arr[17]-=cou;
			arr[4]-=cou*2;
		}
		for(lli i=0;i<cou;i++)	
			ans+="3";

		
		cou=min3(arr[14],arr[13],arr[4]);
		if(cou!=0)
		{
			arr[14]-=cou;
			arr[13]-=cou;
			arr[4]-=cou;
		}
		for(lli i=0;i<cou;i++)	
			ans+="1";
		

		cou=min4(arr[5],arr[8],arr[21],arr[4]);
		if(cou!=0)
		{
			arr[5]-=cou;
			arr[8]-=cou;
			arr[21]-=cou;
			arr[4]-=cou;
		}
		for(lli i=0;i<cou;i++)	
			ans+="5";

		cou=min3(arr[18],arr[8],arr[23]);
		if(cou!=0)
		{
			arr[18]-=cou;
			arr[8]-=cou;
			arr[23]-=cou;
		}
		for(lli i=0;i<cou;i++)	
			ans+="6";

		temp=arr[4]/2;
		cou=min4(arr[18],arr[21],temp,arr[13]);
		if(cou!=0)
		{
			arr[18]-=cou;
			arr[21]-=cou;
			arr[13]-=cou;
			arr[4]-=cou*2;
		}
		for(lli i=0;i<cou;i++)	
			ans+="7";

		
		temp=arr[13]/2;
		cou=min3(temp,arr[8],arr[4]);
		if(cou!=0)
		{
			arr[8]-=cou;
			arr[4]-=cou;
			arr[13]-=cou*2;
		}
		for(lli i=0;i<cou;i++)	
			ans+="9";
		sort(ans.begin(),ans.end());
		cout<<"Case #"<<test<<": "<<ans<<endl;
	}

    return 0;
}
