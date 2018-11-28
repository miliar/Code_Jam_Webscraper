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
		char buf[20202];
		scanf("%s",buf);
		int n=strlen(buf);
		vector<int> a;
		for(int i=0;i<n;i++){
			int p=(buf[i]=='C'?0:1);
			if(a.empty() || a.back()!=p)a.push_back(p);
			else a.pop_back();
		}
		printf("%d\n",5*(n-(int)a.size()/2));
	}
}