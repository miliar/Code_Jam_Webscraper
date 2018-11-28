#include <iostream>
using namespace std;

char s[1099];

int main()
{
  int t;
  int len;
  cin>>t;
  for(int tn=1; tn<=t; tn++) {
    cin>>len;
    cin>>s;
    
    int required = 0;
    if(len == 0) {
      cout<<"Case #"<<tn<<": "<<required<<endl;
      continue;
    }
    int standing = 0;
    int temp = 0;
    for(int i=0; i<=len; i++) {
      temp = i - standing;
      if(temp > 0) {
	required += temp;
	standing += temp;
      }
      standing += (int)(s[i]-'0');
    
  }
  
  cout<<"Case #"<<tn<<": "<<required<<endl;
  
  }
  return 0;
}
