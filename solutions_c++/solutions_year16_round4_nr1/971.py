#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int n,a[10],cnt[10];
char ch[5];
int tot;

struct node
{
	int v,l,r;
} tr[50000];


int build(int k,int d,int lim){
	tot++;
	tr[tot].v=k;
	//cerr <<"add "<< tot<<endl;
	if (d==lim){
		cnt[k]++;
		return tot;
	}
	int p=tot;
	tr[p].l=build(k,d+1,lim);
	tr[p].r=build(k%3+1,d+1,lim);
	//cerr<< "l "<<trl<<endl;
	return p;
}

string dfs(int p,int d,int lim){
	if (d==lim){
		char s[2];
		s[0]=ch[tr[p].v];
		//cerr << "pos"<<p<<endl;
		//cerr <<"num"<< tr[p].v <<endl;
		s[1]='\0';
		//cerr << "test : "<<s[0]<<endl;
		return (string)s;
	}
	string s1=dfs(tr[p].l,d+1,lim);
	string s2=dfs(tr[p].r,d+1,lim);
	if (s1<s2) return s1+s2;
	else return s2+s1;
}

int main(){
	ch[1]='P';
	ch[2]='R';
	ch[3]='S';
	int tt;
	cin>>tt;
	for (int cs=1;cs<=tt;cs++){
		printf("Case #%d: ",cs);
		scanf("%d%d%d%d",&n,&a[2],&a[1],&a[3]);
		vector<string> ans;
		string str;
		for (int i=1;i<=3;i++){
			tot=0;
			cnt[1]=cnt[2]=cnt[3]=0;
			build(i,0,n);
			if (cnt[1]==a[1] && cnt[2]==a[2] && cnt[3]==a[3]){
				str=dfs(1,0,n);
				//cerr << "s = "<<str<<endl;
				ans.push_back(str);
			}
		}
		if (ans.size()==0) puts("IMPOSSIBLE");
		else{
			sort(ans.begin(),ans.end());
			cout<< ans[0] <<endl;
		}
		
	}

	return 0;
}