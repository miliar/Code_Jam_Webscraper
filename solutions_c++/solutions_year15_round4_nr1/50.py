#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<string>
#include<stack>
#include<cstdio>
#include<cmath>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int,int> P;
typedef pair<int,P> P1;

#define fr first
#define sc second
#define mp make_pair
#define pb push_back
#define rep(i,x) for(int i=0;i<x;i++)
#define rep1(i,x) for(int i=1;i<=x;i++)
#define rrep(i,x) for(int i=x-1;i>=0;i--)
#define rrep1(i,x) for(int i=x;i>0;i--)
#define sor(v) sort(v.begin(),v.end())
#define rev(s) reverse(s.begin(),s.end())
#define lb(vec,a) lower_bound(vec.begin(),vec.end(),a)
#define ub(vec,a) upper_bound(vec.begin(),vec.end(),a)
#define uniq(vec) vec.erase(unique(vec.begin(),vec.end()),vec.end())
#define mp1(a,b,c) P1(a,P(b,c))

const int INF=1000000000;
const int dir_4[4][2]={{1,0},{0,1},{-1,0},{0,-1}};
const int dir_8[8][2]={{1,0},{1,1},{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1}};

int main(){
	int T;
	cin >> T;
	rep1(ppp,T){
		printf("Case #%d: ",ppp);
		
		int r,c;
		char a[102][102];
		bool b[102][102][4];
		scanf("%d%d",&r,&c);
		rep(i,r){
			scanf("\n");
			rep(j,c){
				scanf("%c",&a[i][j]);
				rep(k,4){
					b[i][j][k] = false;
				}
			}
		}
		
		rep(i,r){
			rep(j,c){
				if(a[i][j] != '.'){
					b[i][j][3] = true;
					break;
				}
			}
			rrep(j,c){
				if(a[i][j] != '.'){
					b[i][j][1] = true;
					break;
				}
			}
		}
		rep(j,c){
			rep(i,r){
				if(a[i][j] != '.'){
					b[i][j][0] = true;
					break;
				}
			}
			rrep(i,r){
				if(a[i][j] != '.'){
					b[i][j][2] = true;
					break;
				}
			}
		}
		
		int ret = 0;
		rep(i,r){
			rep(j,c){
				if(a[i][j] == '.')continue;
				int t;
				if(a[i][j] == '^')t = 0;
				else if(a[i][j] == '>')t = 1;
				else if(a[i][j] == 'v')t = 2;
				else if(a[i][j] == '<')t = 3;
				if(b[i][j][t]){
					ret ++;
					if(b[i][j][0] && b[i][j][1] && b[i][j][2] && b[i][j][3]){
						puts("IMPOSSIBLE");
						goto NEXT;
					}
				}
			}
		}
		printf("%d\n",ret);
		NEXT:;
	}
}
			
