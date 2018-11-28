#include<iostream>
#include<string>
#include<algorithm>
#include<stack>
#include<queue>
#include<set>
#include<complex>
#include<map>
#include<list>
#include<deque>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>

#define pb push_back
#define clr clear()
#define sz size()
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define all(a) (a).begin(),(a).end()
using namespace std;

typedef long long ll;
typedef vector<int> vi;

struct BigInt{
  vi v;
  int s;

  BigInt(void){v.clr;s=0;}
  
  BigInt(int x){
    v.clr; s = 1;
    if(!x)s = 0;
    else if(x<0){ s = -1; x *= -1; }
    while(x){ v.pb(x%10); x/=10; }
  }

  BigInt(string &x){
    int a = 0;
    v.clr; s = 1;
    if(x[0]=='-'){ s = -1; a = 1; }
    else if(x[0]=='0')s = 0;
    for(int i=x.sz-1;i>=a;i--)v.pb(x[i]-'0');
  }

  BigInt nega(void){
    BigInt t = *this;
    t.s *= -1;
    return t;
  }

  BigInt abs(void){
    if(s<0)return this->nega();
    return *this;
  }

  string bitos(void){
    if(!s)return "0";
    string res;
    REP(i,v.sz)res += v[i]+'0';
    reverse(res.begin(),res.end());
    return (s<0)?("-"+res):res;
  }

  BigInt operator+(BigInt a){
    if(!s)return a;
    if(!a.s)return *this;
    if(s==a.s){
      if(a.v.sz < v.sz)return a+(*this);
      REP(i,v.sz)a.v[i] += v[i];
      REP(i,a.v.sz-1)
	if(a.v[i]>9){
	  a.v[i] -= 10;
	  a.v[i+1]++;
	}

      if(a.v[a.v.sz-1]>9){
	a.v[a.v.sz-1] -= 10;
	a.v.pb(1);
      }
      return a;
    }else{
      if(s<0)return a-(*this).nega();
      else return (*this)-a.nega();
    }
  }
  
  BigInt operator-(BigInt a){
    if(!s)return a.nega();
    if(!a.s)return *this;   
    if(s==a.s){
      if(a.abs() > this->abs())return (a-(*this)).nega();
      BigInt b = *this;
      REP(i,a.v.sz)b.v[i] -= a.v[i];
      REP(i,b.v.sz-1)
	if(b.v[i]<0){
	  b.v[i] += 10;
	  b.v[i+1]--;
	}

      while(b.v.sz && !b.v.back())b.v.pop_back();
      if(b.v.empty())b.s=0;
      return b;
    }else return (*this)+a.nega();
  }

  BigInt operator*(BigInt a){
    if(!s)return *this;
    if(!a.s)return a;

    BigInt b(0),tmp;    
    REP(i,a.v.sz){
      tmp = *this;
      REP(j,tmp.v.sz)tmp.v[j] *= a.v[i];
   
      REP(j,tmp.v.sz){
	if(i+j<b.v.sz)b.v[i+j] += tmp.v[j];
	else b.v.pb(tmp.v[j]);
      }
    }

    REP(i,b.v.sz){
      if(b.v[i]>9){
	if(i+1<b.v.sz)b.v[i+1] += b.v[i]/10;
	else b.v.pb(b.v[i]/10);
	b.v[i] %= 10;
      }
    }
    b.s = s*a.s;
    return b;
  }

  void operator=(BigInt a){v = a.v;s = a.s;}

  bool operator==(BigInt a)const{
    if(s!=a.s)return false;
    if(!s)return true;
    if(v.sz!=a.v.sz)return false;
    REP(i,v.sz)if(v[i]!=a.v[i])return false;
    return true;
  }

  bool operator<(BigInt a)const{
    if(s!=a.s)return s<a.s;
    if(!s)return false;
    int d = v.sz - a.v.sz;
    if(d)return 0>d*s;
    for(int i=v.sz-1;i>=0;i--){
      d = v[i] - a.v[i];
      if(d)return 0>d*s;
    }
    return false;
  }

  bool operator<=(BigInt a)const{return (*this==a)||(*this<a);}
  bool operator>(BigInt a)const{return !(*this<=a);}
  bool operator>=(BigInt a)const{return !(*this<a);}
};

vector<BigInt> ps;
string a,b;
ll ans;

int cnt = 0;
void rec(int l,int n,string s,int sum){
  if(2*l>=n){
    cnt++;
    if(n&1)l--;
    for(int i=l-1;i>=0;i--)s += s[i];
    ps.push_back(BigInt(s)*BigInt(s));
    return;
  }

  for(int i=0;i<=3;i++){
    if(l==0 && i==0)continue;
    s += (char)('0'+i);
    int tmp = sum;
    if(2*(l+1)<=n)sum += i*i*2;
    else sum += i*i;
    if(sum<10)rec(l+1,n,s,sum);
    sum = tmp;
    s.erase(s.end()-1);
  }
}

int main(){
  int testcase;
  for(int i=1;i<=51;i++)rec(0,i,"",0);

  cin >> testcase;
  for(int casenum=1;casenum<=testcase;casenum++){
    cin >> a >> b;
    ans = upper_bound(all(ps),BigInt(b)) - lower_bound(all(ps),BigInt(a));
    cout << "Case #" << casenum << ": ";
    cout << ans << endl;
  }
}
