#include <iostream>
#include <algorithm>

using namespace std;

long long arr[102];
long long add[102];


int main()
{
	long long t,t2,a,n,i,ans,count,count2;
	cin>>t;
	t2=t;
	while(t2--)
	{
		ans=0;
		count=0;
		cin>>a>>n;
		for(i=0;i<n;i++)
		{
			add[i]=0;
			cin>>arr[i];
		}
		sort(arr,arr+n);
		for(i=0;i<n;i++)
		{
			if(arr[i]<a)
			{
				a+=arr[i];
				continue;
			}
			else
			{
				if(a+a-1>arr[i])
				{
					count++;
					add[i]++;
					a+=a-1;
					a+=arr[i];
				}
				else
				{
				    if(a==1)
                    {
                        ans=n;
                        break;
                    }
					count++;
					add[i]++;
					a+=a-1;
					i--;
				}
			}
		}
		for(i=0;i<n;i++)
		{
			if(add[i]!=0)
			{
				if(count>n-i)
				{
					ans+=n-i;
					break;
				}
				else
				{
					count-=add[i];
					ans+=add[i];
				}
			}
		}
		cout<<"Case #"<<(t-t2)<<": ";
		cout<<ans<<endl;


	}
	return 0;
}
