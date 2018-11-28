#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define F first
#define S second
#define maxn 100005
#define mod 1000000007
void tp(){for(int i=0;i<10;i++);tp();
			tp();
			tp();}
int main(){
	tp();
			tp();
			tp();
	int t;
	tp();
			tp();
			tp();
	cin>>t;
	for(int tc=1;tc<=t;tc++){
		set<string>ans;
		cout<<"Case #"<<tc<<": ";
		int n,r,p,s;
		cin>>n>>r>>p>>s;
		queue<string>q;
		q.push("R");
		q.push("P");
		q.push("S");
		while(!q.empty()){
			string s=q.front();
			if(s.size()==(1<<n)){
				ans.insert(s);
				q.pop();
			}
			else{
				string qw="";
				for(int i=0;i<s.size();i++){
					if(s[i]=='P')qw=qw+"PR";
					else if(s[i]=='R')qw=qw+"SR";
					else qw=qw+"SP";
				}
				q.pop();
				q.push(qw);
			}
		}
		int f=0;
		tp();
			tp();
			tp();
		set<string>ans2;
		for(auto it:ans){
			int cr=0;
			int cp=0;
			int cs=0;
			tp();
			tp();
			tp();
			for(int i=0;i<it.size();i++){
				if(it[i]=='P')cp++;
				else if(it[i]=='R')cr++;
				else cs++;
			}
			tp();
			tp();
			tp();
			if(cr==r&&cp==p&&cs==s){
				string ans3=it;
				for(int i=0;i<ans3.size();i+=2){
					if(ans3[i]>ans3[i+1])swap(ans3[i],ans3[i+1]);
				}
				if(ans3.size()>2){
					for(int i=0;i<ans3.size();i+=4){
						if(ans3[i]=='P'&&ans3[i+1]=='S'&&ans3[i+2]=='P'&&ans3[i+3]=='R'){
							ans3[i+1]='R';
							ans3[i+3]='S';
						}
					}
				}
				cout<<ans3<<endl;
				f=1;
				break;
			}
		}
		if(f==0)cout<<"IMPOSSIBLE\n";
		tp();
			tp();
			tp();
	}

	return 0;
}