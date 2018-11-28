#include<bits/stdc++.h>

using namespace std;
typedef long long ll;
#define N 100005

int main(){
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int tc = 1;tc<=t;tc++){
		int n;
		cin>>n;
		int a[n];
		for(int i = 0;i<n;i++)
		cin>>a[i];
		priority_queue< pair<int,int> > p;
		for(int i = 0;i<n;i++){
			p.push(make_pair(a[i],i));
		}
	
		cout<<"Case #"<<tc<<": ";
		
		while(p.size() > 2){
			cout<<(char)(p.top().second + 'A')<<" ";
			pair<int,int> tem = p.top();
			p.pop();
			if(tem.first > 1)
			p.push(make_pair(tem.first-1,tem.second));
		}
		int x = p.top().first;
		char c1 = (char) (p.top().second + 'A');
		p.pop();
		char c2 = (char) (p.top().second + 'A');
		while(x--){
			cout<<c1<<c2<<" ";
		}
		cout<<endl;
	}

	return 0;
}
