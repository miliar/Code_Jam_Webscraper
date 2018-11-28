#include<iostream>
#include<cstring>

using namespace std;

int main()
{
  int a[5][5];
  int b[5][5];
  int fa[17] = {0};
  int fb[17] = {0};
  int one, two;
  int t, z = 1;
  cin>>t;
  while(t--){
    memset(fa, 0, sizeof(fa));
    memset(fb,0,sizeof(fb));
    cin>>one;
    for(int i = 0;i<4;i++){
      for(int j = 0;j<4;j++){
	cin>>a[i][j];
      if(i == one - 1){
	fa[a[i][j]]++;
      }
      }
    }
    cin>>two;
    for(int i = 0;i<4;i++){
      for(int j = 0;j<4;j++){
	cin>>b[i][j];
	if(i == two - 1){
	  fb[b[i][j]]++;
	}
      }
    }
    int c = 0;
    int ans;
    for(int i = 0;i<17;i++){
      if(fa[i] && fb[i]){
	c++;
	ans = i;
      }
    }
    cout<<"Case #"<<z<<": ";
    if(c == 1){
      cout<<ans<<endl;
    }
    else if(c == 0){
      cout<<"Volunteer cheated!"<<endl;
    }
    else{
      cout<<"Bad magician!\n";
    }
    z++;
  }
}