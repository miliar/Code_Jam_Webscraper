#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include<cstring>
#define pii pair<int,int>
#define mk make_pair
#define pb push_back 
#define ll long long
#define LB(v,x) lower_bound(v.begin(),v.end(),x)-v.begin()
#define UB(v,x) upper_bound(v.begin(),v.end(),x)-v.begin()
#define N 100
using namespace std;
char M[5][5];
bool falta=0;
int dx[]={0,1,1,1};
int dy[]={1,0,1,-1};

int doit(){
	for(int i=0;i<4;++i){
		for(int j=0;j<4;++j){
			for(int k=0;k<4;++k){
				int cero=0,equis=0,te=0;
				int nx=i,ny=j,ct=1;
				while(nx>=0 && nx<4 && ny>=0 && ny<4 && ct<=4){
					if(M[nx][ny]=='O')cero++;
					if(M[nx][ny]=='X')equis++;
					if(M[nx][ny]=='T')te++;
					nx=nx+dx[k],ny=ny+dy[k];
					ct++;
				}
				//cout<<i<<" "<<j<<" "<<k<<" --> "<<equis<<" "<<cero<<" "<<te<<endl;
				if(equis==4 || (equis==3 && te==1))return 1;
				if(cero==4 || (cero==3 && te==1))return 2;
			}
		}
	}
	if(falta==1){
		return 4;
	}
	else return 3;
}


int main(){
	int t;
	string s;
	cin>>t;
	for(int ii=0;ii<t;++ii){
		getline(cin,s);
		falta=0;
		for(int i=0;i<4;++i){
			getline(cin,s);
			for(int j=0;j<4;++j){
				M[i][j]=s[j];
				if(s[j]=='.')falta=1;
			}
		}
		int res=doit();
		printf("Case #%d: ",ii+1);
		if(res==1)puts("X won");
		if(res==2)puts("O won");
		if(res==3)puts("Draw");
		if(res==4)puts("Game has not completed");
		
	}
}










