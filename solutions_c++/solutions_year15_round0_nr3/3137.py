#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
char s[10010];
char ss[10010];
bool kk[10010];
char mmm(char a,char b,int &s){
if(a=='1'){
	if(b=='1')return '1';
	if(b=='i')return 'i';
	if(b=='j')return 'j';
	if(b=='k')return 'k';
}
else if(a=='i'){
if(b=='1')return 'i';
	if(b=='i'){s=1;return '1';}
	if(b=='j')return 'k';
	if(b=='k'){s=1;return 'j';}
}
else if(a=='j'){
if(b=='1')return 'j';
	if(b=='i'){s=1;return 'k';}
	if(b=='j'){s=1;return '1';}
	if(b=='k')return 'i';
}
else if(a=='k'){
if(b=='1')return 'k';
	if(b=='i')return 'j';
	if(b=='j'){s=1;return 'i';}
	if(b=='k'){s=1;return '1';}
}
}
int main() {
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
			memset(kk,0,sizeof(kk));
		int L,X;
		cin>>L>>X;
		cin>>ss;
		int sn=0;
		for(int j=1;j<=X;j++){
		for(int i=0;i<L;i++){
		s[++sn]=ss[i];
		}
		}
		char aa='1';
		int aas=0;
		for(int i=sn;i>0;i--){
		//cout<<i<<"~~\n";
			int si=0;
			aa=mmm(s[i],aa,si);
			aas=(aas^si);
			//cout<<i<<" "<<aa<<" "<<aas<<"==kk\n";
			if(aa=='k'&&aas==0)kk[i]=1;
		}
		//cout<<kk[1]<<"==kk\n";
		//cout<<kk[2]<<"==kk\n";
		//cout<<kk[3]<<"==kk\n";
		//cout<<"==\n";
		int an=0;
		char ai='1';
		int ais=0;
		for(int i=1;i<=sn-2;i++){
			int si=0;
			ai=mmm(ai,s[i],si);
			ais=(ais^si);
			
			if(!(ai=='i'&&ais==0))continue;
			char aj='1';
			int ajs=0;
			for(int j=i+1;j<=sn-1;j++){
				int ssi=0;
				aj=mmm(aj,s[j],ssi);
				ajs=(ajs^ssi);
				if(i==3&&j==6){
				//cout<<ai<<"=="<<aj<<"=="<<kk[7]<<"==\n";
				}
				if(!(aj=='j'&&ajs==0))continue;
				if(kk[j+1]){an=1;break;}
			}
			if(an)break;
		}
		if(an==1)cout<<"Case #"<<tt<<": YES"<<endl;
		else cout<<"Case #"<<tt<<": NO"<<endl;
	}
	return 0;
}

