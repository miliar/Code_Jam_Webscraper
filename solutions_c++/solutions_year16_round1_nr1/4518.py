#include<iostream>
#include<string>
#include<vector>
#include<queue>
#include<set>
#include<algorithm>
#define loop(i,a,b) for(int i=a;i<b;i++)
#define rep(i,a) loop(i,0,a)
using namespace std;

void print(int n,string ans){
	cout<<"Case #"<<n<<": "<<ans<<endl;
}

int main(){
	int n;
	cin>>n;
	rep(p,n){
		string s,ans="";
		pair<int,string> alt(0,""),temp;
		cin>>s;
		queue<pair<int,string> > que;
		vector<string> vec;
		que.push(alt);
		while(!que.empty()){
			alt=que.front();
			que.pop();
			temp=alt;
			if(temp.first!=s.size()){	
				temp.second=temp.second+s[temp.first];
				temp.first++;
				que.push(temp);
			}else{
				vec.push_back(temp.second);
				continue;
			}
			if(alt.first!=s.size()){
				alt.second=s[alt.first]+alt.second;
				alt.first++;
				que.push(alt);
			}else{
				vec.push_back(alt.second);
			}
		}
		sort(vec.begin(),vec.end());
		print(p+1,vec[vec.size()-1]);
	}
	return 0;
}