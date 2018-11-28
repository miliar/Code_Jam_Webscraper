#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<cmath>
#include<string>
#define M 10000007;

#define input(a) scanf("%d",&a);
#define print(a) printf("%d",a);

using namespace std;

int main()
{


freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);

int t=0;
cin>>t;
int q=0;
while(q++<t)
{
	//cout<<"I n L";
char sq[4][4]={'.'};
int flag=0;

for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	{	cin>>sq[i][j];
	
			if(sq[i][j]=='.')
				flag=4;
		}

for(int i=0;i<4;i++)
{
	if(((sq[i][0]=='X')||(sq[i][0]=='T'))&&((sq[i][1]=='X')||(sq[i][1]=='T'))&&((sq[i][2]=='X')||(sq[i][2]=='T'))&&((sq[i][3]=='X')||(sq[i][3]=='T')))

			{  // cout<<"in flag";
				flag=1;
			}
			}


for(int i=0;i<4;i++)
{
	if(((sq[0][i]=='X')||(sq[0][i]=='T'))&&((sq[1][i]=='X')||(sq[1][i]=='T'))&&((sq[2][i]=='X')||(sq[2][i]=='T'))&&((sq[3][i]=='X')||(sq[3][i]=='T')))
			flag=2;
			}



for(int i=0;i<4;i++)
{
	if(((sq[i][0]=='O')||(sq[i][0]=='T'))&&((sq[i][1]=='O')||(sq[i][1]=='T'))&&((sq[i][2]=='O')||(sq[i][2]=='T'))&&((sq[i][3]=='O')||(sq[i][3]=='T')))

			{  // cout<<"in flag";

				flag=5;
			}
			}




for(int i=0;i<4;i++)
{
	if(((sq[0][i]=='O')||(sq[0][i]=='T'))&&((sq[1][i]=='O')||(sq[1][i]=='T'))&&((sq[2][i]=='O')||(sq[2][i]=='T'))&&((sq[3][i]=='O')||(sq[3][i]=='T')))
			{

				flag=6;
		}
			}


if(flag==0)
{

for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	{
		if(sq[i][j]=='.')
			{   flag=3;

				}
		}
		
		if(flag==0)
		flag=3;
}


if(((sq[0][0]=='O')||(sq[0][0]=='T'))&&((sq[1][1]=='O')||(sq[1][1]=='T'))&&((sq[2][2]=='O')||(sq[2][2]=='T'))&&((sq[3][3]=='O')||(sq[3][3]=='T')))
			{

				flag=7;
		}

if(((sq[0][3]=='O')||(sq[0][3]=='T'))&&((sq[1][2]=='O')||(sq[1][2]=='T'))&&((sq[2][1]=='O')||(sq[2][1]=='T'))&&((sq[3][0]=='O')||(sq[3][0]=='T')))
			{

				flag=7;
		}


if(((sq[0][0]=='X')||(sq[0][0]=='T'))&&((sq[1][1]=='X')||(sq[1][1]=='T'))&&((sq[2][2]=='X')||(sq[2][2]=='T'))&&((sq[3][3]=='X')||(sq[3][3]=='T')))
			{

				flag=8;
		}

if(((sq[0][3]=='X')||(sq[0][3]=='T'))&&((sq[1][2]=='X')||(sq[1][2]=='T'))&&((sq[2][1]=='X')||(sq[2][1]=='T'))&&((sq[3][0]=='X')||(sq[3][0]=='T')))
			{

				flag=8;
		}




cout<<"Case #"<<q<<": ";


if(flag==1)
{
cout<<"X won"<<endl;
}
if((flag==2)||(flag==8))
{

cout<<"X won"<<endl;
}if(flag==3)
{

cout<<"Draw"<<endl;
}
if((flag==5)||(flag==6)||(flag==7))
{
	cout<<"O won"<<endl;
}
if(flag==4)
{
cout<<"Game has not completed"<<endl;
}





}



}


