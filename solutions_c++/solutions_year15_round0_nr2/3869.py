#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<(n);++i)

int TC;
int n;
map<vector<int>, int> m;
int now=0;

int calc(vector<int> vec){
    sort(vec.begin(),vec.end());
    if(m.count(vec))return m[vec];
    if(vec.empty())return m[vec]=0;

    int x=114514;
    vector<int> vv=vec;
    for(int i=0;i<vec.size();++i){
	for(int j=1;j<vec[i];++j){
	    vv[i]-=j;
	    vv.push_back(j);
	    x=min(x,calc(vv)+1);
	    vv.pop_back();
	    vv[i]+=j;
	}
    }
    vector<int> nv;
    rep(i,vec.size())if(vec[i]>1)nv.push_back(vec[i]-1);
    x=min(x,calc(nv)+1);
    return m[vec]=x;
}

int main(){
    scanf("%d",&TC);
    rep(tc,TC){
	printf("Case #%d: ", tc+1);
	scanf("%d", &n);
	vector<int> p(n);
	rep(i,n)scanf("%d",&p[i]);
	printf("%d\n",calc(p));
    }
    return 0;
}
