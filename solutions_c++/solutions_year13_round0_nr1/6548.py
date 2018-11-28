#include<cstdio>
#include<iostream>
#include<cassert>
#include<cctype>
#include<cfloat>
#include<climits>
#include<cstring>
#include<bitset>
#include<deque>
#include<map>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
int ar[5][5];
int main()
{
	int t,i,j,k,tempo,tempx,countd,flag;
	string str;
	k=0;
	scanf("%d",&t);
	while(t--)
	{
		k++;

		flag=0;
		countd=0;
		for(i=0;i<4;i++)
		{
			cin>>str;
			for(j=0;j<4;j++)
			{
				if(str[j]=='.')
				{
					ar[i][j]=0;
					countd++;
				}
				else if(str[j]=='X')
					ar[i][j]=1;
				else if(str[j]=='O')
					ar[i][j]=2;
				else if(str[j]=='T')
					ar[i][j]=3;
			}
		}
		for(i=0;i<4;i++)
		{
			tempx=0;
			tempo=0;
			for(j=0;j<4;j++)
			{
				if(ar[i][j]==1||ar[i][j]==3)
				{
					tempx++;
				}
				if(ar[i][j]==2||ar[i][j]==3)
				{
					tempo++;
				}
			}
			if(tempo==4)
			{
				//cout<<"length for"<<endl;
				flag=2;
				break;
			}
			else if(tempx==4)
			{
				//cout<<"length for"<<endl;
				flag=1;
				break;
			}
		}
		if(flag==0)
		{
			for(j=0;j<4;j++)
			{
				tempx=0;
				tempo=0;
				for(i=0;i<4;i++)
				{
					if(ar[i][j]==1||ar[i][j]==3)
					{
						tempx++;
					}
					if(ar[i][j]==2||ar[i][j]==3)
					{
						tempo++;
					}
				}
				if(tempo==4)
				{
					//cout<<"height for"<<endl;
					flag=2;
					break;
				}
				else if(tempx==4)
				{
					//cout<<"height for"<<endl;
					flag=1;
					break;
				}
			}
		}
		if(flag==0)
		{
			//cout<<"inside else"<<endl;
			if(((ar[0][0]==1||ar[0][0]==3)&&(ar[1][1]==1||ar[1][1]==3)&&(ar[2][2]==1||ar[2][2]==3)&&(ar[3][3]==1||ar[3][3]==3))||((ar[0][3]==1||ar[0][3]==3)&&(ar[1][2]==1||ar[1][2]==3)&&(ar[2][1]==1||ar[2][1]==3)&&(ar[3][0]==1||ar[3][0]==3)))
			{
				flag=1;
			}
			else if(((ar[0][0]==2||ar[0][0]==3)&&(ar[1][1]==2||ar[1][1]==3)&&(ar[2][2]==2||ar[2][2]==3)&&(ar[3][3]==2||ar[3][3]==3))||((ar[0][3]==2||ar[0][3]==3)&&(ar[1][2]==2||ar[1][2]==3)&&(ar[2][1]==2||ar[2][1]==3)&&(ar[3][0]==2||ar[3][0]==3)))
			{
				flag=2;
			}
		}
		if(flag==1)
		{
			printf("Case #%d: X won\n",k);
		}
		else if(flag==2)
		{
			printf("Case #%d: O won\n",k);
		}
		else if(flag==0&&countd==0)
		{
			printf("Case #%d: Draw\n",k);
		}
		else if(flag==0&&countd!=0)
		{
			printf("Case #%d: Game has not completed\n",k);
		}
	}



	return 0;
}
