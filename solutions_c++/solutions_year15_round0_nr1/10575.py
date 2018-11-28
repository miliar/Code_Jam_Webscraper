#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	int k=1;
	while(t--)
	{
		int n;
		cin>>n;
		string a;
		cin>>a;
		int sum = 0;
		int c = 0;
		for(int i=0;i<n+1;i++)
		{	
			if(sum-i<0&&a[i]!='0')
			{
				c+=(i-sum);
				sum+=c;
			}
			sum+=(a[i]-'0');
			//cout<<c<<"-"<<sum<<" ";
		}
		cout<<"Case #"<<k++<<": "<<c<<endl;
	}
	return 0;
}