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
#define int long long


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

const int P = 1000002013;

int n;

int cal(int s,int t){

  int q = t-s;
  return(((n*q)%P-((q*(q-1))/2)%P+P)%P);

}

#undef int
int main(){
#define int long long
  ios_base::sync_with_stdio(false) ;
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    int m;
    cin>>n>>m;
    int total = 0;
    vector<Pair> points;
    for (int i=1;i<=m;i++){
      int x,y,z;
      cin>>x>>y>>z;
      total = (total+z*cal(x,y))%P;
      points.push_back(Pair(x,-z));
      points.push_back(Pair(y,z));
    }
    sort(points.begin(),points.end());
    int best = 0;
    map<int,int> lst;
    for (int i=0;i<points.size();i++)
      if (points[i].second < 0)
	lst[-points[i].first]+=-points[i].second;
      else{
	int rem = points[i].second;
	while (rem > 0){
	  int a = min(rem,lst.begin()->second);
	  lst.begin()->second -= a;
	  best += (a*cal(-((lst.begin())->first),points[i].first))%P;
	  best %= P;
	  if (lst.begin()->second == 0)
	    lst.erase(lst.begin());
	  rem -= a;
	}
      }
    cout<<"Case #"<<ccount<<": "<<(total+P-best)%P<<endl;
  }
}
