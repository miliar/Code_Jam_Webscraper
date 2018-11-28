#include <stdio.h>
#include <string.h>


struct node
{
	int p,r,s;
	bool operator==(const node& rhs) const
	{
		return p==rhs.p && r==rhs.r && s==rhs.s;
	}
};

node p[20],r[20],s[20];;

char str[2][5000];
char tmp[5000];

char func[200][2];

void getfirst(char *pat,int len,int pos)
{
	if(len==1) return ;
	int len2=len>>1;
	getfirst(pat,len2,pos);
	getfirst(pat+len2,len2,pos+len2);
	if(strncmp(pat,pat+len2,len2)>0){
		strncpy(tmp,pat,len2);
		strncpy(pat,pat+len2,len2);
		strncpy(pat+len2,tmp,len2);
	}
}

int main()
{
	func['P'][0]='P';
	func['P'][1]='R';
	func['R'][0]='R';
	func['R'][1]='S';
	func['S'][0]='P';
	func['S'][1]='S';
	p[0].p=1;
	p[0].r=0;
	p[0].s=0;
	r[0].p=0;
	r[0].r=1;
	r[0].s=0;
	s[0].p=0;
	s[0].r=0;
	s[0].s=1;
	for(int i=1; i<20; i++){
		p[i].p=p[i-1].p+p[i-1].s;
		p[i].r=p[i-1].p+p[i-1].r;
		p[i].s=p[i-1].r+p[i-1].s;
		r[i].p=r[i-1].p+r[i-1].s;
		r[i].r=r[i-1].p+r[i-1].r;
		r[i].s=r[i-1].r+r[i-1].s;
		s[i].p=s[i-1].p+s[i-1].s;
		s[i].r=s[i-1].p+s[i-1].r;
		s[i].s=s[i-1].r+s[i-1].s;
	}
	int cas;
	scanf("%d",&cas);
	for(int T=1; T<=cas; T++){
		node inp;
		int n;
		scanf("%d %d %d %d",&n,&inp.r,&inp.p,&inp.s);
		if(inp==p[n]){
			str[0][0]='P';
			str[0][1]='R';
		}else if(inp==r[n]){
			str[0][0]='R';
			str[0][1]='S';
		}else if(inp==s[n]){
			str[0][0]='P';
			str[0][1]='S';
		}else{
			printf("Case #%d: IMPOSSIBLE\n",T);
			continue;
		}
		int now=0;
		for(int i=1; i<n; i++){
			for(int j=0; j<(1<<i); j++){
				str[1^now][j<<1]=func[str[now][j]][0];
				str[1^now][(j<<1)+1]=func[str[now][j]][1];
			}
			now^=1;
		}
		str[now][1<<n]='\0';
		getfirst(str[now],1<<n,0);
		printf("Case #%d: %s\n",T,str[now]);
	}
	return 0;
}
