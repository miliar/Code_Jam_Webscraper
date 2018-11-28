#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<iostream>
#include <cassert>
#include<map>
#include<queue>
#include<stack>
#include<time.h>
#include<math.h>
#include<set>
#include<complex>
using namespace std;
#define INF 0x3f3f3f3f
#define DINF 1e10
#define EPS 1e-15
#define PII acos(-1)
#define LL long long
#define Pii pair<int,int>
#define For(i,n) for(int i=0;i<n;i++)
#define ileer(n) scanf("%d",&n)
#define i2leer(n,m) scanf("%d %d",&n,&m)
#define fleer(n) scanf("%lf",&n)
#define f2leer(n,m) scanf("%Lf %Lf",&n,&m)
#define MK make_pair
#define PB push_back
#define llenar(arr,val) memset(arr,val,sizeof(arr))
#define VLL vector< LL >
#define matrix vector<VI >
#define F first
#define S second
#define MAXN 101
char cad[MAXN];
int main(){
	int t;
	ileer(t);
	For(c,t){
		scanf("%s",cad);
		string g=cad;
		int n=g.size();
		int can=0;
		while(true){
			int k=n-1;
			bool encontre=false;
			int pos;
			for(int i=n-1;i>=0;i--){
				if(g[i]=='-'){
					encontre=true;
					pos=i;
					break;
				}
			}
			//cout<<pos<<endl;
			if(!encontre){
				break;
			}
			
			for(int i=pos;i>=0;i--){
				g[i]=g[i]=='-'?'+':'-';
			}
			can++;
			//cout<<g<<endl;
		}
		printf("Case #%d: %d\n",c+1,can);
		
		
		
		
		
		
		
	}
}