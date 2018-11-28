#include<bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define nl printf("\n")
#define ll long long
#define FOR(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)

typedef pair<int,int> ii;
typedef pair<int,ii> iii;

inline int ini(){int temp;scanf("%d",&temp);return temp;}
inline ll inll(){ll temp;scanf("%lld",&temp);return temp;}
inline int stoi(string x){int temp;sscanf(x.c_str(),"%d",&temp);return temp;}
inline ll stoll(string x){ll temp;sscanf(x.c_str(),"%lld",&temp);return temp;}
inline string itos(int x){char temp[100];sprintf(temp,"%d",x);return temp;}
inline string lltos(ll x){char temp[100];sprintf(temp,"%lld",x);return temp;}
inline void outi(int x){printf("%d",x);}
inline void outll(ll x){printf("%lld",x);}
inline void OPEN(string a){freopen((a+".in").c_str(),"r",stdin);freopen((a+".out").c_str(),"w",stdout);}

#define ini ini()
#define inll inll()

int px[]={-1,0,1,0};
int py[]={0,1,0,-1};
int px8[]={-1,-1,0,1,1,1,0,-1};
int py8[]={0,1,1,1,0,-1,-1,-1};

#define ull unsigned long long

int main(){
	
	OPEN("AA");
	
	int T=ini;
	int TC=1;
	while(T--){
		set<ull> sull;
		ull x;scanf("%llu",&x);
		ull cop=x;
		int bit=0;
		printf("Case #%d: ",TC++);
		while(1){
			ull div=cop;
			while(div){
				int mod=div%10;

				bit|=(1<<mod);
				
				div/=10;
			}
				
			if(bit==((1<<10)-1)){
				printf("%llu\n",cop);
				break;
			}
			else if(!sull.insert(cop+=x).se){
				puts("INSOMNIA");
				break;
			}
		}
	}
}

