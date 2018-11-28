#include <iostream> 
#include <sstream> 
#include <vector> 
#include <set> 
#include <map> 
#include <algorithm> 
#include <string> 
#include <cstring> 
#include <iomanip>

using namespace std; 

int ttt, tttt;
long long x[100], need, can;
int n,i,j;
long long b,q,bb,hh;
double ans;

double f(int v, long long e){
       long long sum = 0, sum2 = 0;
       int i;
       for (i=1;i<=v;i++){
           if (e<x[i]) return -1000000000000000.0+e;
           sum += (e-x[i]);           
       }
            
       for (i=v+1;i<=37;i++)
           if (x[i]<=e+1) sum2 += (e+1-x[i]);

       if (sum+sum2>b) return -1000000000000000.0-e;
                  
       return (sum*36+0.0)/v-sum-sum2;
}

int main(){
    freopen("a2.dat","r",stdin);
    freopen("a2.sol","w",stdout);
    cin >> ttt;
    for (tttt=1;tttt<=ttt;tttt++){
        cout << "Case #" << tttt << ": ";
        
        cin >> b >> n;
        for (i=0;i<37;i++) x[i] = 0;
        for (i=0;i<n;i++) cin >> x[i];        
        sort(x,x+37);
        x[37] = 1000000000000000000LL;
        for (i=37;i>=0;i--) x[i+1] = x[i];
        q = 0;
        ans = 0;
        cout << fixed << setprecision(15);
        
        long long l,r,c1,c2;
        
        for (i=1;i<=37;i++){
            l = 0;
            r = 100000000000000LL;
            while (l+3<r){
                  c1 = l+(r-l)/3;
                  c2 = r-(r-l)/3;
                  if (f(i,c1)<f(i,c2)) l = c1; else r = c2;
            }
//            if (i == 35) cout << l << " " << r << " " << f(i,391) << " " << f(i,392) << endl;
            while (l<=r){
                  ans = max(ans, f(i,l));
//                  cout << i << " " << l << " " << f(i,l) << endl;
                  l++;
            }
        }
               
        cout << ans << endl;
        
    }
//    system("pause");
    return 0;
}

 
