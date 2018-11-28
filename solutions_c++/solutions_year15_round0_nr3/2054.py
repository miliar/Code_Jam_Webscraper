//Aleksander Łukasiewicz
#include<iostream>
#include<string>
using namespace std;

int t;
pair<int,char> tab[300][300];

void Prepare(){
  tab['1']['1'] = make_pair(1,'1'); tab['1']['i'] = make_pair(1,'i'); tab['1']['j'] = make_pair(1,'j'); tab['1']['k'] = make_pair(1,'k');
  tab['i']['1'] = make_pair(1,'i'); tab['i']['i'] = make_pair(-1,'1'); tab['i']['j'] = make_pair(1,'k'); tab['i']['k'] = make_pair(-1,'j');
  tab['j']['1'] = make_pair(1,'j'); tab['j']['i'] = make_pair(-1,'k'); tab['j']['j'] = make_pair(-1,'1'); tab['j']['k'] = make_pair(1,'i');
  tab['k']['1'] = make_pair(1,'k'); tab['k']['i'] = make_pair(1,'j'); tab['k']['j'] = make_pair(-1,'i'); tab['k']['k'] = make_pair(-1,'1');
}

bool Solve(string Q){
  pair<int,char> exp = make_pair(1, '1');
  for(int i=0; i<Q.size(); i++){
    pair<int, char> tmp = tab[ (int)exp.second ][ (int)Q[i] ];
    exp = make_pair(exp.first*tmp.first, tmp.second);
  }
  
  if(exp.first != -1 || exp.second != '1')
    return false;
  
  exp = make_pair(1, '1');
  bool checkI = false;
  for(int i=0; i<Q.size(); i++){
    pair<int, char> tmp = tab[ (int)exp.second ][ (int)Q[i] ];
    exp = make_pair(exp.first*tmp.first, tmp.second);
    if(checkI == false && exp.first == 1 && exp.second == 'i')
      checkI = true, exp = make_pair(1, '1');
    if(checkI == true && exp.first == 1 && exp.second == 'j')
      return true;
  }
  
  return false;
}

int main(){
  Prepare();
  cin>>t;
  for(int cs=1; cs<=t; cs++){
    string W;
    int L, X;
    cin>>L>>X;
    cin>>W;
    string Quaternion = "";
    for(int i=0; i<X; i++)
      Quaternion += W;
    
    cout<<"Case #"<<cs<<": "<<(Solve(Quaternion) ? "YES" : "NO")<<'\n';
  }

return 0;
}