#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <climits>
#include <ctime>

#define pb       	push_back
#define fi       	first
#define se       	second
#define inf		 	1000000000
#define SET(A,b) memset(A,b,sizeof (A) )
#define SIZE(A) ((int)(A).size())
#define yeral() (node *)calloc(1,sizeof(node))
#define dbg(x) cerr<<#x<<":"<<x<<endl

using namespace std;

typedef long long int lint;
typedef pair<int,int> ii;

int T,size;
char str[105];
int main()
{
	//int steps = 0;
	freopen("oku.txt","r",stdin);
	freopen("yaz.txt","w",stdout);
	
	scanf("%d",&T);
	for(int tt = 1;tt<=T;tt++){
		scanf(" %s",str);
		size = strlen(str);
		int count = 0;
		char last = '*';
		for(int i = 0;i<size;i++){
			if(str[i] != last){
				last = str[i];
				count++;
			}
		}
		if(last == '+')
			count--;
		printf("Case #%d: %d\n",tt,count);
	}
	
}
