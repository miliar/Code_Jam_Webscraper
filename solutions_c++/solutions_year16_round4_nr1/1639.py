/*
 *    Google Code Jam 2016, Round 2, Problem A
 */
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cmath> 
#include <algorithm>
#include <vector>
#include <list>
#include <cstring>
#include <stack>
#include <map>
#include <set>
#include <utility>
#include <queue>
#include <deque>
#include <ctime>
#include <complex>
#include <bitset>
#include <time.h>
#include <iomanip>

using namespace std;
#define PB push_back
#define LL long long
#define MP make_pair
#define fi first
#define se second
typedef unsigned long long ULL;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

#define DBG 0

#define fori(i,a,b) for(int i = (a); i < (b); i++)
#define forie(i,a,b) for(int i = (a); i <= (b); i++)
#define ford(i,a,b) for(int i = (a); i > (b); i--)
#define forde(i,a,b) for(int i = (a); i >= (b); i--)
#define forls(i,a,b,n) for(int i = (a); i != (b); i = n[i])
#define mset(a,v) memset(a, v, sizeof(a))
#define mcpy(a,b) memcpy(a, b, sizeof(a))

#define MIN_LD -2147483648
#define MAX_LD  2147483647
#define MIN_LLD -9223372036854775808
#define MAX_LLD  9223372036854775807
#define MAX_INF 18446744073709551615
const int INF = 0x7fffffff;//use double for addition

typedef set<int> Set;
#define ALL(x) x.begin(),x.end()
#define INS(x) inserter(x,x.begin())
//set_union(ALL(x1),ALL(x2),INS(x)),set_intersection

int T, N,M;
int v[5],w[4100][15];
int cmp(int a,int b){
    if(a==b) return -1;
    int c = min(a,b), d = max(a,b);
    if(c==d-1){return c;}
    else return d;
}
char ar[3] = {'P','R','S'};
int dfs(string& a, int vv[5],int ww[4100][15],int idx){
    if(idx == M) return 1;
    int ans = -1;
    fori(i,0,3){
        if(vv[i]>0){
            int qq[4100][15];mcpy(qq,ww);
            qq[idx][0] = i;
            int good = 1;
            int curidx = idx;
            forie(j,1,N){
                if((curidx+1)%2==0){
                    qq[curidx/2][j] = cmp(qq[curidx-1][j-1],qq[curidx][j-1]);
                    if(qq[curidx/2][j] == -1){
                        good = 0;
                        break;
                    }
                    curidx/=2;
                }
                else{
                    break;
                }
            }
            
            if(!good){
                continue;
            }
            else{
                vv[i]--;
                a+=ar[i];//cout << "before a=" << a << endl;
                ans=dfs(a,vv,qq,idx+1);
                if(ans == 1) break;
                vv[i]++;
                a.erase(a.end()-1);//cout << "after a=" << a << endl;
            }
        }
    }
    return ans;
}
int main(void){
    
    cin.sync_with_stdio(false);
    cin >> T;
    forie(cnt,1,T){
        cin >> N >> v[1] >> v[0] >> v[2];
        M = (int) pow(2,N);
        cout << "Case #" << cnt << ": ";
        string a = "";mset(w,0);
        int ans = dfs(a,v,w,0);
        if(ans==-1){cout << "IMPOSSIBLE\n";}
        else{cout << a << endl;}
    }
        

        
    return 0;
}

