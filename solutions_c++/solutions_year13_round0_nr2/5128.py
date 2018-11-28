#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <fstream>
using namespace std;
typedef long long ll;
typedef vector<int> vint;
typedef pair<int, int> pint;
#define INF 1000000000 //10^9
#define MOD 1000000007 //10^9+7
#define REP(i,a,b) for(int i=a;i<b;i++)
#define QSORT(a) sort(a.begin(),a.end());


int main(){
    
    FILE* fin= freopen("/Users/w_shunn/Desktop/B-large.in.txt", "r", stdin);
    
    FILE* fout= freopen("/Users/w_shunn/Desktop/output.txt", "w", stdout);
    
    
    int T;
    cin>>T;
    
    for (int a=1; a<=T; a++) {
        int N,M;
        cin>>N>>M;
        
        int num[100][100];
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                cin>>num[i][j];
                
            }
        }
        
        int v[100]={},h[100]={};
        
        //v
        
        for (int i=0; i<M; i++) {
            for (int j=0; j<N; j++) {
                v[i]=max(num[j][i],v[i]);
            }
        }
        
        //h
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                h[i]=max(num[i][j],h[i]);
            }
        }
        
        int test[100][100];
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                test[i][j]=max(h[i],v[j]);
            }
        }
        
        
        for (int i=0; i<M; i++) {
                for (int j=0; j<N; j++) {
                    test[j][i]=min(test[j][i],v[i]);
                }
        }
        
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                    test[i][j]=min(test[i][j],h[i]);
                }
        }
        
        bool res=1;
        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                res&=(test[i][j]==num[i][j]);
            }
        }
        
        
        printf("Case #%d: ",a);
        if (res)printf("YES\n");
        else printf("NO\n");
        
    }
    
    fclose(fin);
    fclose(fout);
    
    
    return 0;
}
