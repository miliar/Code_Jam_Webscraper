#include<stdio.h>
#include<fstream>
#include<iostream>
using namespace std;
int main()
{
	int t,i,j,s,c,arra[4][4],arrb[4][4],a,b,d=1;
	scanf("%d",&t);
	ofstream out;
	out.open("new.txt",ios::out);
	while(t--)
	{
		scanf("%d",&a);
		a--;
		for(i=0;i<4;i++)
		{
		for(j=0;j<4;j++)
		scanf("%d",&arra[i][j]);
		}

		scanf("%d",&b);
		b--;
		for(i=0;i<4;i++)
		{
		for(j=0;j<4;j++)
		scanf("%d",&arrb[i][j]);
		}
		c=0;
		for(i=0;i<4;i++)
		{
		for(j=0;j<4;j++)
		{
			if(arra[a][i]==arrb[b][j])
			{c++;
			s=arra[a][i];
			}
		}
		}
		if(c==1)
		cout<<s<<endl;
		else if(c==0)
		cout<<"Volunteer cheated!"<<endl;
		else
		cout<<"Bad magician!"<<endl;


		out<<"Case #"<<d++<<": ";
		if(c==1)
		out<<s<<"\n";
		else if(c==0)
		out<<"Volunteer cheated!"<<"\n";
		else
		out<<"Bad magician!"<<"\n";
	}


}