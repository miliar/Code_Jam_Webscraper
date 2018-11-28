#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cstring>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define VI vector<int>
#define PII pair<int,int>
#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define lint long long int
#define max_n 1005

using namespace std;

lint gcd(lint a,lint b){
	return a%b==0 ? b : gcd(b,a%b);
}

int n; VI v,w;
int gdzie[max_n];

void przesun1(int i, int j){
	int u = i;
	while(u!=j){
		gdzie[v[u]]=u+1;
		gdzie[v[u+1]]=u;
		swap(v[u],v[u+1]);
		
		u++;
	}
}

void przesun2(int i,int j){
	int u = i;
	while(u!=j){
		gdzie[v[u]]=u-1;
		gdzie[v[u-1]]=u;
		swap(v[u],v[u-1]);
		u--;
	}
}



int main(){
	int z; scanf("%d",&z);
	int casenr=0;
	while(z--){
		casenr++;
		printf("Case #%d: ",casenr);
		v.clear();
		w.clear();
		scanf("%d",&n);
		int maxi = 0;
		int dla = 0;
		FOR(i,0,n){
			int a; scanf("%d",&a);
			v.pb(a); w.pb(a);
		}
		sort(w.begin(),w.end());
		FOR(i,0,n){
			FOR(j,0,n)
				if(v[i]==w[j]) v[i] = -j;
		}
		FOR(i,0,n) v[i] = -v[i];
		FOR(i,0,n) gdzie[v[i]] = i;



		int best = 1e6;
		
		
			int res = 0;
			int pos1 = 0; int pos2 = n-1;
			FOR(i,0,n-1){
				int u = gdzie[i];
				if(u-pos1<pos2-u){
					res+=u-pos1;

					przesun2(u,pos1);
					pos1++;
				}
				else{
					res+=pos2-u;
					przesun1(u,pos2);
					pos2--;
				}
			}
		printf("%d\n",res);


	}
	return 0;
}
  

