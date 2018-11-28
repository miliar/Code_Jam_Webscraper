#include<algorithm>
#include<bitset>
#include<climits>
#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<deque>
#include<fstream>
#include<functional>
#include<iomanip>
#include<iostream>
#include<list>
#include<map>
#include<numeric>
#include<set>
#include<stack>
#include<string>
#include<utility>
#include<vector>
using namespace std;

#define f(i,n) for(i=0;i<n;++i)

int main() {
	
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);
	
	int t,tc,i,nf;
	double c,f,x,bst,cfv,cr,ck;
	scanf("%d",&t);
	for(tc=1;tc<=t;++tc) {
		cin>>c>>f>>x;
		cfv=0.0;
		cr=2.0;
		nf=0;
		bst=x/cr;
		while(1) {
			cfv+=c/cr;
			++nf;
			cr+=f;
			ck=cfv+(x/cr);
			if(ck<bst) bst=ck;
			else break;
		}
		printf("Case #%d: %.14g\n",tc,bst);
	}
}

