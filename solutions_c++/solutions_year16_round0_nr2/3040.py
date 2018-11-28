#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <queue>
#include <math.h>
#define MP make_pair

using namespace std;
typedef long long LL;
typedef unsigned int uint;
typedef pair<int,int> pii;
const double pi = atan (1.0) * 4;

char str[1000];

int main (){
//	freopen ("F:\\C++\\B-large.in", "r", stdin);
//	freopen ("F:\\C++\\B-large.out", "w", stdout);
	
	int T; scanf ("%d",&T);
	int cas = 1;
	while (T--){
		scanf ("%s", str);
		int exp=0, now, ans = 0;
		for (int i=strlen(str)-1;i>=0;i--){
			if (str[i] == '-')	now = 1;
			else				now = 0;
			if (exp == now){
				;
			}
			else{
				exp ^= 1;
				ans++;
			}
		}
		printf ("Case #%d: %d\n",cas++,ans);
	}
	return 0;
}