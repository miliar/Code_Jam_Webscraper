#include<iostream>
#include<vector>
#include<algorithm>
#include<iomanip>
#include<queue>
#include<set>
#include<map>
#include<cmath>


using namespace std;

int R, C;

vector<int> dx, dy;
vector<vector<int> > B, A;

int main(){
  dx=vector<int>(4,0);
  dy=dx;
  dx[0]=1;
  dx[2]=-1;
  dy[1]=1;
  dy[3]=-1;
  int T; cin>>T;
  for (int tc=1; tc<=T; ++tc){
    cin>>R>>C;
    B=vector<vector<int> >(R, vector<int>(C,0));
    string s;
    for (int i=0; i<R; ++i){
      cin>>s;
      for (int j=0; j<C; ++j){
	if (s[j]=='.')
	  B[i][j]=-1;
	if (s[j]=='^')
	  B[i][j]=3;
	if (s[j]=='<')
	  B[i][j]=2;
	if (s[j]=='v')
	  B[i][j]=1;
      }
    }
    int ans=0;
    bool god=1;
    for (int i=0; i<R; ++i)
      for (int j=0; j<C; ++j){
	if (B[i][j]==-1)
	  continue;
	int h=B[i][j];
	int k=i; int l=j;
	bool ja=0;
	while(1){
	  k+=dy[h];
	  l+=dx[h];
	  if (!(k>-1 && k<R && l>-1 && l<C))
	    break;
	  if (B[k][l]!=-1){
	    ja=1;
	    break;
	  }
	}
	if (ja)
	  continue;
	for (h=0; h<4; ++h){
	  k=i; l=j;
	  while(1){
	    k+=dy[h];
	    l+=dx[h];
	    if (!(k>-1 && k<R && l>-1 && l<C))
	      break;
	    if (B[k][l]!=-1){
	      ja=1;
	      break;
	    }
	  }
	}
	if (ja)
	  ++ans;
	else
	  god=0;
      }
    cout<<"Case #"<<tc<<": ";
    if (!god)
      cout<<"IMPOSSIBLE\n";
    else
      cout<<ans<<endl;

  }
  return 0;
}
