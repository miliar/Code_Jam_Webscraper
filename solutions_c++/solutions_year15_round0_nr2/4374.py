#include<bits/stdc++.h>
using namespace std;
#define LL long long int
vector<int> a;
int n;
LL time2(int x)
{
	// a is already sorted
	int i;
	int ans=0;
   	for(i=1;;i++)
   	{
   		int pos=upper_bound(a.begin(),a.end(),i*x)-a.begin();
   		//cout<<"pos="<<pos<<endl;
   		if(pos>=n)break;//all are smaller than i*x
   		ans+=(n-pos);
   	}
   	return ans;
}
int main()
{
	int t;
	cin>>t;
	int t2=0;
	while(t--)
	{
	t2++;
	LL d,i;
	cin>>d;
	n=d;
	a.clear();
	a.resize(d);
	
	for(i=0;i<d;i++)cin>>a[i];
	sort(a.begin(),a.end());
	LL mx=a[d-1];
	LL ans=999999999;
	for(i=1;i<=mx;i++)
	{
		LL x=time2(i);
	//	cout<<i<<" "<<x<<endl;
		if(x+i<ans)ans=x+i;
	}
	cout<<"Case #"<<t2<<": "<<ans<<endl;
	}
} 
