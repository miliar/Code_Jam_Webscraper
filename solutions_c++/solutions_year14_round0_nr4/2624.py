/*
 * war.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: prakhar
 */

#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <stdio.h>
#include <vector>
using namespace std;
int main(int a, char** v)
{
	int numCases;
	scanf("%d",&numCases);
	int count;
	for (count = 0; count < numCases; ++count) {
		int num;vector<double> n; vector<double> k;
		scanf("%d",&num);
		double input;int i,j;int war=0, dwar=0;
		for (i = 0; i < num; ++i) {
			scanf("%lf",&input);
			n.push_back(input);
		}
		for (i = 0; i < num; ++i) {
			scanf("%lf",&input);
			k.push_back(input);
		}
		sort(n.begin(),n.end());
		sort(k.begin(),k.end());
		int used[1000];
		int deceptiveused[1000];
		for(i=0; i<num; i++) { used[i] = 0; deceptiveused[i]=0;}
		for(i=0; i<num; i++)
		{
			double w1 = n.at(i);
			double deceptivew1 = k.at(i);
			int worstcaseloc = -1,dworstcaseloc = -1; int flg = 0,dflg=0;
			for(j=0; j<num ;j++)
			{
				double w2 = k.at(j);
				if(used[j] == 0)
				{
					if(w2>w1) {used[j] = 1; flg =1; break;}
					else if(worstcaseloc == -1) worstcaseloc = j;
				}
			}
			if(!flg){ war++; used[worstcaseloc] = 1;}
			for(j=0; j<num ;j++)
			{
				double deceptivew2 = n.at(j);
				if(deceptiveused[j] == 0)
				{
					if(deceptivew2 > deceptivew1){deceptiveused[j]=1; dwar++; dflg=1; break;}
					else if(dworstcaseloc == -1) dworstcaseloc = j;
				}
			}
			if(!dflg){ deceptiveused[dworstcaseloc] = 1; }

		}
		printf("Case #%d: %d %d\n",count+1,dwar,war);
	}
	return 0;
}
