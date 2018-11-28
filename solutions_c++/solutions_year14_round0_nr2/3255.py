#include <cstdio>
int poi=0;
double farmcost,farmproduction,want,waittime,buytime;
double acquiredfarm=0,cookiepersec=2;
double junejune;
int r;
void solve(){
	junejune=0;
	poi++;
	cookiepersec=2;
	acquiredfarm=0;
	scanf("%lf %lf %lf",&farmcost,&farmproduction,&want);
	while(1){
		cookiepersec=2+acquiredfarm*farmproduction;
		waittime=want/cookiepersec;
		buytime=farmcost/cookiepersec+want/(cookiepersec+farmproduction);
		//printf("%lf %lf\n",t,tt);
		if(buytime<waittime){
			junejune+=farmcost/cookiepersec;
			acquiredfarm++;
			continue;
		}
		else{
			junejune+=waittime;
			break;
		}
	}
	printf("Case #%d: %.7lf\n",poi,junejune);
	return;
}
int main(){
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	scanf("%d",&r);
	while(r--) solve();
	return 0;
}