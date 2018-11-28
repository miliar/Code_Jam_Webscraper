#include<stdio.h>
#include<algorithm>
#include<vector>
#include<functional>
#include<string>
#define all(A) (A).begin(), (A).end()
#define II(A) int (A); scanf("%d",&(A));
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;

int TC;

string ans(int R,int P,int S,int type){
	if(R<0 || P<0 || S<0){
		return "IMPOSSIBLE";
	}
	if(R+P+S==1){
		if(R)return "R";
		if(P)return "P";
		if(S)return "S";
		return "";
	}
	string str = ans((R+S-P)/2,(R+P-S)/2,(P+S-R)/2,(type+1)%6);
	if(str=="IMPOSSIBLE")return str;
	string ret;
	for(auto &c:str){
		if(c=='P'){
			if(type<=2)ret.push_back('P'),ret.push_back('R');
			else ret.push_back('R'),ret.push_back('P');
		}
		else if(c=='S'){
			if(2<=type && type<=4)ret.push_back('S'),ret.push_back('P');
			else ret.push_back('P'),ret.push_back('S');
		}
		else{
			if(1<=type && type<=3)ret.push_back('S'),ret.push_back('R');
			else ret.push_back('R'),ret.push_back('S');
		}
	}
	return ret;
}

int main(){
	freopen("input.txt","r",stdin),freopen("output.txt","w",stdout);
	scanf("%d",&TC);
	for(int tc=1;tc<=TC;tc++){
		int N,R,P,S;
		scanf("%d%d%d%d",&N,&R,&P,&S);
		printf("Case #%d: %s\n",tc,ans(R,P,S,0).c_str());
	}
	return 0;
}