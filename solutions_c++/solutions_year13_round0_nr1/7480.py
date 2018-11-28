#include<iostream>
#include<stdio.h>
#include<string.h>

using namespace std;
int main()
{
        freopen("C:\\A\\in.txt","r",stdin);freopen("C:\\A\\out.txt","w",stdout);


    int t=0;
	scanf("%d",&t);
	int n=0;

	char arr[4][4];
	while(n<t)
	{
		n++;
		//cout<<"came back"<<endl;
		int k=0;
		for(;k<4;k++)
		{
			scanf("%s",arr[k]);
			//cout<<arr[k]<<endl;
		}
		int flag=0;
		int no_of_dot=0;
		for(k=0;k<4;k++)
		{
			if(arr[k][0]!='.')
			{
				if((arr[k][0]=='X'||arr[k][0]=='T') && (arr[k][1]=='X'||arr[k][1]=='T') && (arr[k][2]=='X'||arr[k][2]=='T') && (arr[k][3]=='X'||arr[k][3]=='T'))
				{
					printf("Case #%d: X won\n",n);
					flag=1;
					//break;
				}

				if(flag==0 && (arr[k][0]=='O'||arr[k][0]=='T') && (arr[k][1]=='O'||arr[k][1]=='T') && (arr[k][2]=='O'||arr[k][2]=='T') && (arr[k][3]=='O'||arr[k][3]=='T'))
				{
					printf("Case #%d: O won\n",n);
					flag=1;
					//break;
				}
			}
			if(flag==0 && arr[0][k]!='.')
			{
				if((arr[0][k]=='X'||arr[0][k]=='T') && (arr[1][k]=='X'||arr[1][k]=='T') && (arr[2][k]=='X'||arr[2][k]=='T') && (arr[3][k]=='X'||arr[3][k]=='T'))
				{
					printf("Case #%d: X won\n",n);
					flag=1;
					//break;
				}

				if(flag==0 && (arr[0][k]=='O'||arr[0][k]=='T') && (arr[1][k]=='O'||arr[1][k]=='T') && (arr[2][k]=='O'||arr[2][k]=='T') && (arr[3][k]=='O'||arr[3][k]=='T'))
				{
					printf("Case #%d: O won\n",n);
					flag=1;
					//break;
				}
			}
			else if(flag==0)
				{
					int faltu=0;
					for(;faltu<4;faltu++)
						if(arr[k][faltu]=='.')
							no_of_dot++;
				}
			else if(flag==1)
				{k=4;}
		}
		if(flag==0)
		{
			if(arr[0][0]!='.')
			{
				if((arr[0][0]=='X'||arr[0][0]=='T') && (arr[1][1]=='X'||arr[1][1]=='T') && (arr[2][2]=='X'||arr[2][2]=='T') && (arr[3][3]=='X'||arr[3][3]=='T'))
				{
					printf("Case #%d: X won\n",n);
					flag=1;
				}

				else if((arr[0][0]=='O'||arr[0][0]=='T') && (arr[1][1]=='O'||arr[1][1]=='T') && (arr[2][2]=='O'||arr[2][2]=='T') && (arr[3][3]=='O'||arr[3][3]=='T'))
				{
					printf("Case #%d: O won\n",n);
					flag=1;
				}
			}

			else if(flag==0 && arr[0][3]!='.')
			{
				if((arr[0][3]=='X'||arr[0][3]=='T') && (arr[1][2]=='X'||arr[1][2]=='T') && (arr[2][1]=='X'||arr[2][1]=='T') && (arr[3][0]=='X'||arr[3][0]=='T'))
				{
					printf("Case #%d: X won\n",n);
					flag=1;
				}

				else if((arr[0][3]=='O'||arr[0][3]=='T') && (arr[1][2]=='O'||arr[1][2]=='T') && (arr[2][1]=='O'||arr[2][1]=='T') && (arr[3][0]=='O'||arr[3][0]=='T'))
				{
					printf("Case #%d: O won\n",n);
					flag=1;
				}
			}
		}

		if(flag==0)
		{
			if(no_of_dot==0)
				printf("Case #%d: Draw\n",n);
			else if(no_of_dot>0)
				printf("Case #%d: Game has not completed\n",n);
		}
	}
	return 0;
}
