#include<stdio.h>
#include<vector>
#include<map>
#include<algorithm>
#include<iomanip>
#include<math.h>
#include<stdlib.h>
#include<string.h>
using namespace std;
#define iterate(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define size 2100
 int findchar(char str[size],char ch);
int main()
{
	int t;
	scanf("%d",&t);
	char ans[100][size];
	for(int k=0;k<t;k++)
	{
		int arr[10];
		memset(arr,0,sizeof(arr));
		char str[size];
		scanf("%s",str);
		arr[0]=findchar(str,'Z');
		arr[2]=findchar(str,'W');
		arr[4]=findchar(str,'U');
		arr[6]=findchar(str,'X');
		arr[8]=findchar(str,'G');
		arr[1]=findchar(str,'O')-arr[0]-arr[2]-arr[4];
		arr[3]=findchar(str,'T')-arr[2]-arr[8];
		arr[5]=findchar(str,'F')-arr[4];
		arr[7]=findchar(str,'S')-arr[6];
		arr[9]=findchar(str,'I')-arr[6]-arr[5]-arr[8];
		int l=0;
		for(int i=0;i<10;i++)
		{
			for(int j=0;j<arr[i];j++)
			{
				ans[k][l]=i+48;
				l++;
			}
		}
	}
	for(int i=0;i<t;i++)
	{
		printf("Case #%d: %s\n",i+1,ans[i]);
	}
	return 0;
}
int findchar(char str[size],char ch)
{
	int cnt=0;
	for(int i=0;i<strlen(str);i++)
	{
		if(ch==str[i])
			cnt++;
	}
	return cnt;
}
