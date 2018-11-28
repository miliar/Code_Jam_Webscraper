/*
ID: k.kamal1
PROG: test
LANG: C++     
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip> 
#include <string>

using namespace std;

int main() {
    ofstream fout ("o.out");
    ifstream fin ("in.in");
    int tetC;
    fin >> tetC;
    fout << fixed << setprecision(7);
    for(int cnt = 0; cnt < tetC; cnt++)
    {
    	double fRat = 2.0;
    	double curT = 0;
    	double curCok = 0;
    	double C, F, X;
    	fin >> C >> F >> X;
    	//cout << fabs(X - curCok) << endl;
    	//int cntV = 0;
    	while(X - curCok > .0000001)
    	{
    		/*cntV++;
    		if(cntV > 5)
    			break;*/
    	//	cout << " tryrty" << endl;
			double nxtH = (C - curCok) / fRat;
			double nxtT = (X - curCok) / fRat;
			//cout << nxtH << " nxH " << nxtT << " nxt " << endl;
			double nxtTVal;
			if(fabs(nxtT - nxtH) < .0000001)
			{
				//nxtTVal = curT + ((nxtT - curCok)*fRat);
				nxtTVal = nxtT;
				curCok += (nxtTVal) * fRat;
			}
			else if(nxtH - nxtT > 0.0000001) 
			{
				//nxtTVal = curT +  ((nxtT - curCok)*fRat);
				nxtTVal = nxtT;
				curCok += (nxtTVal) * fRat;
			}   
			else 
			{
				nxtTVal = nxtH;
				curCok += (nxtTVal) * fRat;
				double tk = (X - curCok + C) / (fRat + F);
				double wtk = (X - curCok) / (fRat);
				if(wtk - tk > 0.0000001 )
				{
					//nxtTVal = curT +  (((nxtH - curCok)*fRat));
					fRat += F;
					curCok -= C;	
				}
				else 
				{
					curT += nxtT;
					break;
				}
				
			} 
			curT += nxtTVal;
			//cout << curCok << " Cok " << endl; 
			//curT = nxtTVal;
		    		
    	}
    	cout << curT << endl;
		fout << "Case #" << cnt + 1 << ": ";
		fout << curT << endl;
    }
    //fout << a+b << endl;
    return 0;
}
