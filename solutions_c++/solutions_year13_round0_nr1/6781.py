# include <cstdio>
# include <cstring>
# include <cstdlib>
# include <ctime>
# include <iostream>
# include <cmath>
# include <string>
# include <algorithm>
# include <vector>
# define REP(i,n) for(int i=0;i<n;i++)
# define REP1(i,n) for(int i=1;i<=n;i++)
# define CLR(a,b) memset(a,b,sizeof(a))
# define For(i,a,b) for(int i=a;i<=b;i++)
# define Trv(p,a) for(int p=head[a];p;p=next[p])
# define INF 0x7FFFFFFF
# define vi vector<int>
# define it iterator
# define pb push_back
using namespace std;

typedef long long int64;
void setIO(string name){
	string	is=name+".in",
			os=name+".out";
	freopen(is.c_str(),"r",stdin);
	freopen(os.c_str(),"w",stdout);
}

char s[10][10];
int over(){
	REP(i,4)	REP(j,4)	if(s[i][j]=='.')	return 0;
	return 1;
}
int sum0[20],sum1[20];
int check(){
	CLR(sum0,0);CLR(sum1,0);
	REP(i,4){
		REP(j,4)	if(s[i][j]=='X')	sum0[i]++;
					else	if(s[i][j]=='O')	sum1[i]++;
					else	if(s[i][j]=='T')	sum0[i]++,sum1[i]++;
	}
	REP(i,4){
		REP(j,4)	if(s[j][i]=='X')	sum0[i+4]++;
					else	if(s[j][i]=='O')	sum1[i+4]++;
					else	if(s[j][i]=='T')	sum0[i+4]++,sum1[i+4]++;
	}
	REP(i,4)	if(s[i][i]=='X')	sum0[8]++;
				else	if(s[i][i]=='O')	sum1[8]++;
				else	if(s[i][i]=='T')	sum0[8]++,sum1[8]++;
	REP(i,4)	if(s[i][3-i]=='X')	sum0[9]++;
				else	if(s[i][3-i]=='O')	sum1[9]++;
				else	if(s[i][3-i]=='T')	sum0[9]++,sum1[9]++;
	REP(i,10)	if(sum0[i]==4)	return 1;
				else	if(sum1[i]==4)	return -1;
	return 0;
}

void work(){
	REP(i,4){
		scanf("%s",s[i]);
	}
	int v=check();
	if(v)	printf("%c won\n",v==1?'X':'O');
	else	if(over())	printf("Draw\n");
	else	printf("Game has not completed\n");
}

int main(){
	setIO("a");
	int casen;scanf("%d",&casen);
	REP1(i,casen)	printf("Case #%d: ",i),work();
	return 0;
}
