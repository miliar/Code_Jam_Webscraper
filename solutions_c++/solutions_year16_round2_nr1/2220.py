#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
const double eps=1e-9;
int kol[100];
int num[100];
vector<pair<char,int>> v;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	scanf("%d",&n);
	for(int cs=1;cs<=n;++cs){
		/*for(int i=0;i<26;++i){
			pair<char,int> tmpp;
			tmpp.first='A'+i;
			tmpp.second=0;
			v.push_back(tmpp);
		}*/
		string s,t="";
		cin>>s;
		for(int i=0;i<s.size();++i){
			int tmp=s[i]-'A'+1;
			++kol[tmp];
		}
		while(kol[26]>0){
			++num[0];
			--kol[5];
			--kol[18];
			--kol[15];
			--kol[26];
		}
		while(kol[23]>0){
			++num[2];
			--kol[20];
			--kol[15];
			--kol[23];
		}
		while(kol[24]>0){
			++num[6];
			--kol[19];
			--kol[9];
			--kol[24];
		}
		while(kol[7]>0){
			++num[8];
			--kol[5];
			--kol[9];
			--kol[8];
			--kol[20];
			--kol[7];
		}
		while(kol[19]>0){
			++num[7];
			kol[5]-=2;
			--kol[22];
			--kol[14];
			--kol[19];
		}
		while(kol[8]>0){
			++num[3];
			kol[5]-=2;
			--kol[20];
			--kol[18];
			--kol[8];
		}
		while(kol[22]>0){
			++num[5];
			--kol[6];
			--kol[9];
			--kol[5];
			--kol[22];
		}
		while(kol[18]>0){
			++num[4];
			--kol[6];
			--kol[15];
			--kol[21];
			--kol[18];
		}
		while(kol[9]>0){
			++num[9];
			kol[14]-=2;
			--kol[5];
			--kol[9];
		}
		while(kol[15]>0){
			++num[1];
			--kol[14];
			--kol[5];
			--kol[15];
		}
		for(int i=0;i<10;++i){
			while(num[i]>0){
				char ch='0'+i;
				t+=ch;
				--num[i];
			}
		}
		cout<<"Case #"<<cs<<": "<<t<<endl;
	}
	return 0;
}