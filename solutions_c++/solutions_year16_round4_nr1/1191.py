#include<fstream>
#include<string.h>
#include<algorithm>
using namespace std;
void fill(char* s, char c,int l){
	char cc;
	if(c=='P')cc='R';
	else if(c=='S')cc='P';
	else if(c=='R')cc='S';
	if(l>2){
		fill(s,c,l/2);
		fill(s+l/2,cc,l/2);
	}
	else{
		s[0]=c;
		s[l/2]=cc;
	}
}
void check(char* s,int k,int d){
	bool m=false;
	for(int i=0;i<d;i++){
		if(s[k+i]>s[k+d+i]){
			m=true;
			break;
		}
		else if(s[k+i]<s[k+d+i])break;
	}
	if(m){
		for(int i=0;i<d;i++){
			char tmp=s[k+i];
			s[k+i]=s[k+d+i];
			s[k+d+i]=tmp;
		}
	}
}
int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int tt=0;
	fin>>tt;
	int n,r,p,s;
	int rps[3][13][3];
	rps[0][1][0]=1;
	rps[0][1][1]=0;
	rps[0][1][2]=1;
	rps[1][1][0]=1;
	rps[1][1][1]=1;
	rps[1][1][2]=0;
	rps[2][1][0]=0;
	rps[2][1][1]=1;
	rps[2][1][2]=1;
	for(int i=0;i<3;i++){
		for(n=2;n<=12;n++){
			rps[i][n][0]=rps[i][n-1][0]+rps[i][n-1][1];
			rps[i][n][1]=rps[i][n-1][1]+rps[i][n-1][2];
			rps[i][n][2]=rps[i][n-1][2]+rps[i][n-1][0];
		}
	}
	for(int kk=1;kk<=tt;kk++){
		fin>>n>>r>>p>>s;
		int i;
		for(i=0;i<3;i++){
			if(r==rps[i][n][0]&&p==rps[i][n][1]&&s==rps[i][n][2])break;
		}
		if(i==3)
			fout<<"Case #"<<kk<<": "<<"IMPOSSIBLE"<<endl;
		else{
			char c;
			char ans[4097];
			if(i==0)c='R';
			else if(i==1)c='P';
			else if(i==2)c='S';
			int l=1;
			for(int j=0;j<n;j++)l*=2;
			fill(ans,c,l);
			ans[l]=0;
			for(int j=0;j<n;j++){
				int d=pow(2,j);
				for(int k=0;k+d<l;k+=2*d){
					check(ans,k,d);
				}
			}
			fout<<"Case #"<<kk<<": "<<ans<<endl;
		}
	}
	return 0;
}