#include <iostream>
using namespace std;

int main() {
	int t1,t,inp,flag=0,i,j,num;
	int mat[4][4], sel[4],sel1[4];
	//Inputt T
	cin>>t;
	for(t1=0;t1<t;t1++)
	{
		flag=0;
		//Input First Time
		cin>>inp;
		inp--;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				cin>>mat[i][j];
		}
		for(i=0;i<4;i++)
		{
			sel[i]=mat[inp][i];
		}
		//Input Second Time
		cin>>inp;
		inp--;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
				cin>>mat[i][j];
		}
		for(i=0;i<4;i++)
		{
			sel1[i]=mat[inp][in];
		}
		
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(sel[i]==sel1[j])
				{
					flag++;
					num=sel[i];
				}
			}
		}
		cout<<"Case #"<<t1+1<<": ";
		if(flag==1)
		cout<<num<<endl;
		else if(flag>1)
		cout<<"Bad magician!"<<endl;
		else if(flag==0)
		cout<<"Volunteer Cheated!"<<endl;
	}
	return 0;
}