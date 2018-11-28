#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <tuple>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
  
int solve(){
	int n,m;
	char ss[10011];
	vector<string> s;
	scanf("%d%d%s",&m,&n,ss);
	int ln=strlen(ss);
	int f[9][9];
	int ff=0;
	for(int i=0;i<4;i++)f[0][i]=i;
	f[1][0]=1,f[1][1]=4,f[1][2]=3,f[1][3]=6;
	f[2][0]=2,f[2][1]=7,f[2][2]=4,f[2][3]=1;
	f[3][0]=3,f[3][1]=2,f[3][2]=5,f[3][3]=4;
	int a[10011],aa[10011];
	for(int i=0;i<ln;i++){
		if(ss[i]=='i')aa[i]=1;
		else if(ss[i]=='j')aa[i]=2;
		else aa[i]=3;
	}
	int nn=ln*n;
	for(int i=0;i<n;i++){
		for(int j=0,jj=i*ln;j<ln;j++){
			a[jj+j]=aa[j];
			//printf("%d",aa[j]);
		}
	}printf("\n");
	int ia[10011]={a[0]};
	bool af[10011]={0};
	vector<int> vi;
	if(ia[0]==1)vi.push_back(0);
	for(int i=1;i<nn;i++){ 
		ia[i]=f[ia[i-1]][a[i]];
		//printf("%d",ia[i]);
		if(af[i-1]){if(ia[i]>3)ia[i]-=4;else ia[i]+=4;}
		if(ia[i]>3){ia[i]-=4;af[i]=1;}
		else{af[i]=0;if(ia[i]==1)vi.push_back(i);}
	}
	vector<int> vj;
	//printf("\n");
	int aj[10011]={0};
	for(int ii=0,i=0;ii<vi.size();ii++){
		//printf("%d\n",vi[ii]);
		if((i=vi[ii]+1)>=nn)break;
		int nw=a[i];
		bool fb=0;
		if(nw==2)aj[i]=1;
		for(int j=i+1;j<nn;j++){
			nw=f[nw][a[j]];
			if(fb){if(nw>3)nw-=4;else nw+=4;}
			if(nw>3){fb=1;nw-=4;}
			else{fb=0;if(nw==2)aj[j]=1;}//vj.push_back(j);}
		}
	}
	for(int ii=0,i=0;ii<nn;ii++){//printf("%d\n",vj[ii]);
	if(!aj[ii])continue;
	//printf("%d\n",ii);
		if((i=ii+1)>=nn)break;
		int nw=a[i];
		bool fb=0;
		for(int j=i+1;j<nn;j++){
			nw=f[nw][a[j]];
			if(fb){if(nw>3)nw-=4;else nw+=4;}
			if(nw>3){fb=1;nw-=4;}
			else{fb=0; }
		}if(fb==0&&nw==3){printf("YES\n");return 0;}//printf("%d\n",ii); }
	} 
	printf("NO\n"); 
	return 0;
} 
int main(){
	
	freopen("R:\\a.in","r",stdin);
	freopen("R:\\a.out","w",stdout);
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		//printf("Case #%d: %f\n",solvea());
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}