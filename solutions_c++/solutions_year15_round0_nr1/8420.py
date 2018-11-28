#include <iostream>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <vector>
#include <fstream>
using namespace std;

#define FOR(i,a,b)		for(int i=a;i<b;i++)
#define MST(a,b)		memset(a,b,sizeof(a))
#define SCF(a)			scanf("%d",&a)
#define SCF2(a,b)		scanf("%d %d",&a,&b)
#define INF				1<<29

int main()
{
	ifstream infile;
	infile.open("inputa.in");
	ofstream outfile;
	outfile.open("outputa.txt");
	int T;
	infile>>T;
	for(int kase=1;kase<=T;kase++)
	{
		int need=0,sum;
		int n;
		infile>>n;
		char b[1005];
		infile.getline(b,1005);
		sum = b[1]-'0';
		for(int i=2;i<=n+1;i++)
		{
			if(sum < i-1)
			{
				int t = (i-1-sum);
				need += t;
				sum += t;
			}
			sum += b[i]-'0';
		}
		outfile<<"Case #"<<kase<<": "<<need<<endl;
	}
	infile.close();
	outfile.close();
	return 0;
}
