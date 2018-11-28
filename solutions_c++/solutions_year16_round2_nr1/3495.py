#include <iostream>
#include <vector>
#include <array>
#include <cassert>

using namespace std;

string numbers[10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};

template <typename T,unsigned long N>
ostream& operator<<(ostream &os,const array<T,N> &arr){
	int i;
	os<<'{';
	if(N==0)return os;
	os<<arr[0];
	for(i=1;i<(int)N;i++)os<<','<<arr[i];
	return os<<'}';
}

template <typename T>
ostream& operator<<(ostream &os,const vector<T> &arr){
	int i;
	if(arr.size()==0)return os<<"{}";
	os<<'{';
	os<<arr[0];
	for(i=1;i<(int)arr.size();i++)os<<','<<arr[i];
	return os<<'}';
}

bool tryfrom(array<int,26> &counts,vector<int> &res,int from){
	cerr<<"tryfrom("<<counts<<','<<res<<','<<from<<')'<<endl;
	int i,j;
	for(i=0;i<26;i++)if(counts[i]>0)break;
	if(i==26)return true;
	for(i=from;i<=9;i++){
		const string &num=numbers[i];
		for(j=0;j<(int)num.size();j++){
			if(counts[num[j]-'A']==0)break;
			counts[num[j]-'A']--;
		}
		if(j!=(int)num.size()){
			for(j--;j>=0;j--)counts[num[j]-'A']++;
			continue;
		}
		res.push_back(i);
		if(tryfrom(counts,res,i))return true;
		res.pop_back();
		for(j=0;j<(int)num.size();j++)counts[num[j]-'A']++;
	}
	return false;
}

int main(){
	int T;
	cin>>T;
	string line;
	for(int tt=1;tt<=T;tt++){
		cin>>line;
		cout<<"Case #"<<tt<<": ";
		array<int,26> counts;
		int i;
		for(i=0;i<26;i++)counts[i]=0;
		for(i=0;i<(int)line.size();i++)counts[line[i]-'A']++;
		vector<int> res;
		assert(tryfrom(counts,res,0));
		for(int i : res)cout<<i;
		cout<<endl;
	}
}
