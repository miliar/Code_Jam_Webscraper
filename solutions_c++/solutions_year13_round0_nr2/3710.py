#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <map>
#include <cstdlib>
#include <vector>
#include <iterator>
#include <fstream>
#include <list>
#include <queue>
using namespace std;

bool max(int a[][102] , int i , int j , int m , int n)
{
	int maxrow = 0 , maxco = 0;
	for(int k = 1 ; k <= m ; k ++ )
	{
		if(a[k][j] >= maxrow)
			maxrow = a[k][j]; 
	}
	for(int k = 1 ; k <= n ; k ++)
	{
		if(a[i][k] >= maxco)
			maxco = a[i][k];
	}
	if(a[i][j] == maxrow || a[i][j] == maxco)
		return true;
	else
		return false;
}

int main()
{
	ifstream in("1.in");
	ofstream out("ans.out");
	int casen , index = 0;
	in >> casen;
	while(index < casen)
	{
		index ++;
		int a[102][102] , m , n;
		memset(a , 0 , sizeof(a));
		in >> m >> n;
		bool can = true;
		for(int i = 1 ; i <= m ; i ++)
		{
			for(int j = 1 ; j <= n ; j ++)
			{
				in >> a[i][j];
			}
		}
		for(int i = 1 ;i <= m ; i ++)
		{
			for(int j = 1 ; j <= n ; j ++)
			{
				if(max(a , i , j , m , n))
				{
					can = true;
				}
				else
				{
					can = false;
					break;
				}
			}
			if(!can)
			{
				break;
			}
		}
		if(can)
		{
			out << "Case #" << index << ": YES" << endl; 
		}
		else
		{
			out << "Case #" << index << ": NO" << endl; 
		}

	}
	return 0;
}