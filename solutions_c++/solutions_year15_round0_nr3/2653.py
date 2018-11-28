
#include <bits/stdc++.h>
using namespace std;

int main() {

	freopen("C-small-attempt0.in", "r", stdin);
  freopen("C-small-attempt0.out", "w", stdout);
  int inf[5][5];
  inf[1][1]=1;
  inf[1][2]=2;
  inf[1][3]=3;
  inf[1][4]=4;
  inf[2][1]=2;
  inf[2][2]=-1;
  inf[2][3]=4;
  inf[2][4]=-3;
  inf[3][1]=3;
  inf[3][2]=-4;
  inf[3][3]=-1;
  inf[3][4]=2;
  inf[4][1]=4;
  inf[4][2]=3;
  inf[4][3]=-2;
  inf[4][4]=-1;
	int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		int l,x,i;
		cin>>l>>x;
		string s,ans,s1;
		cin>>s;

		for(i=1;i<=x;i++)
		  s1+=s;

    int g=1,fl1=0,fl2=0;
    for(i=0;i<(l*x);i++){

        if(g==2){
            fl1=1;
            break;
        }
        int tmp;
        if(s1[i]=='i')
          tmp=2;
        if(s1[i]=='j')
          tmp=3;
        if(s1[i]=='k')
          tmp=4;
        if(g<0){
            g=(-1)*inf[-g][tmp];
        }
        else g=inf[g][tmp];


    }
    if(fl1==1){
        g=1;

        for(;i<(l*x);i++){
        if(g==3){
            fl2=1;
            break;
        }
        int tmp;
        if(s1[i]=='i')
          tmp=2;
        if(s1[i]=='j')
          tmp=3;
        if(s1[i]=='k')
          tmp=4;
        if(g<0){
            g=(-1)*inf[-g][tmp];
        }
        else g=inf[g][tmp];


    }
        if(fl2==1){
             g=1;
        for(;i<(l*x);i++){

        int tmp;
        if(s1[i]=='i')
          tmp=2;
        if(s1[i]=='j')
          tmp=3;
        if(s1[i]=='k')
          tmp=4;
        if(g<0){
            g=(-1)*inf[-g][tmp];
        }
        else g=inf[g][tmp];


    }
        if(g==4)
          ans="YES";
        else ans="NO";
        }
        else ans="NO";
    }
    else ans="NO";
		cout<<"Case #"<<j<<": "<<ans<<endl;

	}
	return 0;
}

