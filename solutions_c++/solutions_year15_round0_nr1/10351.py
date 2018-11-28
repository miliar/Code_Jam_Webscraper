#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,n,i,sum,no,cnt,j;
	cin>>t;
	for(j=0;j<t;j++)
	{
		sum=0;
		cnt=0;
		cin>>n;
		char s[1005];
		cin>>s;
		for(i=0;i<n+1;i++)
		{
			no=s[i]-48;
			sum+=no;
			if(sum==i)
			{
				cnt++;
				sum++;
			}
		}
		cout<<"Case #"<<j+1<<": "<<cnt<<endl;
	}
	return 0;
}
