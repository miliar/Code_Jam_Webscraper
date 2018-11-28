#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;
double speed,farm_cost,target,add;
bool buy() {
	double tmp1=farm_cost/speed+target/(speed+add);
	double tmp2=target/speed;
	if(tmp1<tmp2) return true;
	else return false;
}
int main() {
	freopen("B-large.in","r",stdin);
	freopen("Bwefqe.txt","w",stdout);
	int TT;
	scanf("%d",&TT);
	for(int TTT=1;TTT<=TT;TTT++) {
		speed=2.0;
		scanf("%lf%lf%lf",&farm_cost,&add,&target);
		double tot=0;
		while(buy()) {
			tot+=farm_cost/speed;
			speed+=add;
		}
		tot+=target/speed;
		printf("Case #%d: %.7lf\n",TTT,tot);
	}
	return 0;
}