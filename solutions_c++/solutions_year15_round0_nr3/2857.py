#include <cstdio>

using namespace std;
#define ll long long

char quartenion(char r, char c){
	char p;
	if(r=='1' && c=='1') p='1';
	if(r=='1' && c=='i') p='i';
	if(r=='1' && c=='j') p='j';
	if(r=='1' && c=='k') p='k';
	if(r=='i' && c=='1') p='i';
	if(r=='i' && c=='i') p='0';
	if(r=='i' && c=='j') p='k';
	if(r=='i' && c=='k') p='J';
	if(r=='j' && c=='1') p='j';
	if(r=='j' && c=='i') p='K';
	if(r=='j' && c=='j') p='0';
	if(r=='j' && c=='k') p='i';
	if(r=='k' && c=='1') p='k';
	if(r=='k' && c=='i') p='j';
	if(r=='k' && c=='j') p='I';
	if(r=='k' && c=='k') p='0';
	if(r=='0' && c=='1') p='0';
	if(r=='0' && c=='i') p='I';
	if(r=='0' && c=='j') p='J';
	if(r=='0' && c=='k') p='K';
	if(r=='I' && c=='1') p='I';
	if(r=='I' && c=='i') p='1';
	if(r=='I' && c=='j') p='K';
	if(r=='I' && c=='k') p='j';
	if(r=='J' && c=='1') p='J';
	if(r=='J' && c=='i') p='k';
	if(r=='J' && c=='j') p='1';
	if(r=='J' && c=='k') p='I';
	if(r=='K' && c=='1') p='K';
	if(r=='K' && c=='i') p='J';
	if(r=='K' && c=='j') p='i';
	if(r=='K' && c=='k') p='1';
	return p;
}

int main(){
	freopen("C-small-attempt2.in", "r", stdin );
	freopen("C-small-attempt2.out", "w", stdout );

	int t,i,l;
	ll x,a,b,c,d;
	bool possible=false,p1,p2;
	char s[10010],r1,r2,r3;

	scanf("%d ",&t);
	for(i=1;i<=t;i++){
		p1=false;
		p2=false;
		scanf("%d%lld%s",&l,&x,s);
		
		r1='1';
		r2='1';
		for(a=0;a<(x*l);a++){
			r1=quartenion(r1,s[a%l]);
			if(r1=='i')
				p1=true;
			if(p1 && r1=='k')
				p2=true;
		}
		printf(r1=='0'&&p1&&p2?"Case #%d: YES\n":"Case #%d: NO\n",i);
	}
}