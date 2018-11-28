#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,si;
	char s[1010];
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		cin>>si;
		cin>>s;
		int cnt=0;
		int sum=s[0]-'0';
		for(int j=1;j<=si;j++)
		{

			if(sum<j)
			{
				
				cnt+=j-sum;
				sum+=j-sum;
			}
		
			  sum+=s[j]-'0';
			
		}
		cout<<"Case #"<<i<<": "<<cnt<<endl;
	}
	return 0;
}