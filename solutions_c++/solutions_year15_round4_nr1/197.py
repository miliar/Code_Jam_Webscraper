#include<iostream>

using namespace std;

char g[100][100];
int R,C;

bool out(int y,int x,int d){
  static const int dy[]={-1,0,1,0};
  static const int dx[]={0,1,0,-1};
  for(;;){
    y+=dy[d];
    x+=dx[d];
    if(y<0||R<=y||x<0||C<=x)return true;
    if(g[y][x]!='.')return false;
  }
}

int main(){
  int T;
  cin>>T;
  for(int c=1;c<=T;c++){
    cin>>R>>C;
    for(int i=0;i<R;i++){
      cin>>g[i];
    }
    int ans=0;
    bool f=false;
    for(int i=0;i<R;i++){
      for(int j=0;j<C;j++){
	if(g[i][j]!='.'){
	  char c=g[i][j];
	  int d=(c=='^')?0
	    :(c=='>')?1
	    :(c=='v')?2:3;
	  if(out(i,j,d)){
	    bool od=false;
	    for(int k=0;k<4;k++){
	      od|=!out(i,j,k);
	    }
	    if(!od){
	      f=true;
	    }else{
	      ans++;
	    }
	  }
	}
      }
    }
    cout<<"Case #"<<c<<": ";
    if(f){
      cout<<"IMPOSSIBLE"<<endl;
    }else{
      cout<<ans<<endl;
    }
  }
}

		    
    
