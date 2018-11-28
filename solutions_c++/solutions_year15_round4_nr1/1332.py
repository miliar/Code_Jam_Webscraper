#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<algorithm>
#include<cmath>
#include<climits>
#include<string>
#include<set>
#include<map>
using namespace std;
#define rep(i,n) for(int i=0;i<((int)(n));i++)
#define reg(i,a,b) for(int i=((int)(a));i<=((int)(b));i++)
#define irep(i,n) for(int i=((int)(n))-1;i>=0;i--)
#define ireg(i,a,b) for(int i=((int)(b));i>=((int)(a));i--)
typedef long long int lli;
typedef pair<int,int> mp;
#define fir first
#define sec second
#define IINF INT_MAX
#define LINF LLONG_MAX

int dx[4]={1,0,-1,0};
int dy[4]={0,1,0,-1};


int main(void){
	int qn;
	scanf("%d",&qn);
	reg(qq,1,qn){
		int w,h;
		char s[105][105]={};
		scanf("%d%d",&h,&w);
		reg(y,1,h){
			scanf("%s",&s[y][1]);
		}
		
		char conv[4]={'v','>','<','^'};
		reg(y,1,h){
			reg(x,1,w){
				bool f=false;
				rep(i,4){
					if(s[y][x]==conv[i]){
						s[y][x]=i;
						f=true;
					}
				}
			}
		}
		
		int wn[105]={};
		int hn[105]={};
		
		reg(y,1,h){
			reg(x,1,w){
				if(s[y][x]!='.'){
					hn[x]++;
					wn[y]++;
				}
				//printf("%d",[y][x]);
			}
			//printf("\n");
		}
		
		/*
		reg(i,1,h){
			printf("%d %d\n",wn[i],hn[i]);
		}
		*/
		
		bool ok=true;
		int ans=0;
		
		reg(x,1,w){
			ireg(y,1,h){
				if(s[y][x]!='.'){
					if(s[y][x]==0){
						if(wn[y]==1 && hn[x]==1)ok=false;
						else ans++;
					}
					break;
				}
			}
		}
		//printf("%d\n",ans);
		
		reg(y,1,h){
			ireg(x,1,w){
				if(s[y][x]!='.'){
					if(s[y][x]==1){
						if(wn[y]==1 && hn[x]==1)ok=false;
						else ans++;
					}
					break;
				}
			}
		}
		
		//printf("%d\n",ans);
		
		reg(y,1,h){
			reg(x,1,w){
				if(s[y][x]!='.'){
					if(s[y][x]==2){
						if(wn[y]==1 && hn[x]==1)ok=false;
						else ans++;
					}
					break;
				}
			}
		}
		//printf("%d\n",ans);
		
		reg(x,1,w){
			reg(y,1,h){
				if(s[y][x]!='.'){
					if(s[y][x]==3){
						if(wn[y]==1 && hn[x]==1)ok=false;
						else ans++;
					}
					break;
				}
			}
		}
		
		
		if(!ok){
			printf("Case #%d: IMPOSSIBLE\n",qq);
		}
		else{
			printf("Case #%d: %d\n",qq,ans);
		}
	}
	return 0;
}




