#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;

int main(){
  int input;
  cin >> input;
  vector<string> ans(input);
  vector<string> s(input);
  for(int i=0;i<input;i++){
    cin >> s[i];
  }
  for(int i=0;i<input;i++){
    map<char,int> cnt;
    int counter[10]={};
    for(auto &it:s[i]){
      cnt[it]++;
    }

    //Zero
    int Z=cnt['Z'];
    counter[0]=Z;
    cnt['Z']-=Z;
    cnt['E']-=Z;
    cnt['R']-=Z;
    cnt['O']-=Z;
    //tWo
    int W=cnt['W'];
    counter[2]+=W;
    cnt['T']-=W;
    cnt['W']-=W;
    cnt['O']-=W;
    //foUr
    int U=cnt['U'];
    counter[4]=U;
    cnt['F']-=U;
    cnt['O']-=U;
    cnt['U']-=U;
    cnt['R']-=U;
    //siX
    int X=cnt['X'];
    counter[6]+=X;
    cnt['S']-=X;
    cnt['I']-=X;
    cnt['X']-=X;
    //eiGht
    int G=cnt['G'];
    counter[8]+=G;
    cnt['E']-=G;
    cnt['I']-=G;
    cnt['G']-=G;
    cnt['H']-=G;
    cnt['T']-=G;
    //Five
    int F=cnt['F'];
    counter[5]=F;
    cnt['F']-=F;
    cnt['I']-=F;
    cnt['V']-=F;
    cnt['E']-=F;
    //One
    int O=cnt['O'];
    counter[1]+=O;
    cnt['O']-=O;
    cnt['N']-=O;
    cnt['E']-=O;
    //Three
    int T=cnt['T'];
    counter[3]+=T;
    cnt['T']-=T;
    cnt['H']-=T;
    cnt['R']-=T;
    cnt['E']-=T;
    cnt['E']-=T;
    //Seven
    int S=cnt['S'];
    counter[7]+=S;
    cnt['S']-=S;
    cnt['E']-=S;
    cnt['V']-=S;
    cnt['E']-=S;
    cnt['N']-=S;
    //NINE
    int I=cnt['I'];
    counter[9]+=I;
    cnt['N']-=I;
    cnt['I']-=I;
    cnt['N']-=I;
    cnt['E']-=I;

    for(int u=0;u<10;u++){
      for(int j=0;j<counter[u];j++){
        ans[i]+='0'+u;
      }
    }
  }
//output
  for(int i=0;i<input;i++){
    cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
  }

}
