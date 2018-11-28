#include<iostream>
#include<algorithm>
using namespace std;
int ans,n;
int arr[10000];
int perm[100000];
int main()
{
	int test;
	cin>>test;
	for(int tt=1;tt<=test;tt++)
	{
		ans=0;
		cin>>n;
		for(int i=0;i<n;i++)
		{
			cin>>arr[i];
			arr[i]--;
		}
		for(int len=1;len<(1<<n);len++)
		{
		int pos=0;
			for(int pp=len,jj=0;pp>0;jj++,pp/=2)
			{
					if(pp%2)
					{
						perm[pos]=jj;
						pos++;
					}
			}
			sort(perm,perm+pos);	
		do{
			int ta=0;
			for(int i=0;i<pos;i++)
			{
				if(perm[(i-1+pos)%pos]==arr[perm[i]] || perm[(i+1)%pos]==arr[perm[i]])
				{
					ta++;
				}
				else
				{
					break;
				}
			}
			if(ta==pos && ta>ans)
			{
				ans=ta;
			}
		}while(next_permutation(perm,perm+pos));
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
}
