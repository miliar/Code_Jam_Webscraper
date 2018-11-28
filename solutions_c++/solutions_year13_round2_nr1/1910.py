#include<iostream>
#include<algorithm>
#define N 101
using namespace std;
int main()
{	int i,j,t,n,motes[N];
	unsigned long long a,cnt,tmp;
	cin>>t;
	for(i=1;i<=t;i++)
	{	cin>>a>>n;
		tmp=cnt=0;
		for(j=0;j<n;j++)
			cin>>motes[j];
		sort(motes,motes+n);
		for(j=0;j<n;)
		{	if(motes[j]<a)
			{	if(tmp>(n-j-1))
				{	cnt+=(n-j);
					break;
				}
				else
					cnt+=tmp;
				a+=motes[j++];
				tmp=0;
			}
			else
			{	if(a==1)
				{	cnt=n;
					break;
				}
				a+=(a-1);
				tmp++;	
			}
		}
		cout<<"Case #"<<i<<": "<<(cnt<n?cnt:n)<<endl;
	}
	return 0;
}