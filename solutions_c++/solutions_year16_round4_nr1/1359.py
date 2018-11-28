/* Brian's GCJ entries */
#include <vector>
#include <iterator>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <cmath>
#include <set>
#include <queue>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <chrono>
using namespace std;
int bitct(long long r) {return r == 0 ? 0 : (bitct(r>>1) + (r&1));}
long long gcd(long long x, long long y) {return x ? gcd(y%x,x) : y;}
long long choose(long long n, long long q) { if(n==0 || q==0) return 1;
	if (q==1) return n; else return ( choose(n, q-1) * (n-q+1 ) /q); }
template<typename T> ostream& operator << (ostream &o,vector<T> v) {o<<"[";
	int i=0,s=v.size();for(;i+1<s;i++)o<<v[i]<<", ";if(s)o<<v[i];o<<"]";return o;}
template<typename K, typename V> ostream& operator << (ostream &o,
  unordered_map<K, V> m) {o<<"h{";for(auto i:m)o<<i.first<<" -> "<< i.second <<
  ", "; o<<"}";return o;}
template<typename K, typename V> ostream& operator << (ostream &o,
  map<K, V> m) {o<<"{";for(auto i:m)o<<i.first<<" -> "<< i.second <<
  ", "; o<<"}";return o;}
template<typename K, typename V> ostream& operator << (ostream &o,
  set<K> m) {o<<"#{";for(auto i:m)o<<i<< ", "; o<<"}";return o;}
template<typename K, typename V> ostream& operator << (ostream &o,
  unordered_set<K> m) {o<<"#h{";for(auto i:m)o<<i<< ", "; o<<"}";return o;}
//int dx[8] = {0,  1,  1,  1,  0, -1, -1, -1}
//int dy[8] = {1,  1,  0, -1, -1, -1,  0,  1}
int dx[4] = {0,1,0,-1};
int dy[4] = {1,0,-1,0};

void calc(ifstream &, ofstream &);
main() { stringstream filename, fnamein, fnameout;
  typedef std::chrono::duration<int,std::milli> ms;
	string file("A");
	filename << file << "-small.";
	fnamein << filename.str() << "in"; fnameout << filename.str() << "out";
	ifstream fin(fnamein.str().c_str()); ofstream fout(fnameout.str().c_str());
	int count;
	fin >> count;
	for(int i=0;i<count;i++) {
		fout << "Case #" << (i+1) << ": ";
    chrono::steady_clock::time_point t0 = chrono::steady_clock::now();
		calc(fin, fout);
    chrono::steady_clock::time_point t1 = chrono::steady_clock::now();
    cerr << "CASE" << (i+1) << " " << 
      (chrono::duration_cast<ms>(t1-t0)).count() << endl;
		fout.flush(); }
	fin.close(); fout.close(); }

void sortss(string & in, int b, int e)
{
  if(b==e) return ;
  int stride = (e-b+1)/2;
  sortss(in, b, b+stride-1);
  sortss(in, b+stride, e);

  bool ok=true;
  for(int i=0;i<stride;i++)
    {
    if(in[b+i] < in[b+stride+i])
      break;
    if(in[b+i] > in[b+stride+i])
      {
      ok=false;
      break;
      }
    }
  if(!ok)
    for(int i=0;i<stride;i++)
      {
      char tmp=in[b+stride+i];
      in[b+stride+i]=in[b+i];
      in[b+i]=tmp;
      }
}

string db (string & in)
{
  string out;
  for(int i=0;i<in.size();i++)
    {
    if(in[i]=='r')
      out.append("rs");
    if(in[i]=='p')
      out.append("rp");
    if(in[i]=='s')
      out.append("ps");
    }
  return out;
}

void calc(ifstream &fin, ofstream &fout)
	{
  int n, r, p , s;
  fin >> n >> r >> p >> s;

  /*
  int str = (1<<n)/3;
  if(
      (r != str) && (r != str+1) ||
      (p != str) && (p != str+1) ||
      (s != str) && (s != str+1))
    {
    fout << "IMPOSSIBLE" << endl;
    return;
    } 
    */

  string a[3];
  a[0]= "r";
  a[1]="p";
  a[2]="s";
  for(int i=0;i<n;i++)
    for(int j=0;j<3;j++)
      a[j]=db(a[j]);

  string best="zmpossible";
  for(int i=0;i<3;i++)
    {
    sortss(a[i], 0, a[i].size()-1);
    int rs=0, ps=0, ss=0;
    for(int j=0;j<a[i].size();j++)
      {
      if(a[i][j]=='r')
        rs++;
      if(a[i][j]=='p')
        ps++;
      if(a[i][j]=='s')
        ss++;
      }
    if(r!=rs || p!=ps || ss!=s)
      continue;

    if(a[i]<best)
      best=a[i];
    }

  if(best[0]=='z')
    best[0]='i';
  for(int i=0;i<best.size();i++)
    best[i] += 'A'-'a';
    fout << best << endl;

  return; 
	}

