#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<queue>
#include<stack>
#include<deque>
#include<map>
#include<set>
#include<list>
#include<vector>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<sstream>
using namespace std;
#define NMAX 0

int zimuCnt[26];
string shuzi[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int b[10]={0,0,0,0,0,0,0,0,0,0};

int del(string s,int n,int cnt){
	string shu = shuzi[n];
	for(int i=0;i<shu.size();i++){
		zimuCnt[shu[i]-'A']-=cnt;
	}
	b[n]+=cnt;
}

int main(){
	//freopen("A-1.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for(int c=1;c<=T;c++){
		memset(zimuCnt,0,sizeof(zimuCnt));
		memset(b,0,sizeof(b));
		string s;
		cin>>s;
		char ch = 'A';
		for(int i=0;i<26;i++){
			zimuCnt[i] = count(s.begin(), s.end(), (char)(ch+i));
		}
		del(s,0,zimuCnt['Z'-'A']);
		del(s,2,zimuCnt['W'-'A']);
		del(s,4,zimuCnt['U'-'A']);
		del(s,6,zimuCnt['X'-'A']);
		del(s,8,zimuCnt['G'-'A']);
		del(s,1,zimuCnt['O'-'A']);
		del(s,3,zimuCnt['R'-'A']);
		del(s,5,zimuCnt['F'-'A']);
		del(s,7,zimuCnt['S'-'A']);
		del(s,9,zimuCnt['I'-'A']);
		cout<<"Case #"<<c<<": ";
		for(int i=0;i<10;i++){
			for(int j=0;j<b[i];j++){
				cout<<i;
			}
		}
		cout<<endl;
	}
	return 0;
}


