#include <stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>

using namespace std;

int main()
{
	int t1;
	long double time1,c,f,x,ActualRate;
	//freopen("myfile.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
	bool flag=true;
	scanf("%d",&t1);
	int i=1;
	while(t1--)
	{
		time1=0;
		flag=true;
		ActualRate=2;
		scanf("%Lf %Lf %Lf",&c,&f,&x);
		while(flag)
		{
			long double temp= x/ActualRate;
			if( temp < (c/ActualRate + x/(ActualRate+f)))
			{
				flag=false;
				time1 += temp ;
			}
			else
			{
				time1 += c/ActualRate;
				ActualRate += f;
			}
		}
		printf("Case #%d: %Lf\n",i,time1);
		i++;
	}
	return 0;
}
