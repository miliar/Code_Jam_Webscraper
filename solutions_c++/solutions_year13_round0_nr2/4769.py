#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cmath>
#include <queue>
#include <cstdio>
#include <set>
#include <map>
#include <cstdlib>
#include <cstring>
#include <stack>
#include <cassert>
#include <limits.h>
#include <unistd.h>
#include <stdint.h>

typedef unsigned long long ULL;
typedef long long LL;

#define MIN(a,b) (a<b?a:b)
#define MAX(a,b) (a>b?a:b)
#define ABS(a) ((a>0)?a:-a)

#define SZ(a) ((int)a.size())
#define PB(a) push_back(a)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define REP(i,n) FOR(i,0,(int)(n-1))
#define FORD(i,a,b) for(int i=(a);i>=(b);i--)
#define printv(v) REP(i,SZ(v))printf("%d ",v[i]);
#define mp(a,b) make_pair(a,b)
#define PII pair<int,int>

#define Sd(t)   scanf("%d",&t)
#define Slld(t) scanf("%lld",&t)
#define Ss(t)   scanf("%s",t)
#define Slf(t)  scanf("%lf",&t)

#define Pd(t)   printf("%d",t)
#define Plld(t) printf("%lld",t)
#define Ps(t)   printf("%s",t)
#define Plf(t)  printf("%lf",t)

#define Pc(t)   printf("%c",t)
#define Pn	Pc('\n')
#define MOD 1000000007
#define MX 10000

class FastInput {
	public:
		FastInput() {
			m_dataOffset = 0;
			m_dataSize = 0;
			m_v = 0x80000000;
		}
		uint32_t ReadNext() {
			if (m_dataOffset == m_dataSize) {
				int r = read(0, m_buffer, sizeof(m_buffer));
				if (r <= 0) return m_v;
				m_dataOffset = 0;
				m_dataSize = 0;
				int i = 0;
				if (m_buffer[0] < '0') {
					if (m_v != 0x80000000) {
						m_data[m_dataSize++] = m_v;
						m_v = 0x80000000;
					}
					for (; (i < r) && (m_buffer[i] < '0'); ++i);
				}
				for (; i < r;) {
					if (m_buffer[i] >= '0') {
						m_v = m_v * 10 + m_buffer[i] - 48;
						++i;
					} else {
						m_data[m_dataSize++] = m_v;
						m_v = 0x80000000;
						for (i = i + 1; (i < r) && (m_buffer[i] < '0'); ++i);
					}
				}
			}
			return m_data[m_dataOffset++];
		}
	public:
		uint8_t m_buffer[32768];
		uint32_t m_data[16384];
		size_t m_dataOffset, m_dataSize;
		uint32_t m_v;
};

using namespace std;
int main(){
    freopen("./Lawnmower_in_2.txt","r",stdin);
    freopen("./Lawnmower_out_2.txt","w",stdout);
    int T,N,M,lawn[105][105],mxr[105],mxc[105],res[105][105];
    Sd(T);
    FOR(cs,1,T){
        REP(i,104){
            mxr[i] = mxc[i] = 0;
        }
        Sd(N);Sd(M);
        REP(i,N){
            REP(j,M){
                Sd(lawn[i][j]);
                if(lawn[i][j] > mxr[i])
                    mxr[i] = lawn[i][j];
                if(lawn[i][j] > mxc[j])
                    mxc[j] = lawn[i][j];
                res[i][j] = 100;
            }
        }
        REP(i,N){
            REP(j,M){
                if(res[i][j] > mxr[i])
                    res[i][j] = mxr[i];
            }
        }
        REP(i,N){
            REP(j,M){
                if(res[i][j] > mxc[j])
                    res[i][j] = mxc[j];
            }
        }
        int flag = 0;
        REP(i,N){
            REP(j,M){
                if(res[i][j] != lawn[i][j])
                    flag = 1;
            }
        }
        if(flag == 1){
            printf("Case #%d: NO\n",cs);
        }
        else
            printf("Case #%d: YES\n",cs);
    }
	return 0;
}
