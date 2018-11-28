//Nakul Krishnan
//Computer Science Engineering
//Amrita Vishwa Vidyapeetham

//Try to be a problem solver rather than a coder
//I do this with the best intentions to improve my problem solving skills and learn new things
//Here is the default template of my new .cpp file

#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <climits>
#include <algorithm>
#include <sstream>
#include <queue>
#include <stack>

#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

#define PB push_back
#define MP make_pair
#define INF (int)1e9
#define LL long long
#define EPS (double)1e-6
#define PI acos(-1.0)
#define SZ(a) (int)(a).size()
#define ALL(a) (a).begin(),(a).end()
#define DEB if(1)
#define VI vector<int>
#define PII pair<int,int>
#define FILL(a,b) memset((a),(b),sizeof((a)))

using namespace std;

LL mod=INF+7;

int main()
{
	int tc=1,tests;
	scanf("%d",&tests);
	while(tc<=tests)
	{
		int first_ans,second_ans,ret=0,ans=0;
		map<int,int> cnt;
		scanf("%d",&first_ans);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			{
				int temp;
				scanf("%d",&temp);
				if(i==first_ans)
					cnt[temp]++;
			}
		scanf("%d",&second_ans);
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
			{
				int temp;
				scanf("%d",&temp);
				if(i==second_ans)
					cnt[temp]++;
			}
		for(map<int,int> :: iterator it=cnt.begin(); it!=cnt.end(); it++)
			if(it->second==2)
				ret++,ans=it->first;
		printf("Case #%d: ",tc);
		if(ret==1)
			printf("%d",ans);
		else if(ret==0)
			printf("Volunteer cheated!");
		else
			printf("Bad magician!");
		printf("\n");
		tc++;
	}
    scanf("\n");
    return 0;
}

//Nakul © Copyright 2012 - All Rights Reserved ( Last modified on 25th March 2014 )
