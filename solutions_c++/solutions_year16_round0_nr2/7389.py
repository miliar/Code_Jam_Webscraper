#include<bits/stdc++.h>

using namespace std;

int main(){
  int t;
  int _index = 0;
  cin>>t;
  while(t--){
    string s;
    int i,j,k;
    int _start=0,_middle=0,_end=0;
    int sp=0;
    cin>>s;
    int l = s.length();
  //  cout<<"Lngth :"<<l<<endl;
    //is minues n start
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
      //count toggle from + to -
      //definitely s[sp] will be +
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

    //cout<<_start<<endl;
    //cout<<_middle<<endl;
    int ans = _start + (_middle * 2);
    cout<<"Case #"<<(++_index)<<": "<<ans<<endl;
  }

}
