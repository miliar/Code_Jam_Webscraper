#include <stdio.h>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>

using namespace std;

#define ll long long
#define pi pair<int,int>
#define X first 
#define Y second
#define pb push_back
#define ab(x) ((x)<0?(-(x)):(x))
#define xx(x) ((x)*(x))
#define D 1000000007
#define Max (1<<30)
#define LLMAX (1ll<<60)
#define mp make_pair
#define MM 1000000000000000000ll
#define pss pair<string,string>
#define psi pair<string,int>
#define NN 3


int a[155][155];
int now[155][155];
int n,m;


bool can(int y,int x,int ck,int h){
	bool r=1;
	if(ck==0){
		for(int i=1;i<=m;i++)if(a[y][i]>h)r=0;
	}else{
		for(int i=1;i<=n;i++)if(a[i][x]>h)r=0;
	}

	return r;
}
int main(){
	freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);

	int t;
	cin>>t;
	int CC=0;
	while(t--){
		CC++;
		cin>>n>>m;

		memset(a,0,sizeof(a));
		memset(now,0,sizeof(now));

		for(int i=1;i<=n;i++)for(int j=1;j<=m;j++)cin>>a[i][j],now[i][j]=100;
		bool NO=0;
		for(int H=100;H>=1;H--){


			for(int i=1;i<=n;i++)for(int j=1;j<=m;j++){
				if(a[i][j]!=H)continue;
				
				if(now[i][j]!=a[i][j]){
					if(can(i,j,0,H)){

						for(int k=1;k<=m;k++)now[i][k]=H;

					}else if(can(i,j,1,H)){

						for(int k=1;k<=n;k++)now[k][j]=H;

					}else{
						NO=1;
					}
				}
			}
			if(NO)goto END;
		}
		END:;


		printf("Case #%d: ",CC);
		if(NO)cout<<"NO";
		else cout<<"YES";
		cout<<endl;
	}

}