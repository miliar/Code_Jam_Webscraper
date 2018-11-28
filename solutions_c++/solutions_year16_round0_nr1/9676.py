#include<iostream>
using namespace std;
int main(){
  int t;
  cin>>t;
  int bitmap[10];
  bitmap[0]=1;
  int checkpoint=(1<<10)-1;
  for (int i=1;i!=10;i++) bitmap[i]=bitmap[i-1]<<1;
  for (int i=0; i!=t; i++) {
    long long num;
    cin>>num;
    if (num==0) 
      cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
    else {
      long long flag=0, j=0;
      while (flag!=checkpoint) {
	j++;
	long long tmp=num*j;
	while (tmp) {
	  flag |= bitmap[tmp%10];
	  tmp=tmp/10;
	}
      }
      cout<<"Case #"<<i+1<<": "<<j*num<<endl;
    }
  }
  return 0;
}
