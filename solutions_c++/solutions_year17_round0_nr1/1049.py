#include<bits/stdc++.h>
using namespace std;

char a[1005];

void f(int i,int k)
{
	for(int j=0;j<k;j++)
		a[i+j]=a[i+j]=='+'?'-':'+';
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,_,l,k,i,s;
	for(scanf("%d",&T),_=1;_<=T;_++)
	{
		scanf("%s%d",a,&k);
		l=strlen(a);
		for(s=i=0;i<=l-k;i++)
			if(a[i]=='-')
				f(i,k),s++;
		for(i=0;i<l;i++)
			if(a[i]=='-')
				break;
		if(i<l) printf("Case #%d: IMPOSSIBLE\n",_),fprintf(stderr,"Case #%d: IMPOSSIBLE\n",_);
		else printf("Case #%d: %d\n",_,s),fprintf(stderr,"Case #%d: %d\n",_,s);
	}
	return 0;
}
