#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int whowon(int arr[4][4])
{
	int sum1,sum2;
	
	//checking rows and columns
	for(int i=0;i<4;i++){
		sum1=sum2=0;
		for(int j=0;j<4;j++)
		{
			sum1+=arr[i][j];
			sum2+=arr[j][i];
		}
		if(sum1==4 || sum1==103 || sum2==4 || sum2==103)
			return 0;
		if(sum1==0 || sum1==100 || sum2==0 || sum2==100)
			return 1;
	}
	
	//checking diagonals
	sum1 = arr[0][0]+arr[1][1]+arr[2][2]+arr[3][3];
	sum2 = arr[0][3]+arr[1][2]+arr[2][1]+arr[3][0];
	if(sum1==4 || sum1==103 || sum2==4 || sum2==103)
			return 0;
	if(sum1==0 || sum1==100 || sum2==0 || sum2==100)
			return 1;
	return 2;

}

inline bool solve(char temp[])
{
	for(int i=0;i<4;i++)
		if(temp[i]=='.')	return 1;
	return 0;
}	

int main()
{
 freopen("A-small-attempt0.in","r",stdin);
	 freopen("out.txt","w",stdout);
	int T,arr[4][4];
	char temp[5];
	scanf("%d",&T);

	for(int t=1;t<=T;t++){
		gets(temp);
		bool dotfound=false;
		for(int i=0;i<4;i++)
		{
			gets(temp);
			if(!dotfound)	dotfound = solve(temp);
			for(int j=0;j<4;j++)
				if(temp[j]=='X')
					arr[i][j]=1;
				else if(temp[j]=='O')
					arr[i][j]=0;
				else if(temp[j]=='T')	arr[i][j]=100;
				else arr[i][j]=-100;
		}
			
			int c = whowon(arr);
			if(c==0)
				printf("Case #%d: X won\n",t);
			else if(c==1)
				printf("Case #%d: O won\n",t);
			else {
				if(dotfound)
				printf("Case #%d: Game has not completed\n",t);
				else
				printf("Case #%d: Draw\n",t);

			}
	}
}
