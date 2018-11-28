#include<iostream>
#include<cstdio>
//#include<algorithm>
//#include<iomanip>
//#include<map>
//#include<cstring>
//#include<vector>
//#include<set>
#include<cmath>
#define MOD 1000000007
using namespace std;
/*
long long powee(long long int ax, long long int b)
{
	if(b==1)
	return ax;
	else if(b==0)
	return 1;
	if(ax==1)
	return 1;
    long long x=1,y=ax; 
    while(b > 0)
    {
        if(b%2 == 1)
        {
            x=(x*y);
            if(x>MOD) x%=MOD;
        }
        y = (y*y);
        if(y>MOD) y%=MOD; 
        b /= 2;
    }
    return x;
}
*/
long long int a[100];
int main()
{
	freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
	long long int i,j,k,l=1,n,t;
	cin>>t;
	while(t--)
	{
		
		long long int sum=0,ma1=-99999999999,ma2=-999999999999,kk;
		cin>>n;
		for(i=0;i<n;i++)
		{
			cin>>a[i];
			sum+=a[i];
		}
		cout<<"Case #"<<l<<": ";
		if(n==1)
		{
			while(sum>=2)
			cout<<"AA"<<" ",sum-=2;
			if(sum>0)
			cout<<"A"<<" ",sum-=1;
		}
		
		else if(n>=2)
		{
			while(sum>0)
			{
				for(i=0;i<n;i++)
				{
				if(ma1<=a[i])
				{
				ma1=a[i];
				k=i;
				}
				}
				for(i=0;i<n;i++)
				{
					if(i!=k)
					{
						if(ma2<=a[i])
						{
							ma2=a[i];
							kk=i;
						}
					}
				}
//				cout<<k<<" "<<ma1<<" "<<kk<<" "<<ma2<<endl;
				if(ma1==ma2&&ma1!=1)
				{
					a[k]-=1;
					a[kk]-=1;
					sum-=2;
					ma1=-9999999999;
					ma2=-9999999999;
					cout<<(char)('A'+k)<<(char)('A'+kk)<<" ";
				}
				if(ma1==ma2&&ma1==1)
				{
					if(sum%2==0)
					{
					a[k]--;
					a[kk]--;
					sum-=2;
					ma1=-9999999999;
					ma2=-9999999999;
					cout<<(char)('A'+k)<<(char)('A'+kk)<<" ";
					}
					else
					{
					a[k]--;
					sum-=1;
					ma1=-9999999999;
					ma2=-9999999999;
					cout<<(char)('A'+k)<<" ";
					}
				}
				else if(ma1!=ma2)
				{
					a[k]-=2;
					sum-=2;
					ma1=-9999999999;
					ma2=-9999999999;
					cout<<(char)('A'+k)<<(char)('A'+k)<<" ";
				}
			}
		}
		cout<<endl;	
		l++;
		}
	
return 0;
}


