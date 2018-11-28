#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int main()
{
freopen("magic.in","r",stdin);
freopen("magicout.txt","w",stdout);
int test,ans1,ans2,card1[4][4],card2[4][4],c=0,a=1,no;
cin>>test;
while(test--)
{
	c=0;
	no=0;
	cin>>ans1;
	for(int x=0;x<4;x++)
	for(int i=0;i<4;i++)
	cin>>card1[x][i];
	cin>>ans2;
	for(int x=0;x<4;x++)
	for(int i=0;i<4;i++)
	cin>>card2[x][i];
	for(int x=0;x<4;x++)
	{
		for(int i=0;i<4;i++)
		{
			
			if(card1[ans1-1][x]==card2[ans2-1][i])
			{
				c=c+1;
				no=card1[ans1-1][x];
				}			
			}
		}
	if(c==1)
	{
		cout<<"Case #"<<a<<": "<<no<<endl;
		}
	else if(c>1)
	{
		cout<<"Case #"<<a<<": "<<"Bad magician!"<<endl;
		}
	else
	{
		cout<<"Case #"<<a<<": "<<"Volunteer cheated!"<<endl;
		}
	a=a+1;
}

return 0;	
}
