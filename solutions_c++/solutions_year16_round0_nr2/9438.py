#include <bits/stdc++.h>

using namespace std;

int main(){

    int n;

    cin>>n;

    for(int i = 1;i<=n;i++){
    string s;

    cin>>s;

    int v[s.size()];

    for(int j = 0; j<s.size();j++){
        if(s[j] == '+'){
           v[j] = 1;

        }else{
        v[j] = -1;
        }
    }


  int o = 0;
int soma = 0;
// while(o < s.size()){
  //  o=0;
    for(int j = 0;j<s.size() -1;++j){
        if(v[j] != v[j+1]){
            soma++;
            //int u[j+1];
           // for(int z = 0;z<j+1;++z){
           // u[z] = v[s.size()- j - z - 1] * (-1);

          //  }
          //  for(int z = 0;z<j+1;++z){
            //v[j] = v[j]*(-1);
            //}
        }
    }

    if(v[s.size() -1] == -1){
    cout<<"Case #"<<i<<": "<<soma+1<<endl;
    }else{
    cout<<"Case #"<<i<<": "<<soma<<endl;
    }

    //for(int j = 0;j<s.size();++j)
      //  o += v[j];


 }
return 0;
    }


