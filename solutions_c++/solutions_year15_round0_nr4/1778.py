#include<iostream>
using namespace std;

int t;
int x,r,c;

bool solve(){
	scanf("%d%d%d",&x,&r,&c);
	if((r*c)%x)
		return false;
	if(x<=2)
		return true;
	if(x==3){
		if(r==1 || c==1)
			return false;
		else
			return true;
	}
	// x==4
	if(r<=2 || c<=2)
		return false;
	if(r%4 && c%4)
		return false;
	return true;
}


int main()
{
	freopen("D-small-attempt0.in","r",stdin);
	freopen("D-small-attempt0.out","w",stdout);
	scanf("%d",&t);
	for(int c=1;c<=t;c++){
		if(solve())
			printf("Case #%d: GABRIEL\n",c);
		else
			printf("Case #%d: RICHARD\n",c);
	}
	return 0;
}