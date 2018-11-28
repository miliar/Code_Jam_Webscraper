#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int T;
	cin>>T;
	while(T--)
	{
		int a,card1[4][4];
		cin>>a;
		for (int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>card1[i][j];
		}
		sort(card1[a-1],card1[a-1]+4);
		int b,card2[4][4],c=0,k;
		cin>>b;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			cin>>card2[i][j];
		}
		sort(card2[b-1],card2[b-1]+4);
		for(int i=0,j=0;i<4&&j<4;)
		{
			if(card1[a-1][i]>card2[b-1][j])
			j++;
			else if(card1[a-1][i]<card2[b-1][j])
			i++;
			else
			{c++;k=i;i++;j++;}
		}
		if(c==1)
		cout<<card1[a-1][k]<<endl;
		else if(c>1)
		cout<<"Bad magician!"<<endl;
		else
		cout<<"Volunteer cheated!"<<endl;
	}
	// your code goes here
	return 0;
}
