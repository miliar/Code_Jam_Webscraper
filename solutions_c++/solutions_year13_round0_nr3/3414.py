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
#include <sstream>
#include <queue>
#include <cmath>
using namespace std;

bool ispall(int a)
{
	stringstream tmp;
	tmp << a;
	string k;
	tmp >> k;
	int n = k.size() / 2;
	for(int i = 0 ; i < n; i ++)
	{
		if(k[i] != k[k.size() - i - 1])
		{
			return false;
		}	
	}
	return true;
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
		int a , b;
		in >> a >> b;
		int num = 0;
		for(int i = a ; i <= b ; i ++)
		{
			if(ispall(i))
			{
				int c = sqrt((double)i);
				if(c * c == i)
				{
					if(ispall(c))
					{
						num ++;
					}
				}
			}
		}
		out << "Case #" << index << ": " << num << endl;
	}
	return 0;
}