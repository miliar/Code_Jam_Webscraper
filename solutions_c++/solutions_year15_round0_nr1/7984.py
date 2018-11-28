#include <iostream>
#include <string>

using namespace std;

int main(){

  int t;
  cin>>t;

  for(int index=1;index<=t;index++){
    int n;
    string s;
    char c;
    cin>>n>>s;
    int count=0;
    int total=0;
    for(int i=0;i<=n;i++){
      if(count<i)
	count=i;
      count+=s[i]-'0';
      total+=s[i]-'0';
    }
    cout<<"Case #"<<index<<": "<<count-total<<endl;
  }
}
