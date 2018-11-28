#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int main(int argc,char **argv)
{
    freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
    int cnt,n,ans;
	char str[1020]; 
	cin >> cnt;
	for(int i=1;i<=cnt;i++){
		int res_ans=0,ans_x;
		printf("Case #%d: ", i);
		scanf("%d %s",&n,str);
		int a=str[0]-'0';int b=0;
		for(int i=1;i<=n;i++){
			int now=str[i]-'0';
			if(i>a){
				b+=(i-a);
				a=i;
			}
			a+=now;
			//printf("%d %d %d\n",a,b,i);
			
		}
		printf("%d\n",b);
	}
} 
