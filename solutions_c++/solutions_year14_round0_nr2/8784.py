

/*
  ID:wilbeib1
  PROG:cookie
  LANG:C++
*/
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	//freopen("cookie.in","r",stdin);
	//freopen("cookie.out","w",stdout);
	int N;
	cin>>N;
	double C,F,X;
	for (int i = 0; i < N; ++i) {
		cin>>C>>F>>X;

		double sp = 2;
		double To = X;
		double time = 0;
		double Er = 0;
		while(To -Er > 10e-7) {
			
			double tmp = C/sp;
			time += tmp;
			Er += C;
			if( (To-Er)/sp > C/F){
				sp += F;
				Er -= C;
			}
			else {
				time += (To-Er)/sp;
				break;
			}
				
		}
		printf("Case #%d: %.7lf\n", i+1, time);
	}
	
	return 0;	  
}
