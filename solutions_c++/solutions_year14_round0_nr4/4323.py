#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <vector>

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;

vector<vi> AdjList;
vi match, vis;                                          // global variables

int Aug(int l) {                 // return 1 if an augmenting path is found
  if (vis[l]) return 0;                               // return 0 otherwise
  vis[l] = 1;
  for (int j = 0; j < (int)AdjList[l].size(); j++) {
    int r = AdjList[l][j];
    if (match[r] == -1 || Aug(match[r])) {
      match[r] = l; return 1;                           // found 1 matching
  } }
  return 0;                                                  // no matching
}

bool isprime(int v) {
  int primes[10] = {2,3,5,7,11,13,17,19,23,29};
  for (int i = 0; i < 10; i++)
    if (primes[i] == v)
      return true;
  return false;
}

int deceitWar(vector<double> a, vector<double> b) {
  int V = 2*((int)a.size()), Vleft = (int)a.size();                               // we ignore vertex 0
  AdjList.assign(V, vi());

  for(int i=0;i<Vleft;i++){
  	for(int j=0;j<Vleft;j++){
  		if(a[i]>b[j]){
  			AdjList[i].push_back(j);
  		}
  	}
  }

  int MCBM = 0;
  match.assign(V, -1);    // V is the number of vertices in bipartite graph
  for (int l = 0; l < Vleft; l++) {         // Vleft = size of the left set
    vis.assign(Vleft, 0);                    // reset before each recursion
    MCBM += Aug(l);
  }
  return MCBM;
}


int playWar(vector<double> n, vector<double> k){
	int ken = 0;
	int max = (int)n.size();
	double minDiff;
	vector<bool> notUsed (max,true);
	for(int i=0;i<max;i++){
		minDiff = 1.1;
		int rem = -1;
		for(int j=0;j<max;j++){
			if (k[i]>n[j] && notUsed[j]){
				if (k[i]-n[j]<minDiff){
					minDiff = k[i] - n[j];
					rem = j;
				}
			}
		}
		if(rem!=-1){
			ken++;
			notUsed[rem] = false;
		}
	}
	return max - ken;
}

int playDeceitWar(vector<double> n, vector<double> k){

	int currBest = (int)n.size();
	while(true){
		sort(n.begin(),n.end());
		sort(k.begin(),k.end());
		if(n[0]>k[k.size()-1]){
			return currBest;
		} else {
			n.erase(n.begin());
			k.pop_back();
			currBest--;
		}
		if(currBest==0){
			break;
		}
	}
	return currBest;
}

int main(){
	int t,n;
	double b;
	vector<double> naomi, n1, n2;
	vector<double> ken, k1, k2;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d",&n);	
		naomi.clear();
		ken.clear();
		for(int j=0;j<n;j++){
			scanf("%lf",&b);
			naomi.push_back(b);
		}
		for(int j=0;j<n;j++){
			scanf("%lf",&b);
			ken.push_back(b);
		}
		n1 = vector<double> (naomi);
		n2 = vector<double> (naomi);
		k1 = vector<double> (ken);
		k2 = vector<double> (ken);
		printf("Case #%d: %d %d\n",i,deceitWar(n1,k1),playWar(n2,k2));
	}
}