#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

int ispalindrome(long long a){
  long long res=0;
  long long a2 = a;
  while(a2){
    res*=10;
    res+=a2%10;
    a2/=10;
  }
  if (res==a)
    return 1;
  return 0;
}

int main(){

  vector<long long> fairsquare;
  for (long long i=1;i<10000000;i++){
    if (ispalindrome(i)){
      if (ispalindrome(i*i)){
	fairsquare.push_back(i*i);
      }
    }
  }
  int T;
  cin>>T;
  for (int t=1;t<=T;t++){
    long long a,b;
    cin>>a>>b;
    int total=0;
    for (int i=0;i<fairsquare.size();i++){
      if (a<=fairsquare[i] && b>=fairsquare[i]){
	total++;
      }
    }
    cout<<"Case #"<<t<<": "<<total<<endl;
  }
}
