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

 
 
int check(vector<int> Vay, int m1, int m2)
 {
  vector<int> T(Vay.size());
  int w;
  
  T = Vay;
  T[m1]--;
  T[m2]--;
  w = sum(T);
  if(w == 0) return 1;
  for(int h=0;h<T.size();h++) if((float)T[h]/w > 0.5) return 0;
  return 1;
 }

void solve(vector<int> arr)
 {
  int i, n1, m2;
  int cnt = 0;
  while(sum(arr) > 0)
   {
    n1 = max(arr,-1);
    m2 = max(arr,n1);
    if(check(arr,n1,m2) == 0) m2 = max(arr,-1);
    if(check(arr,n1,m2) == 0) m2 = -1;
    if(m2 != -1) cout << (char)('A' + n1) << (char) ('A' + m2) << " ";
    else         
      cout << (char)('A' + n1) << " ";
    arr[n1]--;
    if(m2 != -1)
     arr[m2]--;
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
