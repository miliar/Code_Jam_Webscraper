#include <iostream>
#include<stdio.h>

using namespace std;

int main() {
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("output.txt","wt",stdout);
int t;
cin>>t;
int q=0;
while(t--)
{ q++;
cout<<"Case #"<<q<<": ";
	int arr[4][4],arr1[4][4];
	int i,j,a,b;
	cin>>a;
	
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			cin>>arr[i][j];
		}
	}
	cin>>b;
	int flag=0,ans;
	for(i=0;i<4;i++)
	for(j=0;j<4;j++)
	cin>>arr1[i][j];
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(arr[a-1][i]==arr1[b-1][j])
			{flag++;
			ans=arr[a-1][i];
		}}
	}
	if(flag==0)
	cout<<"Volunteer cheated!"<<endl;
    if(flag==1)
    cout<<ans<<endl;
    if(flag>1)
    cout<<"Bad magician!"<<endl;
    
}



	return 0;
}
