#include <iostream>
#include <cctype>
#include <algorithm>
#include <vector>
#include <ctime>
#include <cstdio>
#include <cmath>
#include <string>
#include <cstdlib>
#include <iomanip>
using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);//Entradas desde archivo.
	freopen("B-large.out", "w", stdout);//Salidas a archivo.
	int rep, flag;
	double c, f, x, seg, cps, aux1, aux2;
	
	cin>>rep;
	rep++;
	for(int j=1;j<rep;j++){
		cin>>c>>f>>x;
		seg=0;
		cps=2;
		flag=0;
		while(!flag){
		aux1=(c/cps)+(x/(cps+f));
		aux2=(x/cps);
		if(aux1<aux2){
			seg+=(c/cps);
			cps+=f;
		}
		else{
			seg+=(x/cps);
			flag=1;
		}
		}
		cout<<fixed<<setprecision(7)<<"Case #"<<j<<": "<<seg<<endl;
	}
	return 0;
}



