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


int main()
{
	freopen("input3.in","r",stdin);
	freopen("output1.txt","w",stdout);
	lli count,t,n,res,number,l,copy_num;
	cin>>t;
	for(lli test=1;test<=t;test++)
	{
		count=0;
		res=0;
		lli arr[10];
		for(lli i=0;i<10;i++)
			arr[i]=0;
		cout<<"Case #"<<test<<": ";
		cin>>n;
		if(n==0)
		{
			cout<<"INSOMNIA\n";
			continue;
		}
		/*if(number%10==0)
			{
				arr[0]=1;
				count++;
			}
			while(float(n)/10.0==(float)(n/10))
			n=n/10;
		*/
		for(lli i=1;i<=100000*n;i++)
		{
			number=i*n;
			copy_num=number;
			while(number!=0)
			{
				l=number%10;
				if(arr[l]==0)
				{
					//cout<<"count++ at l="<<l<<endl;
					count++;
					arr[l]+=1;
				}
				number/=10;
			}
			if(count==10)
			{
				res=1;
				break;
			}
		}
		if(res==1)
			cout<<copy_num<<endl;
		else
			cout<<"INSOMNIA\n";
	}
    return 0;
}
