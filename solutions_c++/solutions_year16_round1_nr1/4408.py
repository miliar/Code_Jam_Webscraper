#include <iostream>
#include <cstring>
using namespace std;

int main() {
	long long int t,length,i,j,k;
	char str[1001],temp[1001];
	cin>>t;
	for(i=0;i<t;i++)
{
	
	cin>>str;
	length = strlen(str);
	temp[0] = str[0];
	for(j=1;j<length;j++)
	{
		if(str[j]<temp[0])
		{
			temp[j]=str[j];
		}
		else
		{
			for(k=j;k>0;k--)
			temp[k]=temp[k-1];
			temp[0]=str[j];
		}
	}
	cout<<"Case #"<<i+1;": ";
	for(j=0;j<length;j++)
	cout<<temp[j];
	cout<<endl;
}
	return 0;
}