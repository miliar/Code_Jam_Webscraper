#include<iostream>
#include<cstring>
#include<map>
using namespace std;

int main(){
  int T;
  string ans;

  cin>>T;
  for(int i=1;i<=T;i++){
    int L,X;
    string s;
    cin>>L>>X;
    cin>>s;
    int count = 0;
    char result = '1';
    int minus = 0;
    for(int j = 0;j < L * X;j++){
      
      if (result == '1') result = s[j%L];
      else if(result == s[j%L]){minus++;result='1';}
      else if(result == 'i' && s[j%L] == 'j') result = 'k';
      else if(result == 'j' && s[j%L] == 'k') result = 'i';
      else if(result == 'k' && s[j%L] == 'i') result = 'j';      
      else if(result == 'j' && s[j%L] == 'i'){minus++; result = 'k';}
      else if(result == 'k' && s[j%L] == 'j'){minus++; result = 'i';}
      else if(result == 'i' && s[j%L] == 'k'){minus++; result = 'j';}

      if (result  == ('i' + count)){
        count++;
        result = '1';
      }
    }

    if (count == 3 && minus % 2 == 0 && result == '1') ans = "YES";
    else ans = "NO";
    cout<<"Case #"<<i<<": "<<ans<<endl;
  }
  return 0;
}
