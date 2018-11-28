#ifndef COMP_H_
#define COMP_H_

// compile with g++ -std=c++11 filename.c++


#include<algorithm>
#include<sstream>
#include<iostream>
#include<string>
#include<limits>
#include<vector>
#include<map>
#include<set>
#include<queue>

using namespace std;

#define __STRA__(x) #x
#define __STRB__(x) __STRA__(x)
#define __BNAME__ string(string(__FILE__).c_str()+string(__FILE__).find_last_of("/\\")+1)
#define __LOC__ __BNAME__+string(":")+__STRB__(__LINE__)

// Location
#define lcn __LOC__+" : "
#define lcnh() clog << "here:" << __LOC__ << endl
#define lcnv(v) clog << "here: " << __LOC__ << " " << #v << ":\"" << v << "\"" << endl
#define lcne() clog << "here:" << __LOC__ << "[e]" << endl << endl


// Why do I need this?
inline string (tostr)(){
  return "";
}
template <typename T, typename... Args>
inline string (tostr)(T arg, Args... args)
{
  return string(arg)+tostr(args...);
}
#define tochars(...) (tostr)(__LOC__,": ",__VA_ARGS__).c_str()


// Exception
#define exc() runtime_error( string(__LOC__)+" "+"error found")


// display a vector
template <typename T>
inline ostream & operator<<(ostream & os, const vector<T> & v){
  const size_t n = v.size();
  for(int i = 0; i < n; i++){
    if (i > 0 ) os << ", ";
    os << v[i];
  }
  return os;
}

// display a map
template <typename K, typename V>
inline ostream & operator<<(ostream & os, const map<K,V> & v){
  const size_t n = v.size();
  int i = 0;
  for(typename map<K,V>::const_iterator it = v.begin(); it != v.end(); it++ ){
    if (i++ > 0 ) os << ", ";
    os << "(" << it->first << ", " << it->second << ")";
  }
  return os;
}


namespace op {
  istringstream getline(istream & cin){
    istringstream iss;
    string line;
    getline(cin,line);
    iss.str( line );
    iss.clear();
    return iss;
  }
  template <typename T>
  vector<T> getelems(istream &cin, int n){
    vector<T> v;
    v.reserve(n);
    for(int i = 0; i < n; i++){
      T k;
      cin >> k;
      v.push_back(k);
    }
    return {v};
  }
}

#endif
