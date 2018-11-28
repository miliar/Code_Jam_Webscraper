#include<iostream>
#include<string>
using namespace std;
#define lin long long int
int main()
{
 lin t,n,a[1002];
 cin>>t;
 char temp;
 int caseN=1;
 while(t--)
 {
	cin>>n;
	lin count=0,fri=0;
	for(int i=0;i<=n;i++)
 	{
		cin>>temp;
		a[i]=temp-'0';
		//cout<<count<<"-- "<<i<<endl;
                if(count<i)
		{
			//cout<<count<<"  "<<i<<endl;
			fri+=i-count;
			count+=i-count;
		}
		count=count+a[i];
	}
	cout<<"Case #"<<caseN++<<": "<<fri<<endl;
 }

}
