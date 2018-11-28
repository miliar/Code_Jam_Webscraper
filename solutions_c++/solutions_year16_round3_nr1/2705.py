#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int max(vector<int> V, int no_i)
 {
  int in = 0,max = -1;
  
  for(int i = 0; i < V.size(); i++) if(i != no_i) if(V[i]>max) { max = V[i]; in = i; };
  return in;
 }

int sum(vector<int> V)
 {
  int s = 0;
  
  for(int i = 0; i < V.size(); i++) s+=V[i];
  return s;
 }
 
int check(vector<int> V, int m1, int m2)
 {
  vector<int> T(V.size());
  int s;
  
  T = V;
  T[m1]--;
  T[m2]--;
  s = sum(T);
  if(s == 0) return 1;
  for(int k=0;k<T.size();k++) if((float)T[k]/s > 0.5) return 0;
  return 1;
 }

void evaquate(vector<int> V)
 {
  int i, m1, m2;

  while(sum(V) > 0)
   {
    m1 = max(V,-1);
    m2 = max(V,m1);
    if(check(V,m1,m2) == 0) m2 = max(V,-1);
    if(check(V,m1,m2) == 0) m2 = -1;
    if(m2 != -1) cout << (char)(65 + m1) << (char) (65 + m2) << " ";
    else         cout << (char)(65 + m1) << " ";
    V[m1]--;
    if(m2 != -1) V[m2]--;
   }
  cout << "\n";
 }

int main()
 {
  int n,p;

  cin >> n;
  for(int i = 0; i < n; i++)
   {
	cin >> p;

	vector<int> V(p);
	for(int j = 0; j < p; j++) cin >> V[j];
	cout << "Case #" << i+1 << ": ";
	evaquate(V);
   }
  return 0;
 }
