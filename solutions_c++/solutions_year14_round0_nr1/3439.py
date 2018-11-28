#include <iostream>
#include <iomanip>
#include <cstdio>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <utility>
#include <fstream>
using namespace std;
int main()
{
	std::iostream::sync_with_stdio(false);
	int s=1;
	ofstream myfile;
	 myfile.open ("example.txt");
	 ifstream infile;
	 infile.open("A-small-attempt1.in");
	int t;
	infile>>t;
	while(t--)
	{
		int p;
		infile>>p;
		std::vector<int> v1(17,0);
		int i,j;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				int b;
				infile>>b;
				if(i==p-1)
					v1[b]++;
			}
		}
		int q;
		infile>>q;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				int b;
				infile>>b;
				if(i==q-1)
					v1[b]++;
			}
		}
		int count=0;
		for(i=1;i<17;i++)
		{
			if(v1[i]>1)
				count++;
		}
		if(count==0)
			myfile<<"Case #"<<s<<": Volunteer cheated!"<<endl;
		else if(count>1)
			myfile<<"Case #"<<s<<": Bad magician!"<<endl;
		else
		{
			for(i=1;i<17;i++)
				if(v1[i]==2)
					break;
			myfile<<"Case #"<<s<<": "<<i<<endl;
		}
		s++;
	}
	infile.close();
	myfile.close();
	return 0;
}