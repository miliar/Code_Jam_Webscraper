#include <iostream>
#include <fstream>
using namespace std;

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int i=1; i<=T; i++){
		double X, C, F, time=0;
		int N=0;
		scanf("%lf%lf%lf", &C, &F, &X);
		//test range: step ~ step*10
		if(X/2 <= (X/(2+F)+C/2)){
		    N = 0;
		}
		else{
		    int step = 1;
		    while( X/(2+F*step) > (X/(2+F+F*step)+C/(2+F*step)) ){
                step *= 10;
            }
            if( X/(2+F*step-F) > (X/(2+F*step)+C/(2+F*step-F)) ){   //N =step*10^n
                N = step;
            }
            else{
                step /= 10;
                while(step){
                    N += step;
                    if( X/(2+F*N) < (X/(2+F*(N+1))+C/(2+F*N)) ){
                        if(step > 1){
                            N -= step;
                            step /= 10;
                        }
                        else{
                            break;
                        }
                    }
                }
            }
		}

		//calculate time
		for(int j=0; j<N; j++){
			time += C/(2+F*j);
		}
		time += X/(2+F*N);

		char *c1 = "Case #";
		char *c2 = ": ";
		printf("%s%d%s%.7lf\n", c1, i, c2, time);
	}

	return 0;
}
