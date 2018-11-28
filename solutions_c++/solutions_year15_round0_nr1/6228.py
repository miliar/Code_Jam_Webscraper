#include <iostream>
using namespace std;

int main() {
	int t=0,num=0;

	cin>>t;
	int inc=1;
	while(t--!=0)
	{
		int ans=0,temp =0,flag=0,bong=0;
		char a[1005];
		cin>>num;
		cin>>a;
		temp = a[0]-48;
		//cout<<temp;
		for(int i=1;i<=num;i++)
		{

			if(a[i]!='0' && i>temp)
			{
				ans = ans+i-temp;
				flag =1;
				bong = i-temp;
			}

		//cout<<ans<<" "<<temp<<" ";

			if(flag ==0)temp = temp +a[i]-48;
			else temp = temp +a[i]-48+bong;

			flag=0;
		}
		cout<<"case #"<<inc++<<": "<<ans<<"\n";
	}
	return 0;
}
