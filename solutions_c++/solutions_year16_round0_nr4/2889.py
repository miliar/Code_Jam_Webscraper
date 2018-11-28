#include<iostream>
using namespace std;
int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("q4_sm.out","w",stdout);
	int t;
	cin>>t;
	int kk=0;
	while(t--)
	{
		kk++;
		int k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<kk<<": ";
		for(int i=1;i<=s;i++)
		{
			cout<<i<<" ";
		}
		cout<<endl;
	}
	return 0;
}
