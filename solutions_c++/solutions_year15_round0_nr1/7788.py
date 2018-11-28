#include <iostream>
#include <cstdio>
using namespace std;
char s[1006];
int main ()
{
	freopen("A-large.in","r",stdin);
freopen("outputDeb.out","w",stdout);
  int t,n,inv,frnds,cntSt,cnt=1;
  cin>>t;
  while(t--) {
  	frnds=0;cntSt=0;
  	cin>>n;
  	cin>>s;
  	cntSt+=s[0]-'0';
  	for(int i=1;i<=n;i++) {
  		if(cntSt<i) {
  			inv=(i-cntSt);
  			cntSt=cntSt+inv+s[i]-'0';
  			frnds+=inv;
  		}
  		else {
  			cntSt+=s[i]-'0';
  		}
  	}
  	printf("Case #%d: %d\n",cnt,frnds);
  	cnt++;
  }

  return 0;
}
