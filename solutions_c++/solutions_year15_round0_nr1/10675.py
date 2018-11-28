#include <iostream>
#include <stdio.h>
using namespace std;
int main()
{
	freopen("A-small-attempt3 (1).in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,s,x;
	char ch[1001];
	cin>>t;
	int t1=t;
	while(t--)
	{
		cin>>s;
		cin>>ch;
		int sum=0;
		int count=0;
		for(int i=0;i<=s;i++)
		{
			if(sum<i)
			{
			  //  cout<<i<<" "<<i-sum<<" ";
				count=count+(i-sum);
				sum+=(i-sum);
		//		cout<<count<<" "<<sum<<endl;
			}
			switch(ch[i])
			{
				case '0':x=0;
					break;
				case '1':x=1;
					break;
				case '2':x=2;
					break;
				case '3':x=3;
					break;
				case '4':x=4;
					break;
				case '5':x=5;
					break;
				case '6':x=6;
					break;
				case '7':x=7;
					break;
				case '8':x=8;
					break;
				case '9':x=9;
					break;
			}
			sum+=x;
		}
		cout<<"case #"<<(t1-t)<<": "<<count<<endl;
	}
	// your code goes here
	return 0;
}
