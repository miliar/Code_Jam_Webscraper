#include<iostream>
using namespace std;
int getbits(long long int n) {
 int val = 0;
 while(1) {
  int dig = n%10;
  val = (val | (1<<dig));
  n /= 10;
  if(n==0) break;
 }
 return val;
}
int goal = 1023;
int main() {
  int t;
  cin>>t;
 int kase=0;
  while(t--) {
     kase++;
     int i;
     cin>>i;
     if (i==0)
     {
         cout<<"Case #"<<kase<<": INSOMNIA\n";
         continue;
     }
     int cur = 0;
     long long int cnt = 1;
     while(1) {
       cur |= getbits(cnt*i);
       if(cur==goal)
           break;
       cnt++;
     }
     cout<<"Case #"<<kase<<": "<<cnt*i<<endl;
  }

  return 0;
}
