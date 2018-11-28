#include<stdio.h>
int tcn,tc;
int ans;
int n,d;
int s[1001000];
int srange[1001000][2];
int p[2001000];
int m[1001000];
int cs,cm;
int as,am;
int rs,rm;
int main(){
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int i;
	scanf("%d",&tcn);
	for(tc=1;tc<=tcn;tc++){
		scanf("%d%d",&n,&d);
		scanf("%d%d%d%d",&s[0],&as,&cs,&rs);
		scanf("%d%d%d%d",&m[0],&am,&cm,&rm);
		d++;
		for(i=0;i<n;i++){
			s[i+1]=(((long long int)s[i])*as+cs)%rs;
			m[i+1]=(((long long int)m[i])*am+cm)%rm;
		}
		srange[0][0]=s[0];
		srange[0][1]=s[0]+d;
		for(i=1;i<n;i++){
			m[i]%=i;
			srange[i][0]=srange[m[i]][0];
			srange[i][1]=srange[m[i]][1];
			if(srange[i][0]<s[i])srange[i][0]=s[i];
			if(srange[i][1]>s[i]+d)srange[i][1]=s[i]+d;
		}
		for(i=0;i<n;i++){
			if(srange[i][0]<srange[i][1]){
				p[srange[i][0]]++;
				p[srange[i][1]]--;
			}
		}
		ans=0;
		int tans=0;
		for(i=0;i<rs+d+3;i++){
			tans+=p[i];
			if(ans<tans)ans=tans;
		}
		for(i=0;i<n;i++){
			if(srange[i][0]<srange[i][1]){
				p[srange[i][0]]--;
				p[srange[i][1]]++;
			}
		}
		printf("Case #%d: %d\n",tc,ans);
	}
}