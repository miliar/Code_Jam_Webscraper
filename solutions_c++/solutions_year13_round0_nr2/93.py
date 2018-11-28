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

int n,m,num[200][200];
bool e[200][200],row[200],col[200];

int main(){
  ios_base::sync_with_stdio(false) ;
  int ttime;
  cin>>ttime;

  for (int ccount=1;ccount<=ttime;ccount++){
    cin>>n>>m;
    for (int i=1;i<=n;i++)
      for (int j=1;j<=m;j++)
	cin>>num[i][j];
    bool b = false;
    for (int number=1;number<=100;number++){
      for (int i=1;i<=n;i++)
	for (int j=1;j<=m;j++)
	  e[i][j] = (num[i][j] <= number);
      for (int i=1;i<=n;i++)
	row[i] = false;
      for (int i=1;i<=m;i++)
	col[i] = false;

      for (int i=1;i<=n;i++)
	for (int j=1;j<=m;j++)
	  if (!e[i][j])
	    row[i] = col[j] = true;


      /*
      if (number <= 2){
	for (int i=1;i<=n;i++)
	  cout<<row[i]<<' ';
	cout<<endl;
	for (int i=1;i<=m;i++)
	  cout<<col[i]<<' ';
	cout<<endl;
	for (int i=1;i<=n;i++,cout<<endl)
	  for (int j=1;j<=m;j++)
	    cout<<e[i][j]<<' ';
	cout<<"**********"<<endl;
      }
      */
      bool bad = false;
      for (int i=1;i<=n;i++)
	for (int j=1;j<=m;j++)
	  if (e[i][j] && row[i] && col[j])
	    bad = true;
      if (bad)
	b = true;
    }

    if (b)
      cout<<"Case #"<<ccount<<": NO"<<endl;
    else
      cout<<"Case #"<<ccount<<": YES"<<endl;

  }
}
