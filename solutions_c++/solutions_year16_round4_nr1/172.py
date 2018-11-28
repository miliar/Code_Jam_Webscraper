#include<stdio.h>
#include<string>
using namespace std;
string res[13][3];
void rearrange(string&s){
	for(int i=1; i<s.length(); i*=2){
		string tmp="";
		for(int j=0; j<s.length(); j+=2*i){
			if(s.substr(j,i) < s.substr(j+i,i)){
				tmp += s.substr(j,i);
				tmp += s.substr(j+i,i);
			}else{
				tmp += s.substr(j+i,i);
				tmp += s.substr(j,i);
			}
		}
		s = tmp;
	}
}
void init(){
	res[0][0] = "P";
	res[0][1] = "R";
	res[0][2] = "S";
	for(int i=1; i<=12; i++){
		for(int j=0; j<3; j++){
			for(int k=0; k<res[i-1][j].length(); k++)
				if(res[i-1][j][k] == 'P')
					res[i][j] += "PR";
				else
				if(res[i-1][j][k] == 'R')
					res[i][j] += "RS";
				else
				if(res[i-1][j][k] == 'S')
					res[i][j] += "PS";
			rearrange(res[i][j]);
		}
	}
}
int main(){
	int _;
	init();
	scanf("%d",&_);
	for(int T=1; T<=_; T++){
		int n,P,R,S;
		scanf("%d%d%d%d",&n,&R,&P,&S);
		string out = "";
		for(int j=0; j<3; j++){
			int p=P,r=R,s=S;
			for(int k=0; k<res[n][j].length(); k++)
				if(res[n][j][k] == 'P')
					p--;
				else
				if(res[n][j][k] == 'R')
					r--;
				else
				if(res[n][j][k] == 'S')
					s--;
			if(p==0 && r==0 && s==0){
				if(out == "" || out > res[n][j])
					out = res[n][j];
			}
		}
		printf("Case #%d: %s\n",T,out==""?"IMPOSSIBLE":out.c_str());
	}
	return 0;
}