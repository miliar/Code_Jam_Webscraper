#include <cstdio>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>


using namespace std;

typedef pair<int,int> Pair;

template<class t>
ostream & operator << (ostream & tout,const vector<t> &s){
  tout<<'[';
  for (int i=0;i<s.size();i++)
    if (i+1 == s.size())
      tout<<s[i];
    else
      tout<<s[i]<<',';
  tout<<']';
  return(tout);
}

template<class a,class b>
ostream & operator << (ostream & tout,const pair<a,b> &c){
  return(tout<<'('<<c.first<<','<<c.second<<')');
}

template<class T> struct __set__print{
  __set__print(ostream& out) : tout(out), count(0) {}
  void operator() (T x) { 
    if (count > 0)
      tout<<',';
    tout<<x;
    ++count; 
  }
  ostream& tout;
  int count;
};

template<class T>
ostream & operator << (ostream & tout,const set<T> &s){
  tout<<'{';
  for_each(s.begin(),s.end(),__set__print<T>(tout));
  return(tout<<'}');
}

template<class T,class Q> struct print_map{
  print_map(ostream& out) : tout(out), count(0) {}
  void operator() (const pair<T,Q> &x) { 
    if (count > 0)
      tout<<',';
    tout<<'('<<x.first<<" => "<<x.second<<')';
    ++count; 
  }
  ostream& tout;
  int count;
};

template<class T,class Q>
ostream & operator << (ostream & tout,map<T,Q> s){
  tout<<'{';
  for_each(s.begin(),s.end(),print_map<T,Q>(tout));
  return(tout<<'}');
}

template<class T>
string to_string(T s){
  stringstream tin;
  tin<<s;
  string res;
  getline(tin,res);
  return(res);
}


template<class T>
vector<T> to_vector(T *s,int n){
  vector<T> result;
  for (int i=0;i<n;i++)
    result.push_back(s[i]);
  return(result);
}

// *********************************** MY CODE ***************************

class BigInteger{
public:
  vector<int> num;
  bool neg;

  inline void relax(){
    for (int i=0;i+1<(int)num.size();i++){
      num[i+1]+=num[i]/10;
      num[i]%=10;
    }

    if (num.size())
      while (num.back() >= 10){
	num.push_back(num.back()/10);
	num[num.size()-2]%=10;
      }

    while (num.size() > 1 && num.back() == 0) num.pop_back();
    if (num.size() == 1 && num[0] == 0) neg=false;
  }

  bool operator < (BigInteger s)const{
    if (neg != s.neg) return(neg);
    if (num.size() != s.num.size())
      return((num.size() < s.num.size())^neg);
    for (int i=num.size()-1;i>=0;i--)
      if (num[i] != s.num[i])
	return((num[i] < s.num[i])^neg);
    return(false);
  }

  BigInteger negative()const{
    BigInteger ans=*this;
    ans.neg=!ans.neg;
    ans.relax();
    return(ans);
  }

  BigInteger(int s=0){
    num.clear();
    neg=s < 0;
    num.push_back(abs(s));
    relax();
  }

  BigInteger operator + (BigInteger s)const{
    if (s.neg) return(operator - (s.negative()));
    if (neg) return(s - negative());
    BigInteger ans=*this;
    if (ans.num.size() < s.num.size()) ans.num.resize(s.num.size());
    for (int i=0;i<(int)s.num.size();i++) 
      ans.num[i]+=s.num[i];
    ans.relax();
    return(ans);
  }

  BigInteger operator - (BigInteger s)const{
    if (s.neg) return(operator + (s.negative()));
    if (neg) return((s+negative()).negative());
    if (operator < (s))
      return((s-(*this)).negative());
    BigInteger ans=*this;
    for (int i=0;i<(int)ans.num.size();i++){
      if (i < s.num.size())
	ans.num[i] -= s.num[i];
      if (ans.num[i] < 0){
	ans.num[i+1]--;
	ans.num[i]+=10;
      }
    }
    ans.relax();
    return(ans);
  }

  BigInteger operator * (BigInteger s)const{
    if (neg) return((negative()*s).negative());
    if (s.neg) return((operator * (s.negative())).negative());
    BigInteger ans;
    ans.num.resize(s.num.size()+num.size()-1);
    for (int i=0;i<(int)num.size();i++)
      for (int j=0;j<(int)s.num.size();j++)
	ans.num[i+j]+=num[i]*s.num[j];
    ans.relax();
    return(ans);
  }

  BigInteger operator / (BigInteger s)const{
    if (s.num.size() == 1 && s.num[0] == 0) 
      throw ("BigInteger : division by zero!!");

    if (neg) return((negative()/s).negative());
    if (s.neg) return((operator / (s.negative())).negative());
    BigInteger ans;
    ans.num.resize(max((int)num.size()-(int)s.num.size()+2,1));
    BigInteger sum;
    for (int i=(int)ans.num.size()-1;i>=0;i--){

      BigInteger x;
      x.num.resize(s.num.size()+i);
      for (int j=0;j<(int)s.num.size();j++)
	x.num[j+i]=s.num[j];
      x.relax();

      while (true){
	sum=sum+x;
	if (operator < (sum)){
	  sum=sum-x;
	  break;
	}
	ans.num[i]++;
      }
    }
    ans.relax();
    return(ans);
  }

  BigInteger operator % (BigInteger s)const{
    if (neg) return((negative()%s).negative());
    if (s.neg) return(operator % (s.negative()));
    return(operator - (s 
* (operator / (s))));
  }
};


ostream & operator << (ostream & tout,BigInteger s){
  if (s.neg) tout<<'-';
  for (int i=(int)s.num.size()-1;i>=0;i--)
    tout<<s.num[i];
  return(tout);
}

bool is_palindrome(BigInteger s){
  string a = to_string(s);
  for (int i=0;i<a.size();i++)
    if (a[i] != a[a.size()-i-1])
      return(false);
  return(true);
}

BigInteger tb(string s){
  BigInteger ans = 0;
  for (int i=0;i<s.size();i++)
    ans = ans*10+s[i]-'0';
  return(ans);
}

int CC = 51;

int main(){
  ios_base::sync_with_stdio(false) ;
  set<BigInteger> st;
  for (int i=0;i<=99;i++){
    BigInteger x = i;
    if (is_palindrome(x)){
      st.insert(x);
    }
  }
  vector<BigInteger> all;
  while (st.size()){
    BigInteger t = *st.begin();
    st.erase(t);
    if (is_palindrome(t*t)){
      all.push_back(t*t);
      string q = to_string(t);
      while (q.size() <= CC){
	for (int i=1;i<=2;i++){
	  BigInteger qq = tb(char(i+'0')+q+char(i+'0'));
	  if (is_palindrome(qq*qq))
	    st.insert(qq);
	}
	if (q == string(q.size(),'0'))
	  q += '0';
	else
	  q = "0"+q+"0";
      }
    }
  }
  sort(all.begin(),all.end());
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    string X,Y;
    cin>>X>>Y;
    BigInteger x = tb(X),y = tb(Y);
    cout<<"Case #"<<ccount<<": "<<lower_bound(all.begin(),all.end(),y+1)-lower_bound(all.begin(),all.end(),x)<<endl;
  }
}
