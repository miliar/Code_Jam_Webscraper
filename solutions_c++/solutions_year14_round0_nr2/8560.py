#include<cstdio>
#include<map>
#include<queue>
#include<vector>
using namespace std;
priority_queue<double, vector<double>, greater<double> > asd;
int main(){
	int u;
	  freopen ("girdi.txt","r",stdin);
	  freopen ("sonuc.txt","w",stdout);

	double tot=2.0,a,b,c,t,syc=0;
	scanf("%d",&u);
	for(int i=1;i<=u;i++){
		tot=2.0; syc=0;
		while(!asd.empty()) asd.pop();
	scanf("%lf %lf %lf",&a,&b,&c);
	asd.push(c/(double)2.0);
	t=c/2.0;
	while(syc<=t){
	//printf("%lf %lf %lf\n",syc,t,asd.top());
	syc+=a/tot;		if(syc>asd.top()) break;

	tot+=b;
	asd.push(syc+c/tot);
	}
	
	printf("Case #%d: %lf\n",i,asd.top());
}
}
