#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <list>
#include <set>
#include <queue>
#include <iostream>
#include <map>
#include <bitset>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
typedef pair<int,int> PI;
typedef pair<double,double> PD;

#define FOR(x, b, e) for(int x=b; x<=(e); ++x)
#define FORD(x, b, e) for(int x=b; x>=(e); ......x)
#define REP(x, n) for(int x=0; x<(n); ++x)
#define VAR(v,n) typeof(n) v=(n)
#define ALL(c) c.begin(),c.end()
#define SIZE(x) (int)(x).size()
#define FOREACH(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define PB push_back
#define ST first
#define ND second

#define DEBUG 1
#define DEBUG_ON
#define INF 10000000; 


#define NEWLINE cout<<"\n"
#define REPORT(x) cout<<#x<<"="<<(x)<<endl;
#define ASSURE(x) cout<<#x<<endl<<flush
#define ASSERT(x) if(!(x)) REPORT("warunek nie spelniony!!")
template <typename T>
void write(T begin, T end)
{
	T ptr = begin;
	while(ptr!=end){
		cout<<*(ptr++)<<" ";
	}
	cout<<endl;
} 
template <>
void write(pair<int,int> * begin, pair<int,int> * end){
	pair<int,int>* ptr = begin;
	while(ptr!=end){
		cout<<"("<<(ptr->first)<<","<<(ptr->second)<<") ";
		++ptr;
	}
	cout<<endl;

}	
template <typename T>
T to(const std::string & s)
{
    std::istringstream stm(s);
    T result;
    stm >> result;
    return result;
}



template<class T, class K>
ostream& operator<<(ostream& out, const pair<T,K> & p){
	out<<"("<<p.first<<","<<p.second<<")";
	return out;
}

int T[100][100];
int T_maxrow[100];
int T_minrow[100];
int T_mincol[100];
int T_maxcol[100];
int N,M;

void testCase(){
    scanf("%d %d",&N,&M);
    REP(i,N) REP(j,M){
        scanf("%d",&T[i][j]);
    }
    REP(i,N){ T_maxrow[i]=0; T_minrow[i] = 101;}
    REP(i,M){ T_maxcol[i]=0; T_mincol[i] = 101;}

    REP(i,N) REP(j,M){
        T_maxrow[i] = max(T_maxrow[i],T[i][j]);
        T_minrow[i] = min(T_minrow[i],T[i][j]);
    }

    REP(i,M) REP(j,N){
        T_maxcol[i] = max(T_maxcol[i],T[j][i]);
        T_mincol[i] = min(T_mincol[i],T[j][i]);
    }


    //dane wczytane
    
    //check equivalent condition
    REP(i,N){
        REP(j,M){
            if(!(T_maxrow[i] == T[i][j] || T_maxcol[j] == T[i][j])){
                printf("NO\n");
                return;
            }
        }
    }

    printf("YES\n");
}

int main(){
    int T;
    scanf("%d",&T);
    REP(i,T){
        printf("Case #%d: ",i+1);
        testCase();
    }
    return 0;
}	

	
