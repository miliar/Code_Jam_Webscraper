#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;

int check(vector<double>a,vector<double>b,int n1,int n2)
{
	if(n1>=a.size() || n2>=b.size()) return 0;
	if(a[n1]>b[n2]){ return 1+check(a,b,n1+1,n2+1);}
	else return check(a,b,n1+1,n2);
}
int main()
{
	int t;
	cin>>t;
	for(int q=0;q<t;q++)
	{
		int n;cin>>n;
		vector<double> a,b;
		for(int i=0;i<n;i++)
		{
			double x;cin>>x;
			a.push_back(x);
		}
		for(int i=0;i<n;i++)
		{
			double x;cin>>x;
			b.push_back(x);
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		
		int counter1=0,counter2=0,c1=0,c2=0;
		for(int i=n-1;i>=0;i--)
		{
			if(b[i]>a[n-1]) counter1++;
			else break;
		}
		counter2=check(a,b,counter1,0);
		
		
		
		cout<<"Case #"<<q+1<<": "<<counter2;
		
		bool bl[b.size()];
		for(int i=0;i<b.size();i++)
		{
			bl[i]=true;
		}
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				if(a[i]<b[j] && bl[j]) {
					bl[j]=false;
					c2++;break;
				}}}
			
		cout<<" "<<n-c2<<endl;
	}
	/*vector<double>a,b;
	int t;
	cin>>t>>t;
	for(int i=0;i<t;i++) {int x;cin>>x;a.push_back(x);cout<<a[i]<<endl;}
	for(int i=0;i<t;i++) {int x;cin>>x;b.push_back(x);cout<<b[i]<<endl;}
	cout<<check(a,b,0,0)<<endl;
	*/
}
