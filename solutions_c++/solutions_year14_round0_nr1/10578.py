#include<iostream>
using namespace std;


int a1,a2,m1[4][4],m2[4][4];	
	
int findno(int number)
{
	for(int j=0;j<4;j++)	
		if(number==m2[a2-1][j])
			return 1;
 return 0;
}


int main()
{
	int t,i,no;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int res=0,flag=0;
		cin>>a1;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>m1[j][k];

		cin>>a2;
		for(int j=0;j<4;j++)
			for(int k=0;k<4;k++)
				cin>>m2[j][k];

		for(int j=0;j<4;j++)
		{
			
			res+=findno(m1[a1-1][j]);
			if(res==1 && flag==0){
				no=m1[a1-1][j];
				flag=1;
			}
		}
		cout<<"Case #"<<i+1<<": ";
		if(res==1)
			cout<<no<<endl;
		else if (res>1)
			cout<<"Bad magician!\n";
		else 
			cout<<"Volunteer cheated!\n";
	}
}
