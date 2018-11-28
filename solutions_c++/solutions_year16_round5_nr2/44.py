#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>
#include <random>
using namespace std;

vector<int> child[101];
char moji[111];
int siz[111];

mt19937 gen;
uniform_real_distribution<double> rnd(0.0,1.0);

string r_f(vector<int> ps);
string r_t(int p);

int getsiz(int p){
	siz[p]=1;
	for(int i=0;i<child[p].size();i++)siz[p]+=getsiz(child[p][i]);
	return siz[p];
}

string r_f(vector<int> ps){
	vector<int> a;
	for(int i=0;i<ps.size();i++){
		for(int j=0;j<siz[ps[i]];j++)a.push_back(i);
	}
	
	vector<string> ss(ps.size());
	for(int i=0;i<ps.size();i++)ss[i]=r_t(ps[i]);
	
	vector<int> pos(ps.size());
	for(int i=a.size();i>=1;i--)swap(a[rnd(gen)*i],a[i-1]);
	string ret;
	for(int i=0;i<a.size();i++){
		ret+=ss[a[i]][pos[a[i]]];
		pos[a[i]]++;
	}
	return ret;
}

string r_t(int p){
	return string(1,moji[p])+r_f(child[p]);
}

int main(){
	int testcases;
	scanf("%d",&testcases);
	for(int casenum=1;casenum<=testcases;casenum++){
		printf("Case #%d: ",casenum);
		int n;
		scanf("%d",&n);
		vector<int> par(n);
		for(int i=0;i<n;i++){scanf("%d",&par[i]);par[i]--;}
		
		scanf("%s",moji);
		
		int m;
		scanf("%d",&m);
		vector<string> s(m);
		for(int i=0;i<m;i++){
			char buf[1010];
			scanf("%s",buf);
			s[i]=string(buf);
		}
		
		for(int i=0;i<n;i++)child[i].clear();
		for(int i=0;i<n;i++){
			if(par[i]!=-1)child[par[i]].push_back(i);
		}
		for(int i=0;i<n;i++)siz[i]=-1;
		for(int i=0;i<n;i++)if(siz[i]==-1)getsiz(i);
		//for(int i=0;i<n;i++)printf("s%d\n",siz[i]);
		
		int T=10000;
		vector<int> freq(m);
		for(int t=0;t<T;t++){
			vector<int> roots;
			for(int i=0;i<n;i++)if(par[i]==-1)roots.push_back(i);
			string ret=r_f(roots);
			//printf("%s\n",ret.c_str());
			for(int j=0;j<m;j++)if(ret.find(s[j])!=string::npos)freq[j]++;
		}
		for(int i=0;i<m;i++){
			printf("%f",(double)freq[i]/T);
			if(i+1<m)printf(" "); else printf("\n");
		}
	}
}