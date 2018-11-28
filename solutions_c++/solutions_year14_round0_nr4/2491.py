#include<cstdio>
#include<set>
#include<algorithm>
#include<vector>
#define For(Q,W) for(int Q=0; Q<W; Q++)
using namespace std;

int main(){
	int t;
	scanf("%d ",&t);
	For(test,t){
		printf("Case #%d: ",test+1);
		int n;
		scanf("%d ",&n);
		set<double> a,b;
		vector<pair<double,bool> > d;
		For(i,n){
			double pom;
			scanf("%lf ",&pom);
			a.insert(pom);
			d.push_back(make_pair(pom,true));
		}
		For(i,n){
			double pom;
			scanf("%lf ",&pom);
			b.insert(pom);
			d.push_back(make_pair(pom,false));
		}
		
		int nedala=0;
		sort(d.begin(), d.end());
		int mam = 0;
		For(i,d.size()){
			if(d[i].second) mam++;
			else{
				if(mam!=0) mam--;
				
			}
		}
		int good=0;
		
		while(!a.empty()){
			if(*a.rbegin()> *b.rbegin()){
				good++;
				a.erase(*a.rbegin());
				b.erase(*b.rbegin());
				
			}
			else{
				a.erase(a.begin());
				b.erase(*b.rbegin());
			}
		}
		
		
		printf("%d ",good);
		
		
		printf("%d\n",mam);
	}
}
