#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define MP make_pair
#define PB push_back

using namespace std;

using ll = long long;

int read(){
	int i;
	scanf("%d",&i);
	return i;
}

const int Nmax=12;
int rpsCount[Nmax+1][3][3];
char minStr[Nmax+1][3][(1<<Nmax)+1];

int battle[3][2]={{0,2},{1,0},{2,1}};

void Prepare(){
	int n=Nmax;
	rpsCount[0][0][0]=1;
	rpsCount[0][1][1]=1;
	rpsCount[0][2][2]=1;
	for(int i=1;i<=n;i++){
		REP(j,3)
			REP(k,3)
				rpsCount[i][j][k]=rpsCount[i-1][battle[j][0]][k]
									+rpsCount[i-1][battle[j][1]][k];
	}
	minStr[0][0][0]='R';
	minStr[0][1][0]='P';
	minStr[0][2][0]='S';
	for(int i=1;i<=n;i++){
		REP(j,3){
			char *s1=minStr[i-1][battle[j][0]],*s2=minStr[i-1][battle[j][1]];
			if(strcmp(s1,s2)>0)
				swap(s1,s2);
			strcpy(minStr[i][j],s1);
			strcpy(minStr[i][j]+(1<<(i-1)),s2);
		}
	}
}

void Solve(int caseNumber){
	int n=read(),r=read(),p=read(),s=read();
/*	cout<<n<<endl;
	cout<<minStr[n][1]<<endl;
	cout<<rpsCount[n][1][0]<<endl;
	cout<<rpsCount[n][1][1]<<endl;
	cout<<rpsCount[n][1][2]<<endl;*/
	int type=-1;
	REP(i,3)
		if(rpsCount[n][i][0]==r
		&& rpsCount[n][i][1]==p
		&& rpsCount[n][i][2]==s)
			type=i;
	printf("Case #%d: ",caseNumber);
	if(type==-1)
		printf("IMPOSSIBLE\n");
	else
		printf("%s\n",minStr[n][type]);
}

int main(){
	Prepare();
	int t=read();
	REP(caseNumber,t){
		Solve(caseNumber+1);
	}
}