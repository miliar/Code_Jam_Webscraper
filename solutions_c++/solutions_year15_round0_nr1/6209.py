#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main(){
  int t;
  cin >> t;
  for(int test=1;test<=t;test++){
    int smax;
    cin >> smax;
    string s;
    cin >> s;
    int standing=s[0]-'0';
    int count=0;
    for(int i=1;i<s.size();i++){
      if(standing<i){
	count+=(i-standing);
	standing=standing+(s[i]-'0')+i-standing;
      }
      else{
	standing+=(s[i]-'0');
      }
    }
    cout << "Case #" << test << ": " << count << endl;
  }
  return 0;
}