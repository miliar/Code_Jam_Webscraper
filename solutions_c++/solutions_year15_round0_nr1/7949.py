#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,c=1;
	freopen("A-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
	scanf("%d",&t);
	while( t-- ) {
	int n,i,j,ppl=0,ans=0,k;
	scanf("%d",&n);
	char s[10003];
	scanf("%s",s);
	for(i=0;i<=n;i++) {

	j = i;
	if(j<=ppl)	{
	ppl+=s[i]-'0';
	} else if(ppl<j) {
	k = j-ppl;
	ans += k;	
	ppl+=k+s[i]-'0';
	}
//	cout<<j<<" "<<ppl<<" "<<ans<<endl;
	}
	printf("Case #%d: %d\n",c++,ans);
	}
//	return 0;
	fclose(stdin);
	fclose(stdout);
	return 0;
}
	
