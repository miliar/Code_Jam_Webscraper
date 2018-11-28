#include<iostream>
#include<list>
using namespace std;
int sleepnum(int n){
  int n1=n,n0;
  list<int> to_check;
  for(int i=0;i<10;i++)to_check.push_back(i);
  while(!to_check.empty()){
    n0=n1;
    while(n0!=0){
        if(!to_check.empty())to_check.remove(n0%10);
        n0=n0/10;
    }
    n1 += n;
  }
 return (n1-n);
}
int main()
{
   int T,n;
   cin>>T;
   for(int i=0;i<T;i++){
     cin>>n;
     cout<<"Case #"<<i+1<<": ";
     if(n==0)cout<<"INSOMNIA\n";
     else cout<<sleepnum(n)<<endl;
   }
}
