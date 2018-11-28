#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
	long long int t,n,n1,r,add;
	cin>>t;
	for(long long int j=1;j<=t;j++)
	{
	bool q;
	vector <int> v;
	cin>>n;
	if(n==0)
		cout<<"Case #"<<j<<":"<<" INSOMNIA"<<endl;
	else
	{
	add=n;
	while(v.size()<10)
	{	n1=n;
//		cout<<"n="<<n<<endl;
		while(n>0)
		{
			r=n%10;
			n=n/10;
//			cout<<"r="<<r<<endl;
			sort(v.begin(),v.end());
			if(!binary_search(v.begin(),v.end(),r))
			{
				v.push_back(r);
//				cout<<"r1="<<r<<endl;
			}
		}
		n=n1+add;
	}
//	for(int i=0;i<v.size();i++)
		cout<<"Case #"<<j<<": "<<n1<<endl;
	}
	}
	return 0;
}