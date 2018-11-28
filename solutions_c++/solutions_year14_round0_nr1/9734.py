#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t=1;
	int T;
	cin>>T;
	while(t<=T)
	{
		int row1;cin>>row1;
		int arr[5];
		int temp;
		for(int i=1;i<5;i++)
			{
				if(i!=row1){for(int j=1;j<5;j++)cin>>temp;}
				else{for(int j=1;j<5;j++)cin>>arr[j];}
		    }
		int row2;cin>>row2;
		int brr[5];
		for(int i=1;i<5;i++)
		{
			if(i!=row2){for(int j=1;j<5;j++)cin>>temp;}
			else{for(int j=1;j<5;j++)cin>>brr[j];}
	    }
	    int flag;int crr[5]={0};
	    for(int i=1;i<5;i++)for(int j=1;j<5;j++)if(arr[i]==brr[j]){flag=arr[i];crr[i]=1;}
	    int count=0;
	    for(int i=1;i<5;i++)if(crr[i]==1)count++;

		cout<<"Case #"<<t<<": ";
	    if(count==1)cout<<flag<<endl;
	    else if(count>1)cout<<"Bad magician!"<<endl;
	    else cout<<"Volunteer cheated!"<<endl;
	    t++;

	}
	return 0;
}