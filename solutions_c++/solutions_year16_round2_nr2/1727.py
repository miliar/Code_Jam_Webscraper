#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fi first
#define sc second
int n;
pair<int,pair<string,string> > get(string a,string b, int i, int aq1, int p){
  if(i==n){
    return {abs(aq1),{a,b}};
  }
  if(a[i]=='?' && b[i]=='?'){
    if(aq1==0){
      a[i] = '0';
      b[i] = '0';
      pair<int,pair<string,string> > aq12 = get(a,b,i+1,0,p/10);
      a[i] = '1';
      b[i] = '0';
      pair<int,pair<string,string> > aq1234 = get(a,b,i+1,p,p/10);
      a[i] = '0';
      b[i] = '1';
      pair<int,pair<string,string> > aq123 = get(a,b,i+1,-p,p/10);
      if(aq12.fi <= aq1234.fi && aq12.fi <=aq123.fi) return aq12;
      if(aq123.fi <= aq1234.fi && aq123.fi <=aq12.fi) return aq123;
      return aq1234;
    }
    else if(aq1<0){
      a[i]='9';b[i]='0';
      return get(a,b,i+1,aq1 + p*9,p/10);
    }
    else{
      a[i]='0';b[i]='9';
      return get(a,b,i+1,aq1 - p*9,p/10);
    }
  }
  else if(a[i]!='?' && b[i]!='?'){
    return get(a,b,i+1,aq1 + (a[i]-b[i])*p, p/10);
  }
  else if(a[i]=='?'){
    if(aq1<0){
      a[i] = '9';
    }
    else if(aq1>0){
      a[i] = '0';
    }
    else{
      a[i] = b[i];
      pair<int,pair<string,string> > aq12 = get(a,b,i+1,0,p/10);
      pair<int,pair<string,string> > aq1234,aq123;
      aq123.fi = INT_MAX;
      aq1234.fi = INT_MAX;
      if(b[i]!='0'){
        a[i] = b[i]-1;
        aq1234 = get(a,b,i+1,-p,p/10);
      }
      if(b[i]!='9'){
        a[i] = b[i]+1;
        aq123 = get(a,b,i+1,p,p/10);
      }
      if(aq1234.fi <= aq12.fi && aq1234.fi <=aq123.fi) return aq1234;
      if(aq12.fi <= aq1234.fi && aq12.fi <=aq123.fi) return aq12;
      return aq123;
    }
    return get(a,b,i+1, aq1 + p*(a[i]-b[i]),p/10);
  }
  else{
    if(aq1>0){
      b[i] = '9';
    }
    else if(aq1<0){
      b[i] = '0';
    }
    else{
      b[i] = a[i];
      pair<int,pair<string,string> > aq12 = get(a,b,i+1,0,p/10);
      pair<int,pair<string,string> > aq1234,aq123;
      aq123.fi = INT_MAX;
      aq1234.fi = INT_MAX;
      if(a[i]!='0'){
        b[i] = a[i]-1;
        aq1234 = get(a,b,i+1,p,p/10);
      }
      if(a[i]!='9'){
        b[i] = a[i]+1;
        aq123 = get(a,b,i+1,-p,p/10);
      }
      if(aq1234.fi <= aq12.fi && aq1234.fi <=aq123.fi) return aq1234;
      if(aq12.fi <= aq1234.fi && aq12.fi <=aq123.fi) return aq12;
      return aq123;
    }
    return get(a,b,i+1, aq1 + p*(a[i]-b[i]),p/10);
  }
}
signed main() {
  int tt;
  cin >> tt;
  for(int t=1;t<=tt;t++){
    cout << "Case #" << t << ": ";
    string a,b;
    cin >> a >> b;
    n = a.length();
    int c = 1LL;
    for(int i=0;i<n-1;i++) c *= 10;
    pair<int,pair<string,string> > p = get(a,b,0,0,c);
    cout << p.sc.fi << " " << p.sc.sc << "\n";
  }
    return 0;
}
