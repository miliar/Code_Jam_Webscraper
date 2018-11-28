#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <algorithm>
#include <iostream>
#include <assert.h>
#ifdef DM1_MACHINE	
	#include "template.cpp"
#endif

using namespace std;

#define SET(v,i) memset(v,i,sizeof(v));
#define FOR(i,n,k) for(int i=n;i<k;++i)
#define RI(i) scanf("%d",&i);
#define RS(i) scanf("%s",i);
#define RF(i) scanf("%lf",&i);
#define RL(i) scanf("%lld",&i);

const int INF=0x3F3F3F3F;
const int MAXN=100001;
typedef long long int i64;
typedef pair<int,int> pii;
typedef pair<string,int> psi;
void mirror(string &a,int pos_mirr){
	for(int i=0;i<pos_mirr;i++){
		a[a.size()-1-i]=a[i];
	}
}
void work(string &num, int pos1, int pos2) {
	if (pos1 < 0) {
		num[num.size()-1] = '1';
		num.insert(num.begin(), '1');
		return;
   	} else if (int(num[pos1]-48) < 9) {
      		num[pos1]=char(int(num[pos1]+1));
			num[pos2]=num[pos1];
      		return;
   	} else {
     		num[pos1] = '0';
			num[pos2] = '0';
      		work(num, pos1-1, pos2+1);
      		return;
   	}
}
bool comp(string v1, string v2) {
	if (v1.size() != v2.size()) 
		return v1.size() < v2.size();
	for (int i = 0; i < (int)v1.size(); i++)
		if (v1[i] != v2[i])
			return v1[i] < v2[i];
	return false;
}
void ultra_mirror(string &a){
	for(int i=0;i<(int)a.size()/2;i++){
		if(i==0) a[a.size()-1]=a[i];
		else{
			a[i]='0';
			a[a.size()-1-i]='0';
		}
	}
}
i64 palin(string str){
	int arr[10]={11,22,33,44,55,66,77,88,99,101};
	string str2;
	str2=str;
	if(str.size()>=3){
		mirror(str,str.size()/2);
		if(comp(str2,str)) ultra_mirror(str);
		while(!comp(str2,str)){
			if(str.size()%2!=0){
				work(str,str.size()/2,str.size()/2);
			}
			else{
				work(str,(str.size()/2)-1,str.size()/2);
			}
		}
		i64 n=0;
		FOR(i,0,(int)str.size()){
			n*=10;
			n+=(str[i]-48);
		}
		return n;
	}
	else{
		if(str.size()>=2){
			int i;
			for(i=0;i<10;i++){
				if(arr[i]-atoi(str.c_str())>0){
					break;
				}
			}
			return arr[i];
		}
		else{
			i64 n=0;
			FOR(i,0,(int)str.size()){
				n*=10;
				n+=(str[i]-48);
			}
			return n;
		}
	}
}

bool PP(string A){
	FOR(i,0,(int)A.size()){
		if(A[i]!=A[A.size()-i-1]) return false;
	}
	return true;
}

inline void solve(int test){
	int t; RI(t);
	vector<i64> P;
	i64 LIMIT=sqrt((1e14)+1);
	i64 k=0;
	char str[500];
	while(k<=LIMIT){
		sprintf(str,"%lld",k+1);
		k=palin(str);
		if(k<=LIMIT){
			sprintf(str,"%lld",k*k);
			if(PP(str)){
				//fprintf(stderr,"%lld\n",k*k);
				P.push_back(k*k);
				//fprintf(stderr,"--> %lld\n",P[P.size()-1]);
			}
		}
	}
	FOR(ic,1,t+1){
		i64 a,b; RL(a); RL(b);
		int i,j;
		i=j=0;
		while(i<(int)P.size() && P[i]<a) i++;
		while(j<(int)P.size() && P[j]<=b) j++;
		printf("Case #%d: %d\n",ic,j-i);
	}
}
int main(){
	freopen("FILE.in","r",stdin);
	freopen("FILE.out","w",stdout);
	solve(0);
	return 0;
}

////////////////////////////////////////////
/////////////Code by David Moran////////////
/////////////////////////////P=NP///////////

