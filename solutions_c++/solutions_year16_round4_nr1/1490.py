#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
#define lint unsigned long long int

class sol{
public:
  int N,R,P,S;
  int NN=1;
  string bst;

  char win(char a, char b){
    if(a=='R' && b=='S'){
      return a;
    }
    if(a=='P' && b=='R'){
      return a;
    }
    if(a=='S' && b=='P'){
      return a;
    }
    return b;
  }

  bool check(string cur){
    if(cur.size()==1)
      return true;
    string tmp;
    for(int i=0;i<cur.size();i+=2){
      if(cur[i]==cur[i+1])
	return false;
      tmp.push_back(win(cur[i],cur[i+1]));
    }
    return check(tmp);
  }

  bool recurse(string cur, int i, int r, int p, int s){
    if(i==NN){
      if(r!=0 || p!=0 || s!=0)
	return false;
      if(check(cur)){
	bst = cur;
	return true;
      }else{
	return false;
      }
    }else{
      if(p>0){
	if(recurse(cur+"P",i+1,r,p-1,s)){
	  return true;
	}
      }
      if(r>0){
	if(recurse(cur+"R",i+1,r-1,p,s)){
	  return true;
	}
      }
      if(s>0){
	if(recurse(cur+"S",i+1,r,p,s-1)){
	  return true;
	}
      }
      return false;
    }    
  }


  string solve(){
    cin>>N>>R>>P>>S;
    for(int i=0;i<N;i++)
      NN*=2;
    assert(NN==R+P+S);
    if(recurse("",0,R,P,S)){
      return bst;
    }else{
      return "IMPOSSIBLE";
    }
  }
  
};




int main(){
  int N;
  cin>>N;
  for(int i=0;i<N;i++){
    // Leggi
    cout<<"Case #"<<i+1<<": "<<sol().solve()<<endl;
  }

  return 0;
}
