#include<cstdio>
#include<set>
#include<algorithm>
#include<vector>
using namespace std;

int war(set<double> S1, set<double> S2)
{
	set<double>::iterator it,it1;

	for(it=S1.begin();it!=S1.end();it++){
		double ele=*it;
		it1=S2.lower_bound(ele);
		if(it1!=S2.end()) S2.erase(it1);
	}
	return S2.size();
}

int dwar(set<double> S1, set<double> S2)
{
	if(S1.size()==0) return 0;
	set<double>::iterator it1,it2;
	it1=S1.begin();
	it2=S2.begin();
	if(*it1<*it2){
		S1.erase(it1);
		it2=S2.end();it2--;
		S2.erase(it2);
		return dwar(S1,S2);
	} else if(*it1 > *it2) {
		S1.erase(it1);
		S2.erase(it2);
	      return 1 + dwar(S1,S2);
	}
	return 0;
}

int main()
{
	int T,tc=1;
	scanf(" %d",&T);
	while(T--){
		int N,i;
		double x;
		scanf(" %d",&N);
		set<double> S1,S2;
		for(i=0;i<N;i++) { scanf(" %lf",&x); S1.insert(x); }
		for(i=0;i<N;i++) { scanf(" %lf",&x); S2.insert(x); }

		printf("Case #%d: %d %d\n",tc++,dwar(S1,S2),war(S1,S2));
	}
	return 0;
}
