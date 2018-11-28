#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main(void) {
	int n,blah=1;
	cin>>n;
	while(n--)
	{
		int cards[4][4];
		int rowval;
		cin>>rowval;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>cards[i][j];
			}
		}
		int rowval2;
		cin>>rowval2;
		int cards2[4][4];
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin>>cards2[i][j];
			}
		}
		int flag=0;
		int chu[4];
		int k=0;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if (cards[rowval-1][i]==cards2[rowval2-1][j])
				{
					flag++;
					//cout<<"haha"<<cards[rowval][i];
					chu[k++]=cards[rowval-1][i];    	
				}
			}
		}
		if(flag==1)
		{
			cout<<"Case #"<<blah<<": "<<chu[0]<<endl;
	
		}
		if(flag>1)
		{
			cout<<"Case #"<<blah<<": Bad magician!"<<endl;
		}
		if(flag==0)
		{
			cout<<"Case #"<<blah<<": Volunteer cheated!"<<endl;
		}
		
		blah++;
	}
	
	return 0;
}