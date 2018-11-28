//By SCJ
#include<iostream>
#include<deque>
using namespace std;
deque<char> ans;
int a[128],all;
bool dfs()
{
	//cout<<"dfs1\n";
	int mx=-1,tp;
	for(int i='A';i<='Z';++i)
	{
		if(a[i]>mx) mx=a[i],tp=i;
	}
	if(mx==0) return true;
	a[tp]--;all--;
	bool ff=0;
	ans.push_back((char)tp);
	mx=-1;
	for(int i='A';i<='Z';++i)
	{
		if(a[i]>mx) mx=a[i],tp=i;
	}
	if(mx*2<=all)
	{
		ff=1;
		ans.push_back(' ');
		if(dfs()) return true;
	}
	//
	//cout<<"dfs2\n";
	if(ff) ans.pop_back();
	ff=0;
	a[tp]--;all--;
	ans.push_back((char)tp);
		ff=1;
		ans.push_back(' ');
//		for(int k=0;k<ans.size();++k) cout<<ans[k];
//		cout<<endl;
		dfs();
}
int main()
{
//ios::sync_with_stdio(0);
//cin.tie(0);
	int T;cin>>T;
	for(int no=1;no<=T;++no)
	{
		ans.clear();
		int n;cin>>n;
		//all=n;
		for(int i='A';i<'A'+n;++i) cin>>a[i],all+=a[i];
		//cout<<ans.size()<<endl;
		dfs();
		//cout<<"test\n";
		cout<<"Case #"<<no<<": ";
		for(int i=0;i<ans.size();++i) cout<<ans[i];
		cout<<endl;
//		cout<<ans.size()<<endl;
//		while(ans.size())
//		{
//			cout<<ans.front();
//			ans.pop_back();
//		}
	}
}
