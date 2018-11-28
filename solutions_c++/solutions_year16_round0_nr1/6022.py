#include<iostream>

using namespace std;

bool came[10];

void process(long n) {
  while(n>0) {
    came[n%10] = true;
    n = n/10;
  }
}

bool finished() {
  for(int i=0; i<10; i++) {
    if(!came[i])
      return false;
  }
  return true;
}

int main() {
  int T, n, t;
  cin>>T;
  t = 1;
  while(t<=T) {
    for(int i=0; i<10; i++)
      came[i] = false;
    cin>>n;
    if(n==0)
      cout<<"Case #"<<t<<": INSOMNIA"<<endl;
    else {
      int i = 0;
      while(!finished()) {
        i++;
        process(n*i);
      }
      cout<<"Case #"<<t<<": "<<n*i<<endl;
    }
    t++;
  }
  return 0;
}
