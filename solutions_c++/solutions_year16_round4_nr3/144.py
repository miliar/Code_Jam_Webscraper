#include<bits/stdc++.h>
#define MAX   1111
#define HOR(x,y) ((x)*n+(y))
#define VER(x,y) ((x)*(n+1)+(y)+(m+1)*n)
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
#define MASK(i) (1LL<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define next   ___next
#define prev   ___prev
#define left   ___left
#define right   ___right
#define __builtin_popcount __builtin_popcountll
using namespace std;
template<class X,class Y>
    void minimize(X &x,const Y &y) {
        if (x>y) x=y;
    }
template<class X,class Y>
    void maximize(X &x,const Y &y) {
        if (x<y) x=y;
    }
class DisjointSet {
	private:
	vector<int> label; //label[x] stores the root of x if x is not root, otherwise it stores -(size of x's set).
	public:
	DisjointSet(){}
	DisjointSet(int n) {
		label.assign(n+7,-1); //label should contains at least n+1 elements, as x is 1-indexed.
		//At first, each node is a seperate set of size 1.
	}
	int find(int x) { //find the root of set which contains x.
		if (label[x]<0) return (x); //x is root iff label[x] is negative.
		label[x]=find(label[x]);
		return (label[x]); //find the root of x by recursion.
	}
	bool join(int a,int b) { // join the sets which contains a and b. Return false iff a and b are already in the same set.
		int x=find(a);
		int y=find(b);
		if (x==y) return (false); //A set contains both a and b.
		if (label[x]>label[y]) swap(x,y); //label[x]>label[y] means size(x)<size(y).
		//We speed up the disjoint set by joinning the smaller set to the bigger set
		label[x]+=label[y];
		label[y]=x; //Update the label of x and y.
		return (true);
	}
	int getSize(int x) { //return the size of set which contains x.
		return (-label[find(x)]);
	}
	bool sameSet(int x,int y) {
        return (find(x)==find(y));
	}
};
const char noAns[]="IMPOSSIBLE";
int m,n;
pair<int,int> couple[MAX];
int perm[MAX];
void init(void) {
    scanf("%d%d",&m,&n);
    REP(i,2*(m+n)) scanf("%d",&perm[i]);
    REP(i,m+n) couple[i]=make_pair(perm[2*i]-1,perm[2*i+1]-1);
}
int address(int x) {
    if (x<n) return (HOR(0,x));
    if (x<m+n) return (VER(x-n,n));
    if (x<m+2*n) return (HOR(m,m+2*n-1-x));
    return (VER(2*m+2*n-1-x,0));
}
bool ok(int mask) {
    DisjointSet dsu((m+1)*n+(n+1)*m);
    REP(i,m) REP(j,n) {
        if (BIT(mask,i*n+j)) {
            dsu.join(HOR(i,j),VER(i,j+1));
            dsu.join(HOR(i+1,j),VER(i,j));
        } else {
            dsu.join(HOR(i,j),VER(i,j));
            dsu.join(HOR(i+1,j),VER(i,j+1));
        }
    }
    REP(i,m+n) if (!dsu.sameSet(address(couple[i].fi),address(couple[i].se))) return (false);
    return (true);
}
void process(int tc) {
    printf("Case #%d:\n",tc);
    REP(mask,MASK(m*n)) if (ok(mask)) {
        REP(i,m) {
            REP(j,n) printf("%c",BIT(mask,i*n+j)?'\\':'/');
            printf("\n");
        }
        return;
    }
    printf("%s\n",noAns);
}
int main(void) {
    int t; scanf("%d",&t);
    FOR(i,1,t) {
        init();
        process(i);
    }
    return 0;
}
