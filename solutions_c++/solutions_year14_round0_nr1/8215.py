# include<iostream>
using namespace std;
int main ()
{
	int t,num1,num2,count,index;
	int arr1[4][4],first[4][4];
	cin>>t;
	for(int i=0;i<t;i++)
	{
		count=0;
	cin>>num1;
	for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
		cin>>arr1[j][k];
	cin>>num2;
	for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
		cin>>first[j][k];
		
	for(int m=0;m<4;m++)
	 for(int k=0;k<4;k++)
		if(arr1[num1-1][m]==first[num2-1][k])
				{
				   ++count;
					index=m;	
				}
	cout<<"Case #"<<i+1<<": ";
	if(count==1)
	cout<<arr1[num1-1][index];
	else if(count>1)
	cout<<"Bad magician!";
	else
	cout<<"Volunteer cheated!";
	cout<<endl;
	}
	return 0;
}