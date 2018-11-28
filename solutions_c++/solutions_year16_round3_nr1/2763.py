#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;

int max(vector<int> vet, int nah)
 {
  int ini = 0,max = -1;
  
  for(int i = 0; i < vet.size(); i++) if(i != nah) if(vet[i]>max) { max = vet[i]; ini = i; };
  return ini;
 }

int sum(vector<int> Vi)
 {
  int s = 0;
  
  for(int i = 0; i < Vi.size(); i++) s+=Vi[i];
  return s;
 }

 
 
int check(vector<int> Va, int m1, int m2)
 {
  vector<int> T(Va.size());
  int s;
  
  T = Va;
  T[m1]--;
  T[m2]--;
  s = sum(T);
  if(s == 0) return 1;
  for(int k=0;k<T.size();k++) if((float)T[k]/s > 0.5) return 0;
  return 1;
 }

void solve(vector<int> Vqq)
 {
  int i, m1, m2;
  int cnt = 0;
  while(sum(Vqq) > 0)
   {
    m1 = max(Vqq,-1);
    m2 = max(Vqq,m1);
    if(check(Vqq,m1,m2) == 0) m2 = max(Vqq,-1);
    if(check(Vqq,m1,m2) == 0) m2 = -1;
    if(m2 != -1) cout << (char)('A' + m1) << (char) ('A' + m2) << " ";
    else         
      cout << (char)('A' + m1) << " ";
    Vqq[m1]--;
    if(m2 != -1)
     Vqq[m2]--;
   }
  cout << "\n";
 }

int main()
 {
  int t,op;

  cin >> t;
  for(int i = 1; i <= t; i++)
   {
	cin >> op;

	vector<int> V(op);
	for(int j = 0; j < op; j++) cin >> V[j];
	cout << "Case #" << i << ": ";
	solve(V);
   }
  return 0;
 }
