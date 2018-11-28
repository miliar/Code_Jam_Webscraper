#include <iostream>
using namespace std;
int a[16],b[16],row1,row2,ans,count,n,k,l,j;
int main() {
	// your code goes here
	cin>>n;
	l=0;
	while(l<n)
	{
	ans=0,count=0;
	cin>>row1;
	for(int i=0;i<16;i++)
	cin>>a[i];
	cin>>row2;
	for(int i=0;i<16;i++)
	cin>>b[i];
	for(j=4*(row1-1);j<4*(row1-1)+4;j++)
	{for(k=4*(row2-1);k<4*(row2-1)+4;k++)
	if(a[j]==b[k])
	{
		count++;
		ans=a[j];
	}
	
	}
	
	if(ans==0)
	{
	
	if(l!=n-1)
	cout<<"Case #"<<l+1<<": "<<"Volunteer cheated!\n";
	else
	cout<<"Case #"<<l+1<<": "<<"Volunteer cheated!";
	}
	else if(count>1)
	{
	if(l!=n-1)	
	cout<<"Case #"<<l+1<<": "<<"Bad magician!\n";
	else
	cout<<"Case #"<<l+1<<": "<<"Bad magician!";
	}
	else
	{
	if(l!=n-1)	
	cout<<"Case #"<<l+1<<": "<<ans<<"\n";
	else
	cout<<"Case #"<<l+1<<": "<<ans;
	}
	l++;
	}
	return 0;
}