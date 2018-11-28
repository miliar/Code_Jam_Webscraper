#include<bits/stdc++.h>
using namespace std;

int dy[]={-1,0,1,0};
int dx[]={0,1,0,-1};

int H,W;
char t[105][105];
int a[105],b[105];




void init(){
  for(int i=0;i<105;i++){
    a[i]=b[i]=0;
  }
}

int main(){
  int Tc;
  cin>>Tc;
  for(int tc=1;tc<=Tc;tc++){
    init();
    cin>>H>>W;
    for(int i=0;i<H;i++){
      for(int j=0;j<W;j++){
	cin>>t[i][j];
	if(t[i][j]=='.')continue;
	a[i]++;
	b[j]++;
      }
    }

    bool flg=true;
    int sum=0;
    for(int i=0;i<H;i++){
      for(int j=0;j<W;j++){
	if(t[i][j]=='.')continue;

	if(a[i]==1&&b[j]==1)flg=false;
	int y=i,x=j;
	int dir;
	if(t[i][j]=='^')dir=0;
	else if(t[i][j]=='>')dir=1;
	else if(t[i][j]=='v')dir=2;
	else dir=3;
	bool f=false;
	for(int k=0;;k++){
	  y+=dy[dir];x+=dx[dir];
	  if(y<0||x<0)break;
	  if(y>=H||x>=W)break;
	  if(t[y][x]!='.')f=true;
	}
	if(!f)sum++;
	
      }
    }
    
    cout<<"Case #"<<tc<<": ";
    if(flg){
      cout<<sum<<endl;
    }else{
      cout<<"IMPOSSIBLE"<<endl;
    }
  }
  return 0;
}
