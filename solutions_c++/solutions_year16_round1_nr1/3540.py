/*    SHUBHAM SINHA    */



#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <deque>
#include <list>
#include <math.h>

#define ll long long int
#define maxN 100000
#define maxVal 100000000
#define minVal -100000000
#define mod 1000000007LL

#define gcd(a,b) __gcd(a,b)

using namespace std;

char a[maxN+5];
deque<char> q;
deque<char>::iterator it;

int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef LOCAL_SYS
        freopen("A-large.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    int t,i,k,tc=1;
    scanf("%d",&t);
    while(t--)
    {
    	scanf("%s",a);
    	k=0;
    	for(i=0;i<(int)strlen(a);i++)
    	{
    		if(i==0)
    			q.push_back(a[i]);
    		else
    		{
    			if(a[i]-'A'<(q.front())-'A')
    				q.push_back(a[i]);
    			else
    				q.push_front(a[i]);
    		}
    	}
    	printf("Case #%d: ",tc++);
    	for(it=q.begin();it!=q.end();it++)
    		printf("%c",(*it));
    	while(!q.empty())
    		q.pop_back();
    	printf("\n");
    }
    return 0;
}