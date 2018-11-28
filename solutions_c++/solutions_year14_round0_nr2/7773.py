#include<iostream>
#include<iomanip>

using namespace std;

long double c,f,x;
int t; 
long double res,dod_czas,act_v;

int main(){
	ios_base::sync_with_stdio(0);
	cin>>t;
	for(int q=1;q<=t;q++){
		cin>>c>>f>>x;
		
		res = x/2;
		
		dod_czas = c/2;
		act_v = 2 + f;
		
		while(dod_czas < res){
			if(res > (dod_czas + x/act_v)){
				res = (dod_czas + x/act_v);
			}
			dod_czas += c/act_v;
			act_v += f;
		}
		cout<<"Case #"<<q<<": "<<fixed<<setprecision(7)<<res<<endl;
	
	}

return 0;
}
