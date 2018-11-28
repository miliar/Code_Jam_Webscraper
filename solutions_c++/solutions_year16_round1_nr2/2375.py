#include <iostream>
using namespace std;

int main() {
	int t,n,k,i,num,ch=0;
	int arr[10000];
	cin>>t;
	while(t--)
	{
		ch=ch+1;
		cin>>n;
		k=(2*n)-1;
		k=k*n;
		for(i=0;i<2600;i++)
		{
			arr[i]=0;
		}
		for(i=1;i<=k;i++)
		{
			cin>>num;
			arr[num]=arr[num]+1;
		}
		printf("Case #%d: ",ch);
		for(i=0;i<3000;i++)
		{
			if(arr[i]!=0 && arr[i]%2!=0)
			{
				cout<<i<<" ";
			}
		}
		cout<<endl;
	}
	return 0;
}