#include <iostream>
#include <cstdio>
using namespace std;

void main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

	int nCase;
	cin>>nCase;

	cout.setf(ios::fixed);
	cout.precision(7);

	double fC, fF, fX;
	double fTimeTemp;
	double fTime1 = 0.f;
	double fTime2;

	double fTimeMin = 999999999999999.f;
	for(int caseIndex = 0 ; caseIndex < nCase ; caseIndex++)
	{
		cin>>fC>>fF>>fX;
		fTime1 = 0.f;
		fTimeMin = 999999999999999.f;
		for (int nC = 0 ; nC < 100001 ; nC++)
		{
			if(nC > 0){
				fTimeTemp = fC/(2.0f+((nC-1)*fF));
				fTime1 += fTimeTemp;//공장 만드는 시간
			}
			fTime2 = fX/(fF*nC+2.0f);//쿠키만드는 시간
			if(fTime1 + fTime2 > fTimeMin)
				break;
			else
				fTimeMin = fTime1 + fTime2;
		}
		cout <<"Case #"<<caseIndex+1<<": "<<fTimeMin<<endl;
	}
}