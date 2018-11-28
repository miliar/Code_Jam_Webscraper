
#include <bits/stdc++.h>
using namespace std;

int main() {

freopen("D-small-attempt1.in", "r", stdin);
  freopen("D-small-attempt1.out", "w", stdout);
  int xrc[5][5][5];
  memset(xrc,0,sizeof(xrc));
  for(int i=1;i<=4;i++)
    for(int j=1;j<=4;j++)
      xrc[1][i][j]=1;


  xrc[2][1][2]=1;
  xrc[2][2][1]=1;
  xrc[2][1][4]=1;
  xrc[2][4][1]=1;
  xrc[2][2][2]=1;
  xrc[2][4][4]=1;
  xrc[2][2][4]=1;
  xrc[2][4][2]=1;
  xrc[2][3][2]=1;
  xrc[2][2][3]=1;
  xrc[2][3][4]=1;
  xrc[2][4][3]=1;

  xrc[3][2][3]=1;
  xrc[3][3][2]=1;
  xrc[3][4][3]=1;
  xrc[3][3][4]=1;
  xrc[3][3][3]=1;
  xrc[4][4][4]=1;
  xrc[4][3][4]=1;
  xrc[4][4][3]=1;

	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		string ans;
		int x,r,c;
		cin>>x>>r>>c;
		if(xrc[x][r][c]==1)
		  ans="GABRIEL";
    else ans="RICHARD";
		cout<<"Case #"<<j<<": "<<ans<<endl;

	}
	return 0;
}

