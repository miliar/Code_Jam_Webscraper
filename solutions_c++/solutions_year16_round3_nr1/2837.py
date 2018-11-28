#include<iostream>
#include<utility>
#include<algorithm>
using namespace std;

bool compare(pair<int,char> p,pair<int,char> q){
	return p.first>q.first;
}

void solve(int q){
	int n,c=0;
	pair<int,char> p[27];
	cin>>n;
	fill(p,p+27,make_pair(0,'?'));
	for(int i=0;i<n;++i){
		cin>>p[i].first;
		c+=p[i].first;
		p[i].second='A'+i;
	}
	sort(p,p+n,compare);
	cout<<"Case #"<<q<<":";
	if(n>=3){
		for(int i=0;i<n;++i){
			while(p[i].first>p[i+1].first){
				if(c==n){
					for(int j=0;j<=n-3;++j){
						cout<<" "<<p[j].second;
						--p[j].first;
						--c;
					}
					cout<<" "<<p[n-2].second<<p[n-1].second;
					--p[n-1].first;
				}else{
					for(int j=0;j<=i;++j){
						cout<<" "<<p[j].second;
						--p[j].first;
					}
					c-=(i+1);
				}
			}
		}
		cout<<endl;
	}else{
		while(p[0].first>p[1].first){
			cout<<" "<<p[0].second;
			--p[0].first;
		}
		while(p[0].first>0){
			cout<<" AB";
			--p[0].first;
		}
		cout<<endl;
	}
}

int main(){
	int Q;
	cin>>Q;
	for(int q=1;q<=Q;++q){
		solve(q);
	}
}
