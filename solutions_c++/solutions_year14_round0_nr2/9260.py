#include <iostream>
using namespace std;
int T;
int main(){
	freopen("1in.txt","r",stdin);
	freopen("1out.txt","w",stdout);
	int T,i1;
	cin>>T;
	for(i1=0;i1<T;i1++){

		double X,C,F,t,min,t1,F0;
		int i=0;
		cin>>C>>F>>X;
		F0=F;
		t=X/2.0;
		double t0=t;
		min=t;
		t1=C/2.0;
		while(i<10000002){
			if(t<min)
				min=t;
			t=t1+X/(2.0+F);
			t1+=C/(2.0+F);
			F+=F0;
			i++;
		}
		printf("Case #%d: %.9lf\n",i1+1,min);
	}
    
}