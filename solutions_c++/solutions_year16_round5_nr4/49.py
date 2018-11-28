#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
using namespace std;

int main(){
	int testcases;
	scanf("%d",&testcases);
	for(int casenum=1;casenum<=testcases;casenum++){
		printf("Case #%d: ",casenum);
		int n,l;
		scanf("%d%d",&n,&l);
		char buf[1000];
		bool ok=true;
		for(int i=0;i<n;i++){
			scanf("%s",buf);
			bool ones=true;
			for(int j=0;j<l;j++)if(buf[j]=='0')ones=false;
			if(ones)ok=false;
		}
		scanf("%s",buf);
		if(ok){
			if(l>1){
				for(int i=0;i<l;i++)printf("0?");printf(" ");
				for(int i=0;i<l-1;i++)printf("1");puts("");
			}else{
				puts("0 ?");
			}
		}else{
			puts("IMPOSSIBLE");
		}
	}
}