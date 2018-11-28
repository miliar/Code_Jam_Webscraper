#include <cstdio>
#include <string>
using namespace std;
int T;
int Ti;
int n, k;
string a,s;
char xmp[10010];
int mult(int xx, int yy)
{
	int tmp,buh=1,ho=1;
	int x=xx,y=yy;
	if(xx<0)
	{
		ho=-1;
		x=-xx;
	}
	if(yy<0) {
		buh=-1;
		y=-yy;
	}
	if(x==1) tmp = y;
	else if(x==2)
	{
		if(y==1) tmp = x;
		if(y==2) {buh=-1;tmp=1;}
		if(y==3) tmp=4;
		if(y==4) {buh=-1;tmp=3;}
	}
	else if(x==3)
	{
		if(y==1) tmp = x;
		if(y==2) {buh=-1;tmp=4;}
		if(y==3) {buh=-1;tmp=1;}
		if(y==4) tmp=2;
	}
	else if(x==4)
	{
		if(y==1) tmp = x;
		if(y==2) tmp=3;
		if(y==3) {buh=-1;tmp=2;}
		if(y==4) {buh=-1;tmp=1;}
	}
	return ho*buh*tmp;
}
int main()
{
	scanf("%d",&T);
	for(Ti=1;Ti<=T;Ti++)
	{
		scanf("%d%d",&n,&k);
		scanf("%s",xmp);
		int i;
		a = xmp;
		s.clear();
		for(i=0;i<k;i++)
		{
			s += a;
		}
		int l = s.length();
		int stat,targ;
		if(s[0]=='1') stat=1;
		else if(s[0]=='i') stat=2;
		else if(s[0]=='j') stat=3;
		else stat=4;
		int flag=0;
		if(stat == 2) flag = 1;
		for(i=1;i<l;i++)
		{
			if(s[i]=='1') targ=1;
			else if(s[i]=='i') targ=2;
			else if(s[i]=='j') targ=3;
			else targ=4;
			stat = mult(stat, targ);
			if(flag==0)
			{
				if(stat == 2) flag = 1;
			}
			else if(flag==1)
			{
				if(stat == 4) flag = 2;
			}
		}
		if(flag == 2 && stat == -1)
		{
			printf("Case #%d: YES\n",Ti);
		} else printf("Case #%d: NO\n",Ti);
		memset(xmp,0,sizeof(xmp));
	}
	return 0;
}
