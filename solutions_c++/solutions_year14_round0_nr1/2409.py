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
#include <cstring>
#include <string>
#include <queue>
#include <cstdio>
#include <fstream>

using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open ("input.txt");
	fout.open ("output.txt");
	int t=0;
	fin>>t;
	for (int i=0;i<t ; i ++)
	{
		int q1=0, q2=0;
		fin>>q1;
		int arr[4][4];
		int tarr1[4];
		for(int h=0;h<4;h++)
		{
			for(int k=0;k<4;k++) {
				fin>>arr[h][k];
				if (h==q1-1)
					tarr1[k]=arr[h][k]; }
		}

		fin>>q2;

		int tarr2[4];
		for(int h=0;h<4;h++)
		{
			for(int k=0;k<4;k++) {
				fin>>arr[h][k];
				if (h==q2-1)
					tarr2[k]=arr[h][k]; }
		}
		int count =0, index=0;
		for (int l=0;l<4;l++)
		{
			for (int k=0;k<4;k++)
			if(tarr1[l]==tarr2[k]){
				count++;  index=tarr1[l]; }
		}
		if(count==0)
			fout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		else if (count==1)
			fout<<"Case #"<<i+1<<": "<<index<<endl;
		else 
			fout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;

	}
	fin.close();
	fout.close();
}
