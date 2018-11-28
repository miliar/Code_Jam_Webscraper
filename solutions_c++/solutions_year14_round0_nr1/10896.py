//#include <fstream>
//#include <iostream>
#include "stdafx.h"
#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
	int T,card,ans1,ans2,res,cardres;
	int a1[4][4],a2[4][4];
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	for(int c=1;c<=T;c++)
	{
		res=0;
		cardres=0;
		cin>>ans1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				cin>>card;
				a1[i][j]=card;
			}
		cin>>ans2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				cin>>card;
				a2[i][j]=card;
			}
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(a1[ans1-1][i]==a2[ans2-1][j])
				{
					res++;
					cardres=a1[ans1-1][i];
				}
		cout<<"Case #"<<c<<": ";
		if(res==0)
			cout<<"Volunteer cheated!"<<endl;
		else if(res==1)
			cout<<cardres<<endl;
		else if(res>1)
			cout<<"Bad magician!"<<endl;
	}
	//outfile.close();
	return 0;
}