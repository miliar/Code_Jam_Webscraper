#include<iostream>
#include<stdio.h>
using namespace std;
#define MAX 4

int main()
{
	int arrange1[MAX],arrange2[MAX];
	int tc,choice,number,magicnumber,flag;
	cin>>tc;
	for(int i=0;i<tc;i++)
	{
		for(int rounds=0;rounds<2;rounds++)
		{
				cin>>choice;
				for(int j=0;j<MAX;j++)
				{
					for(int k=0;k<MAX;k++)
					{
						cin>>number;
						if((choice-1) == j)
						{
							if(rounds == 0)
							{
								arrange1[k]=number;
								
							}else
							{
								arrange2[k]=number;
							}
							//cout<<number<<" ";
						}
					}
				}
				//cout<<endl;
		}
		magicnumber = -1;
		for(int x=0;x<MAX && (magicnumber!=0);x++)
		{
			flag = 0;
			for(int y=0;y<MAX &&  (flag==0);y++)
			{
				if(arrange1[x] == arrange2[y])
				{
					if(magicnumber ==-1)
						magicnumber = arrange1[x];
					else
						magicnumber = 0;
					flag = 1;
					//cout<<x<<" "<<y<<endl;
				}
			}
		}
		if(i!=0)
			cout<<endl;
		cout<<"Case #"<<i+1<<": ";
		if(magicnumber == -1)
			cout<<"Volunteer cheated!";
		else
			if(magicnumber == 0)
				cout<<"Bad magician!";
			else
				cout<<magicnumber;
	}
	return 0;
}