#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#include <vector>

#define mk make_pair
typedef  long long  LL;

using namespace std;

char re[1024];

int main(){
	int T;
	scanf("%d",&T);
	for(int pp=1;pp<=T;pp++){
		int n;
		vector<int> q;
		scanf("%d",&n);
		scanf("%s",re);
		for(int i=0;i<=n;i++)
			q.push_back(re[i]-'0');
		int ans = 0, tmp =0;
		for(int i=0;i<=n;i++){
			if(tmp<i && q[i]>0){
				ans+=i-tmp;
				tmp=i;
			}
			tmp+=q[i];
		}
		printf("Case #%d: %d\n",pp,ans);
	}
	
	return 0;
}