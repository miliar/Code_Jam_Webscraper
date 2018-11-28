#include <iostream>
#include <algorithm>
#include <utility>

using namespace std;

typedef unsigned long long ll;
typedef pair<ll, ll> ii;
typedef pair<ii, ll> PR;
const int MAXN = 2*1005;
const ll MD = 1000002013ll;
    ll n, m;
ll getk(ll d)
{
  ll t = d*(2*n - d + 1);
  t /= 2;
  t %= MD;
  return t;
}

ll getk(ll dif, ll c)
{
  ll a = getk(dif);
  a *= c;
  a %= MD;
  return a;
}

int main()
{
  int nt;
  cin >> nt;
  for(int it=1; it<=nt; it++)
  {
    ll ans = 0;
    //static PR dat[MAXN];
    static ll ep[2*MAXN];
    int nenp = 0;

    cin >> n >> m;
    ll knorm = 0;

    ii stp[MAXN];
    ii edp[MAXN];
    int nio =0;
    
    for(int i=0; i<m; i++){
      ll s, e, c;
      cin >> s >> e >> c;
      if (s != e){
        
        stp[nio] = ii (s, c);
        edp[nio++] = ii (e, c);
        
        ep[nenp++] = s;
        ep[nenp++] = e;
        knorm += getk(e-s, c);
        knorm %= MD;
      }
    }
    
    sort(ep, ep+nenp);
    int wr = 1;
    for(int i=1; i<nenp; i++){
      if (ep[i] != ep[wr - 1]){
        ep[wr++] = ep[i];
      }
    }
    nenp = wr;
    
    sort(stp, stp+nio);
    sort(edp, edp+nio);
    static ll lp[MAXN* 2];
    static ll cp[MAXN *2];
    
    int cstp = 0;
    int cedp = 0;
    ll ccnt = 0;
    for(int i=0; i<nenp; i++){
      ll cpos =  ep[i];
      while (cedp < nio && edp[cedp].first == cpos){
        ccnt -= edp[cedp].second;
        cedp++;
      }
     while (cstp < nio && stp[cstp].first == cpos){
        ccnt += stp[cstp].second;
        cstp++;
      }
      cp[i] = ccnt;
      lp[i] = ep[i+1] - ep[i];
    }
    bool g = true;
    ll kbad = 0;
    const ll RST = 1000ll*1000ll*1000ll*2000ll;
    while (g){
      g = false;
      ll mxc = RST;
      ll cl = 0;
      int fp = 0;
      for(int i=0; i<nenp; i++)
      {
        if (cp[i] == 0)
        {
          ll ad = getk(cl, mxc);
          if (ad)g = true;
          kbad += ad;
          kbad %= MD;
          for(int j = fp; j < i; j++){
            cp[j] -= mxc;
          }
          cl = 0;
          fp = i + 1;
          mxc = RST;
        }
        else
        {
          cl += lp[i];
          mxc = min(mxc, cp[i]);
        }
      }
    }
    if (kbad < knorm)ans = knorm - kbad;
    else ans = knorm - kbad + MD;
    ans %= MD;
    
    cout << "Case #" << it << ": " << ans << "\n";
  }
  return 0;
}
