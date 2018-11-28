#include<iostream>
using namespace std;


class A{
private:
long long r,t;
public:
  A(){
  }
  void input(){
    cin>>r>>t;
    r++;
  }
  long long solve(){
    long long ans=0;
    while(t>=0){
      //cout<<t<<" "<<r<<" "<<(r*r-(r-1)*(r-1))<<endl;
      t-=r*r-(r-1)*(r-1);
      if(t>=0)ans++;
      r+=2;
    }
    return ans;
  }
};

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    A a;
    a.input();
    cout<<"Case #"<<i+1<<": "<<a.solve()<<endl;    
  }
}
