#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <math.h>
#include <utility>
#include <sstream>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctime>
#include <limits.h>
#include <bitset>
#include <functional>
#include <numeric>
#include <complex>
#include <fstream>
#define DELIM   '\0'

using namespace std;

int main()
{
	ifstream read ("A-small-practice.in");
	int t;
	read>>t;
	ofstream myfile;
    myfile.open ("A-small-practice.out");
    for(int j=1;j<=t;j++)
	{
		int n,p;
		read>>n;
		int *mask=new int[17];
		memset(mask,0,17*sizeof(int));
		int c,count=0,num;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(i+1!=n)
				{
					read>>c;
				}
				else
				{
					read>>c;
					mask[c]=1;
				}
			}
		}

		read>>p;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				if(i+1!=p)
				{
					int c;read>>c;
				}
				else
				{
					read>>c;
					if(mask[c]){count++;num=c;}
				}
			}
		}
		myfile<<"Case #"<<j<<": ";
		if(count>1)
			myfile<<"Bad magician!";
		else if(count ==1)
			myfile<<num;
		else
			myfile<<"Volunteer cheated!";
		myfile<<endl;
	}


	}
