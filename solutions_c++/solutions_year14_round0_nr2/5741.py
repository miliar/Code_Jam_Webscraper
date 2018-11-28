#include<iostream>

using namespace std;



double calc(double C, double X, double F, int R, int n){
	//cout << "      " ;
	double res = 0.;
	for(int i=1; i<=n; i++){
		res += ((double)C)/(R+F*(i-1));
		//cout << res << " - " ;
	}
	

	res += ((double)X)/(R+F*n);
//	cout << res << endl;
	return res;

}


int main(){
	int T;

	cin >> T;
	double C, F, X;
	for(int it=1; it<=T; it++){
		cin >> C >> F >> X;

		int nCookies = 0;
		double time = 0;			
		int rate = 2;
		double TimeTotalAnt = ((double)X)/rate;
		double TimeCompraAnt = ((double) C)/rate;

		int itAtual = 0;

		double atual = ((double)X)/rate;
		double antigo = 99999999999;		
		while(antigo - atual > 0.0000001){

			itAtual++;

			atual = calc(C, X, F, 2, itAtual);
			antigo = calc(C, X, F, 2, itAtual-1);
			//printf("%.7lf\n%.7lf\n", atual, antigo);
			
			

		}
		printf("Case #%d: %.7lf\n", it, antigo);



	}



}
