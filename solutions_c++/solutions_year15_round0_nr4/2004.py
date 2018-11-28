#include <cstdio>

using namespace std;
#define ll long long

int main(){
	freopen("D-small-attempt2.in", "r", stdin );
	freopen("D-small-attempt2.out", "w", stdout );

	int t,i,x,r,c,d;
	bool Richard=false;

	scanf("%d ",&t);
	for(i=1;i<=t;i++){
		Richard=false;
		scanf("%d%d%d",&x,&r,&c);
		d=r*c;
		if(d%x>0 || d<x || (x>2 && (c==1 || r==1)) || (c<x && r<x))
			Richard=true;
		else{
			switch (x){
			case 4:
				if(c==2 || r==2)
					Richard=true;
				break;
			case 5:
				if((c==2 && (r&1)) || (r==2 && (c&1)))
					Richard=true;
				break;
			case 6:
				if(c==2 ||r==2)
					Richard=true;
				if((c==6 && r==3) || (c==3 && r==6))
					Richard=true;
				break;
			}
			if(x>=7)
				Richard=true;
		}	
		printf(Richard?"Case #%d: RICHARD\n":"Case #%d: GABRIEL\n",i);
	}
}