#include<iostream>
#include<vector>
#include<stack>
#define loop(i,a,b) for(int i=a;i<b;i++)
#define rep(i,a) loop(i,0,a)
using namespace std;

int main(){
	int n;
	cin>>n;
	rep(p,n){
		string s;
		cin>>s;
		bool pan[s.size()];
		rep(i,s.size()){
			if(s[i]=='+')pan[i]=1;
			else pan[i]=0;
		}
		int cnt=0;
		for(int i=s.size()-1;i>=0;i--){
			if(pan[i]==0){
				cnt++;
				rep(j,i+1)pan[j]=(!pan[j]);
			}
		}
		cout<<"Case #"<<p+1<<": "<<cnt<<endl;
	}
	return 0;
}