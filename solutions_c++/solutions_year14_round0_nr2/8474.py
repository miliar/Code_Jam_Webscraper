#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	
	int nNumOfTCs,nCurTC = 1;
	double fC,fF,fX;
	double fCurF = 2.0f;
	double fSeconds1= 0.0f,fSeconds2=0.0f,fTotSeconds = 0.0f,fPrevSeconds1=0.0,fPrevSeconds2= 0.0;
	
	cin  >> nNumOfTCs;
	while(nCurTC <= nNumOfTCs){
		cin >>fC>>fF>>fX;
		do{
			fPrevSeconds1 = fSeconds1;
			fSeconds1 += fX/fCurF;
			fPrevSeconds2 = fSeconds2;
			fSeconds2 += ((fC/fCurF) + (fX/(fCurF + fF)));

			if(fSeconds1 > fSeconds2){
				fSeconds1 = fPrevSeconds1 + (fC/fCurF);
				fSeconds2 = fPrevSeconds2 + (fC/fCurF);
				fCurF += fF;
			}
			else{
				break;
			}
		}while(1);
		
		cout<<"Case #"<<nCurTC<<": "<<std::setprecision(7)<<fSeconds1<<"\n"; 
		fSeconds1 = fSeconds2 = 0.0f;
		fTotSeconds = 0.0f;
		fCurF = 2.0f;
		nCurTC++;
	}
	return 0;
}
