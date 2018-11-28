#include<iostream>
#include<string>
using namespace std;

void solve(int q){
	cout<<"Case #"<<q<<": ";
	string S,T;
	cin>>S;
	int n=S.size(),j=0;
	char s[1000];
	for(string::iterator i=S.begin();i!=S.end();++i){
		s[j]=*i;
		++j;
	}
	T.push_back(s[0]);
	for(int i=1;i<n;++i){
		if(*T.begin()-s[i]>0){
			T.insert(T.end(),s[i]);
		}else{
			T.insert(T.begin(),s[i]);
		}
	}
	cout<<T<<endl;
}

int main(){
	int Q;
	cin>>Q;
	for(int q=1;q<=Q;++q){
		solve(q);
	}
}
