#include<set>
#include<iostream>
#include<algorithm>
#include<functional>
using namespace std;

int T,N,X,S[11111];

int main(){

	freopen("A-large.in","r",stdin);
	freopen("out","w",stdout);

	cin>>T;
	for(int tc=1; tc<=T; tc++){
		cout<<"Case #"<<tc<<": ";

		cin>>N>>X;
		for(int i=0; i<N; i++) cin>>S[i];

		sort(S,S+N,greater<int>());

		multiset<int> s;

		for(int i=0; i<N; i++){
			bool inserted=false;
			for(auto it=s.begin(); it!=s.end(); it++){
				if(*it >= S[i]){
					int tmp = *it;
					s.erase(it);
					s.insert(0);
					inserted = true;
					break;
				}
			}
			if(!inserted)
				s.insert(X-S[i]);
		}

		cout<<s.size()<<endl;
	}
}
