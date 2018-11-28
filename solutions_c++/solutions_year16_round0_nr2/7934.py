#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

const int maxn=100000;
int t,n;
int q[maxn],c[maxn][105]; 
char s[105];

void bfs (){
	int i,j,k,h,t,ans=1,pre,tail;
	//strcpy(c[1],s,sizeof (s));
	for (i=0;i<n;i++)if (c[1][i]==1)break;
	if (i==n){cout<<0<<endl;return ;}
	tail=1;
	for (h=0,t=1;h!=t;){
		h=h+1;
		if (h>=maxn)h=0;
		for (i=0;i<n;i++){
			//if (c[h][i]==1){
				t++;
				//cout<<h<<' '<<t<<' '; 
				if (t>=maxn)t=0;
				for (j=0;j<=i;j++){
					c[t][j]=!c[h][i-j];
					//cout<<c[t][j]<<' ';
				}
				for (j=i+1;j<n;j++){
					c[t][j]=c[h][j]; 
					//cout<<c[t][j]<<' ';
				}
				//cout<<endl;
				for (j=0;j<n;j++)if (c[t][j])break;
				if (j==n){cout<<ans<<endl;return ;}
				for  (j=h;j!=t;){
					for (k=0;k<n;k++){
						if (c[t][k]!=c[j][k])break;
					}
					if (k==n){
						t--;
						if (t<0)t=maxn-1;
						break;
					}
					j++;
					if (j>=maxn)j=0;
				}
			//}
		}
		if (h==tail){ans++;tail=t;}
	}
}

int main (){
	//freopen ("b.in","r",stdin);
	//freopen ("b.out","w",stdout);
	cin>>t;
	int i,j;
	for (i=1;i<=t;i++){
		cout<<"Case #"<<i<<": "; 
		scanf ("%s",s);
		n=strlen (s); 
		for (j=0;j<n;j++){
			if (s[j]=='-')c[1][j]=1;
			else c[1][j]=0;
		}
		bfs ();
	}
	return 0;
}
