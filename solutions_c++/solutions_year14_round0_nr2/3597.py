#include<iostream>
#include<iomanip>

using namespace std;

int main(){
  int t,ct=1; double cur,ans1,ans,c,f,x;
  cin>>t;
  while(t>=ct){
    cin>>c>>f>>x;
    ans = x/2;
    ans1 = (c/2) + x/(2+f);
    cur = 2+f;
    while(ans > ans1){
      ans = ans1;
      ans1 -= (x/cur);
      ans1 += (c/cur);
      cur+=f;
      ans1 += (x/cur);
    }
    std::cout << std::setprecision(15) <<"Case #"<<ct<<": "<<ans<<endl;
    ct++;
  }
  return 0;
}