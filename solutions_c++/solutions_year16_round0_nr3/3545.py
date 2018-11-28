#include <iostream>
#include <vector>
using namespace std;
long long int f(long long int n, long long int m){
  long long int i = 0;
  while(n>>i)i++;
  long long int res = 0;
  while(i--){
    res*=m;
    res += ((n>>i)&1);
  }
  return res;
}

long long int g(long long int n){
  if(!(n&1))return 2;
  for(long long int i = 3;i*i<=n;i+=2){
    if(n%i==0)return i;
  }
  return 0;
}
void printb(long long int n ){
  long long int i = 0;
  while(n>>i)i++;
  while(i--){
    cout<<((n>>i)&1);
  }
}

void printv(vector<long long int> v){
  for(long long int i = 0;i<v.size();i++){
    cout<<v[i]<<" ";
  }
}
int c(const long long int n){
  vector<long long int> v;
  for(long long int i = 2;i<=10;i++){
    long long int m=f(n, i);
    //    cout<<"m = "<<m<<endl;
    long long int l=g(m);
    //    cout<<"l = "<<l<<endl;
    if(l)v.push_back(l);
    else return 0;
  }
  //  cout<<n<<endl;
  printb(n);
  cout<<" ";
  printv(v);
  cout<<endl;
  return 1;
}
    
int main(void){
  long long int T;
  long long int N, J;
  cin>>T;
  cin>>N>>J;
  cout<<"Case #1:"<<endl;
  long long int i = (1<<N-1)+1;
  long long int m = (1<<N)-1;
  //  cout<< i <<endl;
  //  cout<<m<<endl;

  for(;i<=m&&J;i+=2){
    J-=c(i);
  }


  return 0;
}
