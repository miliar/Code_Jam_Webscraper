#include <vector>
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
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(void)
{
	
	freopen("A-large.in", "r", stdin);
	freopen("A-large-Newout.out","w",stdout);

	int Test,i;
	cin>>Test;
	
	for(int c = 1; c<= Test; c++)
	{	
		cout << "Case #"<<c<<": ";
		
		int smax;
		char ab;
		int arr[1000];
		cin >> smax;

		int stand = 0, f = 0;
		for(i=0;i<=smax;i++)
		{
			cin >> ab;
			arr[i] = ab - '0';
		}

		if(arr[0] == 0)
		{
			f=1;
			arr[0] = 1;
			stand = 1;
		}
		else
			stand = arr[0];

		for(i=1;i<=smax+1;i++)
		{
			if(stand<smax)
			{
				if(arr[i-1] == 0 && arr[i]>0)
				{			
					if((i-stand)>0)
					{
						f = f+i-stand;
						stand = i + arr[i];
					}
					else
						stand = stand + arr[i];
				}
				else
					stand = stand + arr[i];
			}
		}
		cout<<f<<endl;
	}
	return 0;
}