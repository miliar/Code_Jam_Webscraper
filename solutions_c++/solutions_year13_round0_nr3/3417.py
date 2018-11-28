/*
ID: nongeek1
PROG: my
LANG: C++
*/
#include<iostream>
#include<fstream>
#include<cmath>
using namespace std;

ifstream fin("my.in");
ofstream fout("my.out");

long long A,B;

bool check(int n){
  int a[50];
  int len=0;
  while(n){
    a[len++] = n%10;
    n/=10;
  }
  int i,j;
  for(i=0,j=len-1; i<=j; i++,j--){
    if(a[i]!=a[j]) return false;
  }
  return true;
}
void solve(){
  fin>>A>>B;
  int count=0;
  for(int i=sqrt(A-1)+1; i<=sqrt(B); i++)
    if(check(i)&&check(i*i)) {
      count++;
    }
      

  fout << count << endl;
}
int main(){
  int caseN;
  fin >> caseN;
  for(int index=1; index<=caseN; index++){
    fout << "Case #" << index <<": ";    
    solve();
  }
  return 0;
}
