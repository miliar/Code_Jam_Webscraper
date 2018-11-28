#include <iostream> 
#include <sstream> 
#include <vector> 
#include <set> 
#include <map> 
#include <algorithm> 
#include <string> 
#include <cstring> 

using namespace std; 

int ttt, tttt;

int n,m,i,Q,w;
long long g;
int e[20000];
int o[20000];
int p[20000];
int A[20000];
long long r[20000];
long long c[20000];
long long ans, all, di, cost, aa;
long long md = 1000002013;

map<int, long long> sk;

void add(int v, int t){
     if (!sk.count(v)){
        Q++;
        A[Q] = v;
     }
     sk[v] += t;
     
}

int main(){
    freopen("a2.dat","r",stdin);
    freopen("a2.sol","w",stdout);
    cin >> ttt;
    for (tttt=1;tttt<=ttt;tttt++){
        sk.clear();
        Q = 0;
        aa = 0;
        
        cout << "Case #" << tttt << ": ";
        
        cin >> n >> m;
        for (i=1;i<=m;i++) {
            cin >> o[i] >> e[i] >> p[i];
            di = e[i]-o[i];
            cost = di*(long long)(n)-di*(di-1)/2;
            cost = ((cost%md)*(p[i]%md))%md;
            aa += cost;
            add(o[i], p[i]);
            add(e[i], -p[i]);
        }
        
        A[0] = 0;
        
        sort(A+1,A+Q+1);
        
        ans = 0;
        w = 0;
        
        all = 0;
        
        for (i=1;i<=Q;i++){
            g = sk[A[i]];
            if (g>0){
               w++;
               r[w] = A[i];
               c[w] = g;
            } else {
              while (g<0){
                    if (g+c[w]>=0){
                       di = A[i]-r[w];
                       cost = (di*((long long)(n))-di*(di-1)/2)%md;
                       cost = (cost*(-g))%md;
                       ans = (ans+cost)%md;
                       c[w] += g;
                       g = 0;
                    } else {
                       di = A[i]-r[w];
                       cost = (di*((long long)(n))-di*(di-1)/2)%md;
                       cost = (cost*(c[w]%md))%md;
                       ans = (ans+cost)%md;
                       g += c[w];   
                       w--;                       
                    }
              }
            }
        }
        
        cout << (aa-ans+md)%md << endl;
        
    }
//    system("pause");
    return 0;
}

 
