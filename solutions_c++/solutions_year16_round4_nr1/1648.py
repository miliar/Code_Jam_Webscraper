/*
* Filename:    A.cpp
* Created:     2016年05月29日 05时08分12秒 星期日
* Author:      JIngwei Xu [mail:xu_jingwei@outlook.com]
*
*/
#include<cstdio>
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<queue>
#include<stack>
#include<map>
#include<set>
#include<vector>
using namespace std;
typedef long long ll;

//Init Const
const int INF=1e9;
const int maxn=(1<<12)+7;
//Global Variables
int t,ans;
int N,R,P,S;
bool used[maxn];
int num[3];
//Function Declaration
int judge(int t){
	if(t>=0&&t<P)return 0;
	else if(t>=P&&t<P+R)return 1;
//	else if(t>=P+R&&t<P+R+S)return 2;
	return 2;
}
string ans_str;

int alls;
int fuck[maxn];
bool fids;
int jud(int a,int b){
	if(a==b)return -1;
	int failer=a+1;
	if(failer==3)failer=0;
	if(b==failer)return a;
	else return b;
}
bool check(){
	int cpy[15][maxn];
	int deep=0;
	for(int i=0;i<alls;i++){
		cpy[deep][i]=fuck[i];
	}
	deep++;
	for(int num=alls/2;num>=1;num/=2){
		for(int i=0;i<num;i++){
			int rs=jud(cpy[deep-1][i*2],cpy[deep-1][i*2+1]);
			if(rs==-1)return false;
			cpy[deep][i]=rs;
		}
		deep++;
	}
	return true;
}
void dfs(int pre,int t){
//	cout<<"pre:"<<pre<<" t:"<<t<<endl;
	if(fids)return;
	if(t==alls){
		if(check())fids=true;
		return;
	}
	if(pre==-1){
		if(num[0]<P){
			num[0]++;
			fuck[t]=0;
			dfs(0,t+1);
			if(fids)return;
			num[0]--;
		}
		if(num[1]<R){
			num[1]++;
			fuck[t]=1;
			dfs(1,t+1);
			if(fids)return;
			num[1]--;
		}
		
		if(num[2]<S){
			num[2]++;
			fuck[t]=2;
			dfs(2,t+1);
			if(fids)return;
			num[2]--;
		}
		
	}else if(pre==0){
		if(num[1]<R){
			num[1]++;
			fuck[t]=1;
			dfs(-1,t+1);
			if(fids)return;
			num[1]--;
		}
		
		if(num[2]<S){
			num[2]++;
			fuck[t]=2;
			dfs(-1,t+1);
			if(fids)return;
			num[2]--;
		}
	}else if(pre==1){
		if(num[0]<P){
			num[0]++;
			fuck[t]=0;
			dfs(-1,t+1);
			if(fids)return;
			num[0]--;
		}
		if(num[2]<S){
			num[2]++;
			fuck[t]=2;
			dfs(-1,t+1);
			if(fids)return;
			num[2]--;
		}
	}else if(pre==2){
		if(num[0]<P){
			num[0]++;
			fuck[t]=0;
			dfs(-1,t+1);
			if(fids)return;
			num[0]--;
		}
		if(num[1]<R){
			num[1]++;
			fuck[t]=1;
			dfs(-1,t+1);
			if(fids)return;
			num[1]--;
		}
	}
	
}
void solve(){
	alls=R+P+S;
	num[0]=num[1]=num[2]=0;
	fids=false;
	dfs(-1,0);
	if(!fids){
		printf("IMPOSSIBLE\n");
	}else{
		for(int i=0;i<alls;i++){
			if(fuck[i]==0){
				printf("P");
			}else if(fuck[i]==1){
				printf("R");
			}else if(fuck[i]==2){
				printf("S");
			}
		}
		printf("\n");
	}
}

//Main Program
int main()
{
#ifdef AC_THIS_PROBLEM
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
#endif
	scanf("%d",&t);
	for (int tcase = 1; tcase<=t; tcase += 1)
	{
		printf("Case #%d: ",tcase);
		scanf("%d%d%d%d",&N,&R,&P,&S);
		solve();
	}
	return 0;
}

