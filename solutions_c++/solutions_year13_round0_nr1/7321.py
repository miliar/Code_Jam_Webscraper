// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include<iostream>
#include<sstream>
#include<string>
#include<cstdlib>
#include<vector>
#include<map>
#include<queue>
#include<stack>
#include<cctype>
#include<set>
#include<bitset>
#include<algorithm>
#include<list>
#include<utility>
#include<functional>
#include <deque>
#include <numeric>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <assert.h>
#include<cmath>
#include<math.h>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>



using namespace std;

char a[4][5];

bool CheckWin(char ch)
{
	//check row
	bool ans;
	for(int i=0;i<4;i++)
	{
		ans = true;
		for(int j=0;j<4;j++)
			if(false == (a[i][j]==ch || a[i][j]=='T'))
			{
				ans = false;
				break;
			}
			if(true == ans) return true;
	}




	//check column

	for(int j=0;j<4;j++)
	{
		ans = true;
		for(int i=0;i<4;i++)
			if(false == (a[i][j]==ch || a[i][j]=='T'))
			{
				ans = false;
				break;
			}
			if(true == ans) return true;
	}



	//check diagonal

	ans = true;
	for(int i=0;i<4;i++)
		if(false == (a[i][i]==ch || a[i][i]=='T'))
		{
			ans =false;
			break;
		}

		if(true == ans) return true;

		ans = true;
		for(int i=0,j=3;i<4;i++,j--)
			if(false == (a[i][j]==ch || a[i][j]=='T'))
			{
				ans =false;
				break;
			}


			if(true == ans) return true;

			return false;
}

bool CheckInComplete()
{
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(a[i][j] == '.')
				return true;

	return false;


}



int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-largeout.txt","w",stdout);
	int T;
	cin>>T;

	int n = 0;
	while(T--)
	{

		for(int i=0;i<4;i++)
			cin>>a[i];

		cout<<"Case #"<<++n<<": ";

		if(true == CheckWin('X'))
			cout<<"X won"<<endl;
		else if(true == CheckWin('O'))
			cout<<"O won"<<endl;
		else if(true == CheckInComplete())
			cout<<"Game has not completed"<<endl;
		else
			cout<<"Draw"<<endl;
	}


	return 0;
}


