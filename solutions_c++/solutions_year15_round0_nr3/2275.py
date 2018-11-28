#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<cctype>
#include<cstdio>
#include<string>
#include<sstream>
#include<cstring>
#include<cstdlib>
#include<fstream>
#include<iterator>
#include<iostream>
#include<algorithm>

using namespace std;

#pragma comment(linker,"/STACK:16777216")
#pragma warning(disable:4786)

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)<(b)?(a):(b))
#define myabs(a) ((a)<0?(-(a)):(a))
#define pi acos(-1.0)
#define CLR(a) memset(a,0,sizeof(a))
#define SET(a) memset(a,-1,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define ff first
#define ss second
#define eps 1e-9
#define root 1
#define lft 2*idx
#define rgt 2*idx+1
#define cllft lft,st,mid
#define clrgt rgt,mid+1,ed
#define inf (1<<29)
#define i64 long long
#define MX 1000002

typedef pair<int,int> pii;

void convert(char sa,char ma, char sb,char mb,char &sr,char &mr){
	sr='+';
	if(ma==mb){
		mr='1';
		if(ma!='1')sr='-';
	}
	else if(ma=='1')mr=mb;
	else if(mb=='1')mr=ma;
	else if(ma=='i'){
		if(mb=='j')mr='k';
		if(mb=='k')mr='j',sr='-';
	}
	else if(ma=='j'){
		if(mb=='i')mr='k',sr='-';
		if(mb=='k')mr='i';
	}
	else if(ma=='k'){
		if(mb=='i')mr='j';
		if(mb=='j')mr='i',sr='-';
	}
	if(sa!=sb){
		if(sr=='+')sr='-';
		else sr='+';
	}
}

bool func(string s,i64 l,i64 x){
	if(l*x<3)return false;
	char c='1',sign='+',rc,rs;
	i64 i,xx=x;
	//fprintf(stderr,"%s\n",s.c_str());
	for(i=0;i<l;i++){
		convert(sign,c,'+',s[i],sign,c);
		//fprintf(stderr,"%c%c\n",sign,c);
	}
	//fprintf(stderr,"%c%c\n",sign,c);
	rc='1';
	rs='+';
	while(xx){
		if(xx&1)convert(rs,rc,sign,c,rs,rc);
		convert(sign,c,sign,c,sign,c);
		xx>>=1;
	}

	//fprintf(stderr,"%c%c\n",rs,rc);
	if(!(rc=='1' && rs=='-'))return false;
	//printf("here\n");
	i64 cnt=0,flag=0;
	c='1';
	sign='+';
	while(cnt<100 && cnt<l*x){
		for(i=0;i<l;i++){
			convert(sign,c,'+',s[i],sign,c);
			cnt++;
			//printf("%c%c\n",sign,c);
			if(sign=='+' && c=='i')flag=1;
			else if(flag==1 && sign=='+' && c=='k' && l*x-cnt>0)return true;
		}
	}
	return false;
}

int main(){
	int cs,t=1;
	i64 l,x;
	string s;
	cin>>cs;
	while(cs--){
		cin>>l>>x>>s;
		printf("Case #%d: ",t++);
		if(func(s,l,x))printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}


