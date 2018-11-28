#include <algorithm>
#include <iostream>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <set>
#include <map>
#include <ctime>
#define INF 0x3f3f3f3f
#define Mn 100010
#define Mm 200010
#define mod 1000000007
#define CLR(a,b) memset((a),(b),sizeof((a)))
#define CPY(a,b) memcpy ((a), (b), sizeof((a)))
#pragma comment(linker, "/STACK:102400000,102400000")
#define ul (u<<1)
#define ur (u<<1)|1
using namespace std;
typedef long long ll;
int a[Mn];
int main() {
	freopen("B-large.in","r",stdin);
   	freopen("002.out","w",stdout);
	int t,cas=0;
	scanf("%d",&t);
	while(t--) {
		string s;
		cas++;
		cin>>s;
		printf("Case #%d: ",cas);
		int num=0;
		for(int i=s.size()-1;i>=0;i--) {
			if(s[i]=='+') continue;
			else {
				num++;
				for(int j=0;j<=i;j++) {
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
			}
		}
		printf("%d\n",num);
	}
    return 0;
}
