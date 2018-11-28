#include<bits/stdc++.h>

using namespace std;

/**
 * [algo]
 * at each - after first it will
 * be settled in two passes
 * othr wise from start a single pass
 * and if all + no pass
 * @return [description]
 */


int main(){
  int t;
  int _index = 0;
  cin>>t;
  while(t--){
    string s;
    int i,j,k;
    int _start=0,_middle=0;
    int sp=0;
    cin>>s;
    int l = s.length();
    for(i=0;i<l;i++){
      if(s[i] == '-'){
        _start = 1;
          continue;
      }else {
        sp = i;
        break;
      }
    }

    if(i <= l){
      char curr = s[sp];
      //cout<<"Curr:"<<curr<<endl;
      for(i=sp+1;i<l;i++){
        if(s[i] != curr){
          curr = s[i];
          if(s[i] == '-')
          _middle++;
        }
      }
    }

    int ans = _start + (_middle * 2);
    cout<<"Case #"<<(++_index)<<": "<<ans<<endl;
  }

}
