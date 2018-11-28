#include<iostream>
#include<vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string>
#include <queue>
#include <sstream>
#include <iostream>
#include<string.h>
#include <iomanip>
#include <cstdio>
#include<math.h>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define ull unsigned long long 
#define pi 3.141592653589793
#define ARRAY_SIZE(A) sizeof(A)/sizeof(A[0])
#define PB push_back
#define INF 1<<30
using namespace std;
int main()
{
	int n =0;
	cin>>n;
	int tt =1;
	while(n--)
	{
		int x =0;
		cin>>x;
		int arr[4][4];
		for(int i =0;i<4;i++)
		for(int j =0;j<4;j++)
		scanf("%d",&arr[i][j]);
		int ans[4];
		for(int i =0;i<4;i++)
		{
			ans[i] = arr[x-1][i];
		}
		
		int y =0;
		cin>>y;
		int brr[4][4];
		for(int i =0;i<4;i++)
		for(int j =0;j<4;j++)
		scanf("%d",&brr[i][j]);
		int val[4];
		for(int i =0;i<4;i++)
		{
			val[i] = brr[y-1][i];
		}
		
		int count  =0;
		int f =0;
		for(int i =0;i<4;i++)
		{
			for(int j =0;j<4;j++)
			{
				if(val[i] == ans[j])
				{count++;f =val[i];}
			}
		}
		cout<<"Case #"<<tt++<<": ";
		if(count>1)
		{
			cout<<"Bad magician!"<<endl;
		}
		else if(count == 1)
		cout<<f<<endl;
		else
		cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}