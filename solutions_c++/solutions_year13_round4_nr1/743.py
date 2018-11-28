#include<stdio.h>
#include<algorithm>
#include<vector>

using namespace std;

struct tckt{
	int o,e,p;
};

int n,m;
tckt tickets[1001];
vector<int> xs;
long long p[2001];

int cost(int befcost, int l,long long p){
	long long x = (long long)l * (long long)(n+n-l+1) / (long long)2;
	x = (x%1000002013LL) * (p%1000002013LL);
	x = x + (long long)befcost;
	return int(x%1000002013LL);
}

void process(){
	int i,j,rdcost=0, nmcost=0;
	for(i=0;i<m+m;i++) p[i]=0;
	xs.clear();

	for(i=0;i<m;i++){
		nmcost=cost(nmcost, tickets[i].e-tickets[i].o, tickets[i].p);
	}

	for(i=0;i<m;i++){
		xs.push_back(tickets[i].o);
		xs.push_back(tickets[i].e);
	}
	sort(xs.begin(), xs.end());
	vector<int>::iterator vit = unique(xs.begin(), xs.end());
	xs.erase(vit, xs.end());

	for(i=0;i<m;i++){
		for(j=0;j<xs.size()-1;j++){
			if(tickets[i].o<=xs[j] && xs[j+1]<=tickets[i].e){
				p[j]+=(long long)tickets[i].p;
			}
		}
	}
	p[xs.size()]=0;
	
	vector< pair<long long, int> > ps;
	for(i=0;i<xs.size()-1;i++){
		if(p[i]==0) continue;
		long long minp=p[i];
		ps.clear();
		for(j=i;j<xs.size();j++){
			if(p[j]<minp){
				ps.push_back( make_pair(minp, j) );
				minp=p[j];
			}
		}
		
		ps.push_back( make_pair(0,0) );
		for(j=0;j<ps.size()-1;j++){
			rdcost=cost(rdcost,xs[ps[j].second]-xs[i],(ps[j].first-ps[j+1].first));
		}

		int pi=0;
		for(j=i;j<xs.size()-1;j++){
			if(j==ps[pi].second){
				pi++;
			}
			p[j]-=ps[pi].first;
		}
	}
	rdcost=nmcost-rdcost;
	if(rdcost<0) rdcost+=1000002013;
	printf("%d\n",rdcost);
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i,t,tc;
	scanf("%d",&t);
	for(tc=1;tc<=t;tc++){
		printf("Case #%d: ",tc);
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++){
			scanf("%d%d%d",&tickets[i].o,&tickets[i].e,&tickets[i].p);
		}
		process();
	}
	return 0;
}