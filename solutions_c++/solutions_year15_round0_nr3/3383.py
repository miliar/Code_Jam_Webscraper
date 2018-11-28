//============================================================================
// Name        : jam.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
using namespace std;

int main() {

#ifndef ONLINE_JUDGE
 freopen("D:\\C-small-attempt0.in","rt",stdin);
 freopen("D:\\out.out","wt",stdout);
#endif

	int test;
	cin>>test;
	for (int l=1;l<=test;++l){
int n,m;
string in,s;
map <string,string> mp;
mp["11"]="1";mp["-11"]="-1";mp["1i"]="i";mp["-1i"]="-i";mp["1j"]="j";mp["-1j"]="-j";mp["1k"]="k";mp["-1k"]="-k";
mp["i1"]="i";mp["-i1"]="-i";mp["ii"]="-1";mp["-ii"]="1";mp["ij"]="k";mp["-ij"]="-k";mp["ik"]="-j";mp["-ik"]="j";
mp["j1"]="j";mp["-j1"]="-j";mp["ji"]="-k";mp["-ji"]="k";mp["jj"]="-1";mp["-jj"]="1";mp["jk"]="i";mp["-jk"]="-i";
mp["k1"]="k";mp["-k1"]="-k";mp["ki"]="j";mp["-ki"]="-j";mp["kj"]="-i";mp["-kj"]="i";mp["kk"]="-1";mp["-kk"]="1";
cin>>n>>m>>in;
for (int j=0;j<m;++j)
	s+=in;
bool findi=false,findj=false,findk=false;
int loop=0;
string fund="";
for (int i=0;i<s.length();++i){
fund+=s[i];
if (mp.count(fund)>0 && loop==0){
	if(mp[fund]=="i"){
		findi=true;
		loop=1;
		fund="";
	}
	else
		fund=mp[fund];
}
if(mp.count(fund)>0 && loop==1){
	if(mp[fund]=="j"){
		findj=true;
		loop=2;
		fund="";
	}
	else
		fund=mp[fund];
}
if(mp.count(fund)>0 && loop==2){
	if(mp[fund]=="k"&&i==(s.length()-1)){

		findk=true;
		break;
	}
	else
		fund=mp[fund];
}

}
if((findi && findj && findk) || s=="ijk")
	cout<<"Case"<<" #"<<l<<": "<<"YES"<<endl;
else
	cout<<"Case"<<" #"<<l<<": "<<"NO"<<endl;
	}
	return 0;
}
