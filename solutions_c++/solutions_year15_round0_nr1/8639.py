#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int i;cin>>i;
	for(int n=0;n<i;n++)
	{
		int j;
		cin>>j;
		int sum=0,t=0;
		int k=0;
		char s[j];
		cin>>s;
		while(k<=j)
		{
			if(sum<k)
			{
			int te=k-sum;
			sum=sum+te;
			t=t+te;
			}
			int g=s[k++]-'0';
			sum=sum+g;
		}
		cout<<"Case #"<<n+1<<": "<<t<<endl;
	}

	return 0;
}