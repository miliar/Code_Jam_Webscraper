#include <iostream>
#include <math.h>
#include <algorithm>
#include <string>
#include <cstdio>

#define SC(x) scanf("%d", &x);
#define File freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

using namespace std;
const long long inf =2147483647;
const int md=1e9+7;
const double eps=1e-6;
const int mul[8][8]={
{3,2,6,7,0,1,5,4},
{5,3,0,6,1,7,4,2},
{1,7,3,5,2,4,0,6},
{7,6,5,4,3,2,1,0},
{0,1,2,3,4,5,6,7},
{6,0,4,2,5,3,7,1},
{2,4,7,1,6,0,3,5},
{4,5,1,0,7,6,2,3}};

int n,m,i,j,k,ttt,tt,cur,c,a[1009009],x;
string s;
char ch;

int main(){
	File;
	SC(ttt);
	for (tt=1; tt<=ttt; tt++){
		printf("Case #%d: ",tt);
		scanf("%d%d\n", &n, &x);
		x=min(x,12+(x%4));
		getline(cin, s);
		for (i=1; i<=n*x; ++i){
			ch=s[(i-1)%n];
			if (ch=='i') a[i]=5;
			if (ch=='j') a[i]=6;
			if (ch=='k') a[i]=7;
		}
		n=n*x;
		c=0;
		cur=4;
		for (i=1; i<=n; ++i){
			cur=mul[cur][a[i]];
			if (cur==5){
				++c;
				++i;
				break;
			}
		}
		cur=4;
		for (; i<=n; ++i){
			cur=mul[cur][a[i]];
			if (cur==6){
				++c;
				++i;
				break;
			}
		}
		cur=4;
		for (; i<=n; ++i){
			cur=mul[cur][a[i]];
		}
		if (cur==7 && c==2) printf("YES");
		else printf("NO");
		printf("\n");
	}
	return 0;
}
