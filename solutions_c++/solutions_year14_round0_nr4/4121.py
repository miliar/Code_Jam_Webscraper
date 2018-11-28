#include <cmath>
#include <ctime>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <functional>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#define MAXN 1005
#define inf 1e8
#define eps 1e-8
#define zero(x) (((x)>0?(x):-(x))<eps)
using namespace std;
typedef __int64 ll;
double naomi[MAXN],ken[MAXN];
int main(){
	int ncase;
	double c, f, x;
	int id=0;
	cin>>ncase;
	while(ncase--){
		int n;
		id++;
		cin>>n;
		//memset(bnaomi, false,sizeof(bnaomi));
		//memset(ken, false, sizeof(ken));
		for(int i=0; i<n; i++)scanf("%lf", &naomi[i]);
		for(int i=0; i<n; i++)scanf("%lf", &ken[i]);
		sort(naomi, naomi+n);
		sort(ken, ken+n);

		int khead=0, kend=n-1;
		int deceivescor=0;
		for(int i=0; i<n; i++){
			//bnaomi[i]=true;
			if(naomi[i]<ken[khead]){
				kend--;
			}else{
				deceivescor++;
				khead++;
			}
		}
		int nhead=0, nend=n-1;
		khead=0, kend=n-1;
		int score=0;
		for(int i=n-1; i>=0; i--){
			if( ken[kend] < naomi[nend]){
				khead++;
				nend--;
				score++;
			}
			else{
				kend--;
				nend--;
			}
		}
		//sum+=x/cur;
		printf("Case #%d: %d %d\n", id, deceivescor, score);
	}
}