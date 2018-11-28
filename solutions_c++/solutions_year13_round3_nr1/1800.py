#include<iostream>
#include<string>

using namespace std;

int T;
string S;
int N;
int ans;

bool has(int s,int f) {
	for(int i=s;i<=f-N;i++) {
		bool tmp = true;
		for(int j=i;j<i+N;j++)
			if(S[j] == 'o' || S[j] == 'a' || S[j] == 'e' ||
				S[j] == 'u' || S[j] == 'i')
				tmp = false;
		if(tmp) return true;
	}
	return false;
}

int main() {
	cin>>T;
	for(int ti=0;ti<T;ti++) {
		cin>>S>>N;
		ans = 0;
		for(int i=0;i<S.size();i++)
			for(int j=i+N;j<=S.size();j++)
				if(has(i,j)) {ans++;}
		cout<<"Case #"<<ti+1<<": "<<ans<<endl;
	}
	return 0;
}