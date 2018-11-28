#include<iostream>
#include<cstdio>
#include<map>
#include<vector>
#include<cstring>
using namespace std;
int n,f[30];
int nwords;
map<string,int> words;
vector<int> ans[30];
int a[10000],b[10000];
int ansnum;
void dfs(int x){
	if(x==n){
//	
//		cout<<"ADSF"<<endl;
//		for(int i=0;i<n;i++) cout<<f[i]<<' '; cout<<endl;
//		
//		for(int i=1;i<=nwords;i++) cout<<a[i]<<' '; cout<<endl;
//		for(int i=1;i<=nwords;i++) cout<<b[i]<<' '; cout<<endl;
		int tmp=0;
		for(int i=1;i<=nwords;i++)
			if(a[i]&&b[i]) tmp++;
		if(tmp<ansnum) ansnum=tmp;
		return ;
	}
	int i;
	for(i=0;i<ans[x].size();i++) a[ans[x][i]]++;
	dfs(x+1);
	for(i=0;i<ans[x].size();i++) a[ans[x][i]]--;
	for(i=0;i<ans[x].size();i++) b[ans[x][i]]++;
	dfs(x+1);
	for(i=0;i<ans[x].size();i++) b[ans[x][i]]--;
}
int main(){
	freopen("C-small-attempt2.in","r",stdin); 
	freopen("C-small-attempt2.out","w",stdout); 
	int T,kase,i;
	char s[100000];
	scanf("%d",&T); 
	for(int kase=1;kase<=T;kase++){
		scanf("%d",&n);  
		words.clear(); getchar(); nwords=0;
		string tmp;
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		
		gets(s);
		tmp="";
		for(int j=0;s[j];j++){
				if(s[j]==' '){
					if(words[tmp]==0) words[tmp]=++nwords;
					a[words[tmp]]++;
					tmp="";
				}
				else tmp+=s[j];
			}
		if(words[tmp]==0) words[tmp]=++nwords;
		a[words[tmp]]++;
		
		gets(s);
		tmp="";
		for(int j=0;s[j];j++){
				if(s[j]==' '){
					if(words[tmp]==0) words[tmp]=++nwords;
					b[words[tmp]]++;
					tmp="";
				}
				else tmp+=s[j];
			}
		if(words[tmp]==0) words[tmp]=++nwords;
		b[words[tmp]]++;
		n=n-2;
		
		for(i=0;i<n;i++){
			gets(s); 
		//	puts(s); 
			ans[i].clear();
			string tmp="";
			for(int j=0;s[j];j++){
				if(s[j]==' '){
					if(words[tmp]==0) words[tmp]=++nwords;
					ans[i].push_back(words[tmp]);
					tmp="";
				}
				else tmp+=s[j];
			}
			//cout<<tmp<<endl;
			if(words[tmp]==0) words[tmp]=++nwords;
			ans[i].push_back(words[tmp]);
		}
		ansnum=1<<30;
	//	cout<<n<<endl;
		dfs(0);
		printf("Case #%d: %d\n",kase,ansnum);
	}
	return 0;
}
