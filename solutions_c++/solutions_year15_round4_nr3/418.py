#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <cstring>
#include <cstdio>


using namespace std;

int N,M,K,Q,T;
int NN;
int arr[200][13];
int cc[200];

map<string, int> hash;
int eng[3003];
int fren[3003];
int dfs(int layer){
	if(layer == N-2){
		int res=0;
		for(int i=0;i<hash.size(); ++i){
			if(eng[i]&&fren[i])
				++res;
		}
		return res;
	}
	int res;
	for(int i=0;i<cc[layer];++i){
		eng[arr[layer][i]]++;
	}
	res= dfs(layer+1);
	for(int i=0;i<cc[layer];++i){
		eng[arr[layer][i]]--;
	}
	for(int i=0;i<cc[layer];++i){
		fren[arr[layer][i]]++;
	}
	res= min(res, dfs(layer+1));
	for(int i=0;i<cc[layer];++i){
		fren[arr[layer][i]]--;
	}
	return res;
}

int main(){
	char tmp;
	cin>>T;
	for(int cs=1;cs<=T;++cs){
		hash.clear();
		memset(cc, 0, sizeof(cc));
		memset(eng, 0, sizeof(eng));
		memset(fren, 0, sizeof(fren));
		int hashcnt=0;

		cin>>N;
		NN=N;
		tmp=0;
		while(tmp!='\n'){
			string str;
			cin>>str;
			if(!hash.count(str))
				hash.insert(make_pair(str, hashcnt++));
			++eng[hash[str]];
			tmp=getchar();
		}
		tmp=0;
		while(tmp!='\n'){
			string str;
			cin>>str;
			if(!hash.count(str))
				hash.insert(make_pair(str, hashcnt++));
			++fren[ hash[str]];
			tmp=getchar();
		}
		NN=N-3;
		while(~NN){
			string str;
			cin>>str;
			if(!hash.count(str))
				hash.insert(make_pair(str, hashcnt++));
			tmp=getchar();
			arr[NN][cc[NN]++]=hash[str];
			if(tmp == '\n'){
				--NN;
			}
		}

		cout<<"Case #"<<cs<<": "<<dfs(0)<<endl;
	}

	return 0;
}


