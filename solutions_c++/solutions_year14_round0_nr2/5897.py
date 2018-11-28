#include <cstdio>
#include <cstdlib>
using namespace std;

int main(){
	int casos;
	double costogranja,galletasextra,galletasparaganar;
	double tiempo1;
	double tiempo2;
	double cantgranjas;
	scanf("%d",&casos);
	bool bandera=false;
	double tiempo=0;
	for(int i=0;i<casos;i++){
		tiempo=0.00;
		bandera=false;
		double cantgranjas=0.0000000;
		scanf("%lf",&costogranja);
		scanf("%lf",&galletasextra);
		scanf("%lf",&galletasparaganar);

		while(bandera==false){
			tiempo1=tiempo+galletasparaganar/(2.0000000+(galletasextra*cantgranjas));
			tiempo2=tiempo+(costogranja/(2.0000000+(galletasextra*cantgranjas)))+ (galletasparaganar/(2.0000000+((galletasextra*(cantgranjas+1.00)))));
			if(tiempo1<=tiempo2){
				tiempo=tiempo1;
				bandera=true;
			}
			else {

				tiempo+=costogranja/(2.0000000+(galletasextra*cantgranjas));
				cantgranjas+=1.0000000;
			}
			
		}
		printf("Case #%d: %.7f",i+1,tiempo);
		if(i<casos-1)printf("\n");
	}



	return 0;
}