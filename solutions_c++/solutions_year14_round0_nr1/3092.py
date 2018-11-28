#include<iostream>
using namespace std;
int main()
{
	int T;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		int m,n;
		cin>>m;
		int first[4][4],second[4][4];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>first[i][j];
		cin>>n;	
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>second[i][j];	
						
		int c=0;
		int match=-1;	
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)	
		{
			if(first[m-1][i]==second[n-1][j])
			{
				c++;
				match=first[m-1][i];
			}	
		}
		if(c==0)
			cout<<"Case #"<<(t+1)<<": "<<"Volunteer cheated!"<<endl;
		else if(c==1)
			cout<<"Case #"<<(t+1)<<": "<<match<<endl;
		else 
			cout<<"Case #"<<(t+1)<<": "<<"Bad magician!"<<endl;
	}
	return 0;		

}