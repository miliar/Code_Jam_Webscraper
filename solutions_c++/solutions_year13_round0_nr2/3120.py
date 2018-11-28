#include<iostream>
using namespace std;


class A{
private:
  int x,y;
  int map[110][110];
public:
  A(){};
  void input(){
    cin>>x>>y;
    for(int i=0;i<x;i++){
      for(int j=0;j<y;j++){
        cin>>map[i][j];
      }
    }
  }

  bool able_cut(int nx,int ny){
    int h=map[nx][ny];
    bool res_x=true;
    bool res_y=true;
    for(int i=0;i<x;i++){
      if( map[i][ny]>h && i!=nx ){
        res_x=false;
      }
    }
    for(int i=0;i<y;i++){
      if( map[nx][i]>h && i!=ny ){
        res_y=false;
      }
    }
    //cout<<nx<<" "<<ny<<" "<<h<<" "<<(res_x||res_y)<<endl;
    return (res_x || res_y);
  }

  string solve(){
    for(int i=0;i<x;i++){
      for(int j=0;j<y;j++){
        if(!able_cut(i,j)){
	  return "NO";
	}
      }
    }
    return "YES";
  }
};

int main(){
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    A a;
    a.input();
    cout<<"Case #"<<i+1<<": "<<a.solve()<<endl;
  }
}
