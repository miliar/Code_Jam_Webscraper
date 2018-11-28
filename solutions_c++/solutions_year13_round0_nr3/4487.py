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

int turn(int n){
    int m=0;
    while (n>0) {
        m=m*10+n%10;
        n/=10;
    }
    return m;
}


int main(){
    
    FILE* fin= freopen("/Users/w_shunn/Desktop/C-small-attempt0.in.txt", "r", stdin);
    
    FILE* fout= freopen("/Users/w_shunn/Desktop/output.txt", "w", stdout);
    
    
    int T;
    cin>>T;
    
    for (int a=1; a<=T; a++) {
        int A,B;
        cin>>A>>B;
        
        int res=0;
        for (int i=A; i<=B; i++) {
            if ((int)sqrt(i)*(int)sqrt(i)!=i)continue;
            res+=(turn(i)==i)&&(turn((int)sqrt(i))==(int)sqrt(i));
        }
        
        
        printf("Case #%d: %d\n",a,res);
        
    }
    
    fclose(fin);
    fclose(fout);
    
    
    return 0;
}
