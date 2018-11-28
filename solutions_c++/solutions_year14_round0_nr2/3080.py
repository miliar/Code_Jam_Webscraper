#include <bits/stdc++.h>
using namespace std;

//DEFINITIONS

#define ll long long int
#define S(a) scanf("%d",&(a))
#define SL(a) scanf("%lld", &(a))
#define P(a) printf("%d",(a))
#define PL(a) printf("%lld",(a))
#define STR(a) scanf("%s",(a))
#define SP printf(" ")
#define NL printf("\n")
#define pb push_back
#define mp make_pair
#define MAX 100000005
#define mod 1000000007



int main(){
	double c,f,x,ans,t1,t2,curr,rate,t;
	int i,j,k,tt,tc;
	S(tt);
	//cout<<"hello";
	for(tc=1;tc<=tt;tc++){
		//cout<<"he";
		scanf("%lf%lf%lf",&c,&f,&x);
		curr=0;
		rate=2;
		ans=0;
		t=0;
		while(true){
			t1=(c/rate)+(x/(rate+f));
			t2=(x/rate);
			//cout<<t1<<" "<<t2<<endl;
			if(t1>t2){
				ans+=t2;
				break;
			}
			ans+=(c/rate);
			rate+=f;
		}
		printf("Case #%d: ",tc);
		printf("%.7lf",ans);
		NL;
	}
}