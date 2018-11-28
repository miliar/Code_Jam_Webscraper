#include <iostream>
#include <cstdio>
#include <cstring>
#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int n,m,aa,bb,cc;
vector<int> v[20];

string gao(int k){
	//cout << aa<< "!"<<bb<<" "<<cc<<endl;

	for (int i=0;i<16;i++) v[i].clear();
	
	v[0].push_back(k);
	//	cout << aa<< "!"<<bb<<" "<<cc<<endl;

	for (int i=1;i<=n;i++){
		for (int j=0;j<v[i-1].size();j++){
			v[i].push_back(v[i-1][j]);
			v[i].push_back((v[i-1][j]+3-1)%3);
		}
	}
	
	int x,y,z;
	x=y=z=0;
	for (int i=0;i<v[n].size();i++){
		if (v[n][i]==0) x++;
		if (v[n][i]==1) y++;
		if (v[n][i]==2) z++;
	}
	string ss="";
	//cout << x<< " "<<y<<" "<<z<<endl;
	//cout << aa<< " "<<bb<<" "<<cc<<endl;

	if (x==aa && y==bb && z==cc){
		//cout<<1<<endl;
		for (int i=0;i<v[n].size();i+=2){
			string xx,yy;
			if (v[n][i]==0) xx="R";
			if (v[n][i]==1) xx="P";
			if (v[n][i]==2) xx="S";
			if (v[n][i+1]==0) yy="R";
			if (v[n][i+1]==1) yy="P";
			if (v[n][i+1]==2) yy="S";
			if (xx+yy<yy+xx) ss+=xx+yy;
				else ss+=yy+xx;
				//cout<<ss<<endl;
		}
	//	cout<<ss<<endl;
	}
		else ss="Z";
	return ss;
}

string check(string s1,string s2){
	string ss1,ss2;
	if (s1.length()>1){
		ss1=check(s1.substr(0,s1.length()/2),s1.substr(s1.length()/2,s1.length()/2));
	}else ss1=s1;
	if (s2.length()>1){
		ss2=check(s2.substr(0,s1.length()/2),s2.substr(s1.length()/2,s1.length()/2));
	}else ss2=s2;


	if (ss1<ss2) return ss1+ss2;
		else return ss2+ss1;
}


int main(){
	int T;
	cin >> T;
	for (int ti=1;ti<=T;ti++){
		scanf("%d%d%d%d",&n,&aa,&bb,&cc);
		cout <<"Case #"<< ti<<": ";
		string ans="Z";
		//	cout << aa<< " "<<bb<<" "<<cc<<endl;

		string s1=gao(0);
	//	cout <<s1<<endl;
		if (s1!="Z")
			s1 = check(s1.substr(0,s1.length()/2),s1.substr(s1.length()/2,s1.length()/2));
		string s2=gao(1);
		//cout <<s1<<endl;

	//	cout<<s2<<endl;
		if (s2!="Z")
			s2 = check(s2.substr(0,s2.length()/2),s2.substr(s2.length()/2,s2.length()/2));
		//cout <<s2<<endl;
		
		string s3=gao(2);
		//cout <<s3<<endl;

		if (s3!="Z")
			s3 = check(s3.substr(0,s3.length()/2),s3.substr(s3.length()/2,s3.length()/2));
		//cout <<s3<<endl;

		//cout <<s1 <<" "<<s2<<" "<<s3<<endl;
		if (s1<ans)	ans=s1;	
		if (s2<ans)	ans=s2;	
		if (s3<ans)	ans=s3;
		if (ans=="Z") ans="IMPOSSIBLE";	
		cout<<ans<<endl;
	}
	return 0;
}
