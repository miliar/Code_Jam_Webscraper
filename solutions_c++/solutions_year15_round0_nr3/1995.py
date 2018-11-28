#include <iostream>
#include <fstream>
#include <string>
using namespace std;

char ml[256][256];
int t,n,x,sign[256][256];
string s,is;

int main() {
  ifstream f("input.txt");
  ofstream g("output.txt");
  ml['1']['1']='1'; sign[1][1]=1;
  sign['i']['j']=sign['j']['i']=1;
  sign['i']['k']=sign['k']['i']=1;
  sign['k']['j']=sign['j']['k']=1;
  for(char c='i'; c<='k'; ++c) {
    ml['1'][c]=ml[c]['1']=c;
    sign['1'][c]=sign[c]['1']=1;
    ml[c][c]='1'; sign[c][c]=-1;
  }

  sign['i']['k']=sign['j']['i']=sign['k']['j']=-1;
  ml['i']['j']=ml['j']['i']='k';
  ml['i']['k']=ml['k']['i']='j';
  ml['k']['j']=ml['j']['k']='i';
  f>>t;
  for(int T=1; T<=t; ++T) {
    f>>n>>x>>is;
    x=min(x,x%4+8);
    s="";
    for(int i=1; i<=x; ++i) s+=is;

    char ft='1'; int sc=1;
    int hi=0,hk=0;
    for(int i=0; i<s.size(); ++i) {
      sc*=sign[ft][s[i]];
      ft=ml[ft][s[i]];
      if(ft=='i') hi=1;
      if(ft=='k' && hi) hk=1;
      
    }
    //cout<<s<<'\n';
    //if(T==86) cout<<ft<<' '<<sc<<'\n';
    g<<"Case #"<<T<<": ";
    if(ft=='1' && sc==-1 && hk) g<<"YES";
    else g<<"NO";
    g<<"\n";
  }
}