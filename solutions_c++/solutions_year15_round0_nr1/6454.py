


#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <iostream>

#include <algorithm>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define EPS 0.000000001
#define INF 1000000000

int n;



int main() {
	
	int T;
	cin>>T;
	int n;
	string s;
	
	int caseNum=0;
	
	
	while (T-->0)
	{
		cin>>n>>s;
		
		int pos=0;
		int extra=0;
		int level=0;
		
		for (int i=0;i<n;i++)
		{
			pos=s[i]-'0';
			
			if (level+extra<i)
			{
				extra+=i-level-extra;
			}
			
			level+=pos;
		}
		
		cout<<"Case #"<<++caseNum<<": "<<extra<<endl;
	}
	
	return 0;
}

