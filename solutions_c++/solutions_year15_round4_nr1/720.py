#include <iostream>
using namespace std;

#define MAX 101
int r,c,hmin[MAX],hmax[MAX],vmin[MAX],vmax[MAX];
char s[MAX][MAX];

int main(){
	int t,u,i,j,k,cc,imp;
	cin>>t; for (u=0; u<t; u++){
		cin>>r>>c; for (i=0; i<r; i++) cin>>s[i];
		for (i=0; i<r; i++){ hmin[i]=MAX+1;  hmax[i]=-1;}
		for (i=0; i<c; i++){ vmin[i]=MAX+1;  vmax[i]=-1;}
		for (i=0; i<r; i++) for (j=0; j<c; j++) if (s[i][j]!='.'){
			hmin[i]=min(hmin[i],j);
			hmax[i]=max(hmax[i],j);
			vmin[j]=min(vmin[j],i);
			vmax[j]=max(vmax[j],i);
		}
		for (cc=i=imp=0; i<r; i++) for (j=0; j<c; j++) if (s[i][j]!='.'){
			if (s[i][j]=='>' && hmax[i]>j) ;
			else if (s[i][j]=='<' && hmin[i]<j) ;
			else if (s[i][j]=='^' && vmin[j]<i) ;
			else if (s[i][j]=='v' && vmax[j]>i) ;
			else if (hmin[i]<j || hmax[i]>j || vmin[j]<i || vmax[j]>i) cc++; 
			else imp=1;
		}
		cout<<"Case #"<<(u+1)<<": ";
		if (imp) cout<<"IMPOSSIBLE"<<endl; else cout<<cc<<endl;
	}
	return 0;
}