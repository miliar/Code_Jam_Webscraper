#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<string> vs;

#define st          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())
#define EPS         1e-6
//double diffclock(clock_t clock1,clock_t clock2) { double diffticks=clock1-clock2; double diffms=(diffticks*10)/CLOCKS_PER_SEC; return diffms; }
int main(){
//clock_t begin=clock();
int t;
cin >> t;
for(int test=1;test<=t;test++){
     double c,f,x;
     cin >> c >> f >> x;
     double ans = x / 2.0;
     double f2 = f+2;
     double cur = (c/2.0) + (x/(f2));
     for(int i=1;cur < ans;i++){
          if(cur - ans < EPS){
                 ans = cur;
          }
          //ans = min(ans,cur);
          cur = cur - x/f2 + c/f2;
          f2+=f;
          cur += x/f2;
     }
     cout << "Case #" << test << ": " << fixed << setprecision(7) << ans << endl;
}
//clock_t end=clock(); cout << "Time elapsed: " << double(diffclock(end,begin)) << " ms"<< endl;
return 0;
}
