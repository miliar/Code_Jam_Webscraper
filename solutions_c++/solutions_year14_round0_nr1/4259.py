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
#define MAXN 1000005
#define inf 1e8
#define eps 1e-8
#define zero(x) (((x)>0?(x):-(x))<eps)
using namespace std;
typedef __int64 ll;
int main(){
	int ncase;
	cin>>ncase;
	int tid=0;
	int before[6];
	int after[6];
	while(ncase--){
		int fst;
		tid++;
		int val;
		cin>>fst;
		for(int i=1; i<=4; i++){
			for(int j=1; j<=4; j++){
				scanf("%d", &val);
				if(i==fst){
					before[j]=val;
				}
			}
		}
		cin>>fst;
		for(int i=1; i<=4; i++){
			for(int j=1; j<=4; j++){
				scanf("%d", &val);
				if(i==fst){
					after[j]=val;
				}
			}
		}

		int cnt=0;
		int target;
		for(int i=1; i<=4; i++){
			for(int j=1; j<=4; j++){
				if(after[i]==before[j]){
					cnt++;
					target=after[i];
				}
			}
		}
		if(cnt==0){
			printf("Case #%d: Volunteer cheated!\n", tid);
		}else if(cnt==1){
			printf("Case #%d: %d\n", tid, target);
		}else{
			printf("Case #%d: Bad magician!\n", tid);
		}
	}
}