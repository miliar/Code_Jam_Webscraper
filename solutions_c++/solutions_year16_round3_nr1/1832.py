/*    SHUBHAM SINHA    */
 
 
 
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <math.h>
 
#define ll unsigned long long
#define maxN 30
#define maxVal 100000000
#define minVal -100000000
#define mod 1000000007LL
 
#define gcd(a,b) __gcd(a,b)
 
using namespace std;
 
int p[maxN+5];
set<pair<int,int> > s;
set<pair<int,int> >::reverse_iterator it1,it2;

int main()
{
    #ifndef ONLINE_JUDGE
    	freopen("A-large.in","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif
	int t,n,i,j,p1,q1,p2,q2;
	scanf("%d",&t);
	for(j=1;j<=t;j++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&p[i]);
			if(p[i]!=0)
				s.insert(make_pair(p[i],i));
		}
		printf("Case #%d: ",j);
		while(!s.empty())
		{
			it1=s.rbegin();
			p1=(*it1).first;
			q1=(*it1).second;
			s.erase(s.find(make_pair(p1,q1)));
			if(s.empty())
			{
				if(p1>=2)
				{
					printf("%c%c ",(char)(q1+'A'),(char)(q1+'A'));
					if(p1-2>0)
						s.insert(make_pair(p1-2,q1));
				}
				else if(p1==1)
				{
					printf("%c ",(char)(q1+'A'));
					if(p1-1>0)
						s.insert(make_pair(p1-1,q1));
				}
				continue;
			}
			it2=s.rbegin();
			p2=(*it2).first;
			q2=(*it2).second;
			if((p1-p2)>=2)
			{
				//remove both from p1
				printf("%c%c ",(char)(q1+'A'),(char)(q1+'A'));
				if(p1-1>0)
					s.insert(make_pair(p1-2,q1));
			}
			else if((p1-p2)>=1)
			{
				//remove only from p1
				printf("%c ",(char)(q1+'A'));
				if(p1-1>0)
					s.insert(make_pair(p1-1,q1));
			}
			else
			{
				s.erase(s.find(make_pair(p2,q2)));
				if(p1==1&&p2==1)
				{
					if(s.empty())
					{
						//remove both
						printf("%c%c ",(char)(q1+'A'),(char)(q2+'A'));
					}
					else
					{
						//remove only 1
						printf("%c ",(char)(q1+'A'));
						s.insert(make_pair(p2,q2));
					}
					continue;
				}
				//remove 1 from both p1,q1
				printf("%c%c ",(char)(q1+'A'),(char)(q2+'A'));
				if(p1-1>0)
					s.insert(make_pair(p1-1,q1));
				if(p2-1>0)
					s.insert(make_pair(p2-1,q2));
			}
		}
		printf("\n");
	}
    return 0;
}