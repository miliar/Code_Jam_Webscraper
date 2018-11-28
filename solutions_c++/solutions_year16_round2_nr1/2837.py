#include<iostream>
#include<sstream>
#include<iomanip>
#include<stdlib.h>
#include<string>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<queue>
#include<stack>
#include<map>
#include<utility>
#include<algorithm>
#include<complex>
using namespace std;
#define loop(i,l,r) for(int (i)=(int)(l);(i)<(int)(r);(i)++)
#define rloop(i,l,r) for(int (i)=(int)(l);(i)>(int)(r);(i)--)
#define rep(i,n) loop(i,0,n)
#define rrep(i,n) rloop(i,n-1,-1)
#define INF 0x3f3f3f3f
#define mod 1000000007LL
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;
typedef complex<double> C;

vector<string> split(stringstream& ss){
	string str;
	vector<string> res;
	while(ss>>str)res.push_back(str);
	return res;
}


int main(){
	int n;
	string s;
	const char* str[]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
	cin>>n;
	rep(i,n){
			cin>>s;
			vector<int> d(26,0),dd(10,0);
			rep(j,s.size())d[s[j]-'A']++;
			dd[0]=d['Z'-'A'];//0
			rep(j,strlen(str[0]))d[str[0][j]-'A']-=dd[0];
			dd[2]=d['W'-'A'];//2
			rep(j,strlen(str[2]))d[str[2][j]-'A']-=dd[2];
			dd[4]=d['U'-'A'];//4
			rep(j,strlen(str[4]))d[str[4][j]-'A']-=dd[4];
			dd[6]=d['X'-'A'];//6
			rep(j,strlen(str[6]))d[str[6][j]-'A']-=dd[6];
			dd[8]=d['G'-'A'];//8
			rep(j,strlen(str[8]))d[str[8][j]-'A']-=dd[8];
			dd[1]=d['O'-'A'];//1
			rep(j,strlen(str[1]))d[str[1][j]-'A']-=dd[1];
			dd[3]=d['R'-'A'];//3
			rep(j,strlen(str[3]))d[str[3][j]-'A']-=dd[3];
			dd[5]=d['F'-'A'];//5
			rep(j,strlen(str[5]))d[str[5][j]-'A']-=dd[5];
			dd[7]=d['S'-'A'];//7
			rep(j,strlen(str[7]))d[str[7][j]-'A']-=dd[7];
			dd[9]=d['I'-'A'];//9
			rep(j,strlen(str[9]))d[str[9][j]-'A']-=dd[9];
			cout<<"Case #"<<i+1<<": ";
			rep(j,10)rep(k,dd[j])cout<<j;
			cout<<endl;
	}
}					
