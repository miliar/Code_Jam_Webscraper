#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>

using namespace std;

int card;
int f_card[4];
int s_card[4];

int main()
{
	int T,count,same,num;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int row;
		same=0;
		for(int j=0;j<2;j++)
		{
			count=0;
			cin>>row;
			for(int k=1;k<=16;k++)
			{
				cin>>card;
				if(k>=(row-1)*4+1&&k<=row*4) 
				{
					if(j==0) f_card[count]=card;
					if(j==1)
					{
						for(int x=0;x<4;x++)
							if(card==f_card[x])
							{ same++;  num=f_card[x]; } 
					}
					count++;
				}
			}
		}
		//for(int x=0;x<4;x++) cout<<f_card[x]<<"\n";
		cout<<"Case #"<<i+1<<": ";
		if(same==1) cout<<num<<"\n";
		else if(same>1) cout<<"Bad magician!\n";
		else cout<<"Volunteer cheated!\n";
	}
}