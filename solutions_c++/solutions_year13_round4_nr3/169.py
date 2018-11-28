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

const int MAX_N = 2000+20;
bool e[MAX_N][MAX_N];
vector<int> glo;
bool mark[MAX_N];
int n,a[MAX_N],b[MAX_N],deg[MAX_N],res[MAX_N];
bool reach[MAX_N][MAX_N];

vector<int> s(vector<int> a){
  vector<int> res(a.size(),1);
  for (int i=a.size()-1;i>=0;i--)
    for (int j=i+1;j<a.size();j++)
      if (a[i] >= a[j])
	res[i] = max(res[i],res[j]+1);
  return(res);
}


vector<int> f(vector<int> a){
  vector<int> res(a.size(),1);
  for (int i=0;i<a.size();i++)
    for (int j=0;j<i;j++)
      if (a[i] > a[j])
	res[i] = max(res[i],res[j]+1);
  return(res);
}


int main(){
  ios_base::sync_with_stdio(false) ;
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    cin>>n;
    for (int i=1;i<=n;i++)
      mark[i] = false;
    for (int i=1;i<=n;i++)
      for (int j=1;j<=n;j++)
	e[i][j] = false;
    for (int i=1;i<=n;i++)
      cin>>a[i];
    for (int i=1;i<=n;i++)
      cin>>b[i];
    vector<int> first,second;
    for (int i=1;i<=n;i++)
      first.push_back(a[i]);
    for (int i=1;i<=n;i++)
      second.push_back(b[i]);
    for (int i=1;i<=n;i++)
      for (int j=i+1;j<=n;j++){
	if (a[i] >= a[j]){ // j is not uptade from i then jth number is less than ith number
	  //cout<<i<<' '<<j<<" first issue"<<endl;
	  e[i][j] = true;
	}
	if (b[j] >= b[i]){ // i is not uptade from j then ith number is less than jth number
	  //cout<<i<<' '<<j<<" second issue"<<endl;
	  e[j][i] = true;
	}
      }

    
    
    for (int i=1;i<=n;i++)
      for (int j=1;j<=n;j++)
	for (int k=1;k<=n;k++)
	  if (e[j][i] && e[i][k])
	    e[j][k] = true;

    
    for (int i=1;i<=n;i++) if (b[i] != 1){
      bool bad = true;
      for (int j=i+1;j<=n;j++)
	if (b[i] == b[j] + 1 && e[i][j])
	  bad = false;
      if (bad){
	int first = i+1;
	while (first <= n && (b[i] != b[first]+1 || e[first][i]))
	  first++;
	assert(first <= n);
	assert(b[i] == b[first]+1);
	assert(e[first][i] == 0);
	if (first > n){
	  cerr<<"bad bakht shodim "<<first<<endl;
	}else{
	  cerr<<"here "<<i<<' '<<first<<' '<<n<<endl;
	  e[i][first] = true;
	  for (int k=1;k<=n;k++)
	    if (e[first][k])
	      e[i][k] =true;

	}
      }
	
    }
    
    
    /*
    for (int i=1;i<=n;i++)
      for (int j=i+1;j<=n;j++)
	if (!e[i][j]){
	  e[j][i] = true;
	  for (int k=1;k<=n;k++)
	    if (e[i][k])
	      e[j][k] = true;
	}
    */
    for (int i=1;i<=n;i++)
      for (int j=1;j<=n;j++)
	if (e[i][j])
	  deg[i]++;

    

    vector<int> res(n+1);
    int count = 0;
    while (count < n){
      int start =1;
      while (mark[start] || deg[start])
	start++;
      int last = n;
      while (mark[last] || deg[last])
	last--;
      /*
      if (start != last)
	cerr<<"bad hi"<<endl;
      */
      count++;
      res[start] = count;
      mark[start] = true;
      for (int i=1;i<=n;i++)
	if (e[i][start])
	  deg[i]--;
    }
    cout<<"Case #"<<ccount<<": ";
    for (int i=1;i<=n;i++)
      cout<<res[i]<<' ';
    cout<<endl;
    vector<int> r;
    for (int i=1;i<=n;i++)
      r.push_back(res[i]);
    if (s(r) != second){
      cerr<<n<<endl;
      cerr<<second<<endl;
      cerr<<s(r)<<endl;
      cerr<<endl;
    }
  }
}
