#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int t,a=1;
	cin>>t;
	while(t--)
	{
		int n,i,w;
		cin>>n;
		float ar[n],br[n];
		for(i=0;i<n;i++)
		{
			cin>>ar[i];
		}
		for(i=0;i<n;i++)
		{
			cin>>br[i];
		}
		sort(ar,ar+n);
		sort(br,br+n);
		int j=0;
		i=0;
		while(j!=n)
		{
			if(ar[i]<br[j])
			{
				i++;
				j++;
			}
			else
			j++;
		}
		w=n-i;
		i=0;
		j=0;
		int cnt=0;
		while(i!=n)
		{
			if(ar[i]>br[j])
			{
				i++;
				j++;
				cnt++;
			}
			else
			i++;
		}
		cout<<"Case #"<<a<<":"<<" "<<cnt<<" "<<w<<"\n";
		a++;
	}
	return 0;
}
