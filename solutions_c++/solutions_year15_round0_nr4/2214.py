#include <cstdio>
#include <algorithm>
using namespace std;
bool solve()
{
	int x,r,c;
	scanf("%d%d%d",&x,&r,&c);
	if(x==4)return r+c>=7;
	if(x==1)return true;
	if(x==2)return r%2==0||c%2==0;
	if(c==3)swap(r,c);
	if(x==3)return r==3&&c>=2;
}
int main()
{
	freopen("/Users/Erona/Downloads/D-small-attempt3.in","r",stdin);
	freopen("/Users/Erona/Downloads/D-small-attempt3.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)printf("Case #%d: %s\n",i,solve()?"GABRIEL":"RICHARD");
	return 0;
}