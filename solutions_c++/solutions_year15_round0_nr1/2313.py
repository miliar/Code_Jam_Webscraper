/*************************************************************************
    > File Name: gcja.cpp
    > Author: Lawrence_
    > Mail: 402374437@qq.com
    > Created Time: 2015/4/11 21:29:59
 ************************************************************************/
#include <cstdio>
#include <iostream>
#include <stack>
#include <queue>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <deque>
#include <list>
#include <map>
#include <vector>
#include <cstdlib>
#include <set>
#include <cctype>
#define ll long long
#define lson l,m,rt << 1
#define rson m+1,r,rt << 1 | 1
#define pi acos(-1)
#define INF 0x7f7f7f7f
#define Clear(name,init) memset(name,init,sizeof(name))
#define eps 1e-8
using namespace std;
int s;
char str[1015];
int main(){
    freopen("C:\\Users\\joho\\Desktop\\A-large.in","r+",stdin);
    freopen("C:\\Users\\joho\\Desktop\\A-small-attempt1.out","w+",stdout);
	int t;
	while(~scanf("%d",&t)){
		for(int cas = 1;cas <= t; cas++){
			scanf("%d %s", &s, str);
			int len = s + 1;
			int ans = 0;
			int pos = 0;
			for(int i = 0;i < len; i++){
				int x = str[i] - '0';
				if(i == 0){
					pos = x;
				}
				else{
					if(pos < i){
						int temp = i - pos;
						ans += temp;
						pos += temp + x;
					}
					else{
						pos += x;
					}
				}
			//printf("Case #%d: %d\n", cas, ans);
			}
			printf("Case #%d: %d\n", cas, ans);
	}
	}
	return 0;
}
