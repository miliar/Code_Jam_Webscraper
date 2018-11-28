#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cassert>
#include <queue>
#include <iostream>
using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define lb(x) ((x)&(-(x)))
#define ms(x,y) memset(x,y,sizeof(x))
typedef vector<int> VI;
typedef long long ll;
typedef pair<int,int> PI;
const ll mod=1000000007;
const int inf=0x20202020;
const int N=505;
//head


char str[105];

int main()
{
	int t;
	scanf("%d\n",&t);
	for(int ct=1;ct<=t;ct++) {
		scanf("%s",str);
		int tmp=0,len=strlen(str);
		str[len]='+'; str[len+1]='\0';
		for(int i=0;i<len;i++)
			if(str[i] != str[i+1])
				tmp++;
		printf("Case #%d: %d\n",ct,tmp);
	}
	return 0;
}

