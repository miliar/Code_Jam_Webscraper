#include <cstdio>

using namespace std;

int ile;
double koszt, bonus, dozdob, persek, suma, czas, minim;

int main(){
	scanf("%d", &ile);
	for(int q=1; q<=ile; q++){
		scanf("%lf %lf %lf", &koszt, &bonus, &dozdob);
		suma=0; persek=2; czas=0;
		minim=dozdob/2.0;
		while(true){
			czas+=(koszt/persek);
			persek+=bonus;
			if((dozdob/persek)+czas > minim)
			{
				printf("Case #%d: %.7lf\n",q,minim);
				break;
			}
			else
				minim=(dozdob/persek)+czas;
		}
	}
	return 0;
}
