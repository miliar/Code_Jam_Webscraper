#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
    int i;
	for(int i=0;i<t;i++)
	{ 
		int a;
		cin>>a;
		int b[4][4]={0},d[4][4]={0},e[4]={0},f[4]={0};
		
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>b[j][k];
			}
		}
		
		for(int j=0;j<4;j++)
		e[j]=b[a-1][j];
		
		int c;
		cin>>c;
		
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>d[j][k];
			}
		}
		
		int pos,count=0;
		for(int j=0;j<4;j++)
		f[j]=d[c-1][j];
		
		for(int j=0;j<4;j++)
		{for(int k=0;k<4;k++)
		{
		if(e[j]==f[k]){	
			count++;
		   pos=e[j];
		}
		}
	}
	
	cout<<"Case #";
	if(count==1)
	cout<<i+1<<": "<<pos<<endl;
	else
	if(count>1)
	cout<<i+1<<": "<<"Bad magician!"<<endl;
	else
	if(count==0)
	cout<<i+1<<": "<<"Volunteer cheated!"<<endl;
	
	
	}
	return 0;
}