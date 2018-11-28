
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
#include <stdlib.h>
#include <cstring>
#include <sstream>
using namespace std;

#define N 1000000007

int ans = 100;
int tmpans = 0;
int absorb(int i , vector<int> &a , int &mote )
{
	for( ; i < a.size() ; i ++)
	{
		if(a[i] < mote)
			{
				mote += a[i];
			}
			else
			{
				break;
			}
	}
	return i;
}

void find(int i , vector<int> &a , int mote)
{
	i = absorb(i , a , mote);
	if(tmpans > a.size())
	{
		return ;
	}
	if(i == a.size())
	{
		if(tmpans < ans)
		{
			ans = tmpans;
		}
	}
	else
	{
		//+
		tmpans ++;
		int k = mote - 1;
		mote += k;
		find(i , a , mote);
		tmpans --;
		mote -= k;
		//-
		tmpans ++;
		i ++;
		find(i , a , mote);
		tmpans --;
		i --;
	}
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
		int mote ,n;
		in >> mote >> n;
		vector<int> a , b;
		ans = 100;
		tmpans = 0;
		for(int i = 0 ; i < n ; i ++)
		{
			int tmp;
			in >> tmp;
			a.push_back(tmp);
		}
		sort(a.begin() , a.end());
		int i = 0;
		find(i , a  , mote);
		out << "Case #" << index << ": " << ans << endl;
	}
	return 0;
}