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

lint last;

int f(lint x){
	int mark = 0;
	int ar[10];
	last = x;
	for(int i = 0;i < 10 ;i++)
		ar[i] = 0;
	while(x)
	{
		ar[x%10] = 1;
		x = x/10;
	}
	for(int i = 0;i < 10 ;i++)
		if(ar[i])
			mark |=  (1 << i);
	
	return mark;	
}

int main()
{
	int N,x;
	//int steps = 0;
	freopen("oku.txt","r",stdin);
	freopen("yaz.txt","w",stdout);
	
	scanf("%d",&N);
	for(int i =0;i<N;i++){
		scanf("%d",&x);
		if(x == 0){
			printf("Case #%d: INSOMNIA\n",i+1);
			continue;
		}
		int mark = 0;
		lint sum = x;
		
		while(mark != 1023){
			mark |= f(sum);
			sum += x;
	//		steps++;
		//	dbg(mark);
		}
		printf("Case #%d: %d\n",i+1,last);
	}
	
	
}
