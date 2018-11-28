/*
 * 1BA.cpp
 *
 *  Created on: May 3, 2014
 *      Author: Ganesh
 */

#include <gmp.h>
#include <gmpxx.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <functional>
#include <bitset>
#include <cstdio>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstring>


#define MAX 100
#define iter(i,lim) for(long long i=0; i<lim ; i++)

using namespace std;

int main()
{
	long long cases;
	cin>>cases;
	for(long long q=0 ; q<cases ; q++)
	{
		int N;
		cin>>N;
		vector<string> strings;
		long long data[100][100];
		long long count1[100] , count2[100], mini[100], maxi[100];
		string s[100];
		int avg[100];

		strings.resize(N);
		iter(i, N)
			cin>>strings[i];
		iter(i, 100)
		{
			avg[i] = 0;
			count1[i] = 0;
			count2[i] = 0;
			mini[i] = 100000;
			maxi[i] = 0;
		}
		iter(i, N)
		{
			for(int j=0 ; j<strings[i].length() ; j++)
			{
				data[i][j] = 0;
			}
		}

		iter(i, N)
		{
			int index = 0;
			for(int j=0 ; j<strings[i].length() ; j++)
			{
				s[i] = s[i]  + strings[i][j];
				data[i][index] = 1;
				while((j != strings[i].length()) && (strings[i][j] == strings[i][j+1]))
				{
					data[i][index]++;
					j++;
				}
				mini[index] = min(mini[index], data[i][index]);
				maxi[index] = max(maxi[index], data[i][index]);
				index++;
			}
		}
		bool felgawon = false;
		for(int i=0 ; i<N ; i++)
		{
			if(s[i].compare(s[0]) != 0)
			{
				felgawon = true;
				break;
			}
		}
		cout<<"Case #"<<q+1<<": ";

		if(felgawon)
		{
			cout<<"Fegla Won\n";
		}
		else
		{
			iter(i, N)
			{
				for(int j=0 ; data[i][j]!=0 ; j++)
				{
					avg[i] += data[i][j];
				}
			}
			iter(i, s[0].length())
				avg[i]/=N;

			iter(i, N)
			{
				for(int j=0 ; data[i][j]!=0 ; j++)
				{
					count1[j]+= abs(avg[j] - data[i][j]);
				}
			}
			iter(i, s[0].length())
			{
				avg[i]++;
			}
			long long count = 0;
			iter(i, s[0].length())
			{
				int min_val = 100000;
				for(int k=mini[i] ; k<=maxi[i] ; k++)
				{
					int curr = 0;
					for(int j=0 ; j<N ; j++)
					{
						curr += abs(k - data[j][i]);
					}
					min_val = min(min_val, curr);
				}
				count+=min_val;
				//cout<<min_val<<" ";
			}
		/*	iter(i, N)
			{
				for(int j=0 ; data[i][j]!=0 ; j++)
				{
					count2[j]+= abs(avg[j] - data[i][j]);
				}
			}
			for(int i=0 ; i<s[0].length() ; i++)
				count+=min(count1[i], count2[i]);


				*/
			cout<<count<<"\n";
		}


	}
	return 0;
}
