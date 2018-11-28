//============================================================================
// Name        : CodeJam1B.cpp
// Author      : Fabho
// Version     :
// Copyright   : Copyleft
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

bool isPal(int n){
	if(n<10)
		return true;
int nN = 0,copia = n,mo;
while(copia != 0){
  mo = copia%10;
  copia/=10;
  if(nN == 0)
	 nN = mo;
  else
	  nN = (nN * 10) + mo;
 }
if(n == nN)
	return true;
else
	return false;
}

int main() {
int casos,a,b,total,mini,maxi,cuad;
cin>>casos;
for(int h=1; h<=casos; h++)
   {
	cin>>a>>b;
	total = 0;
	mini = min(a,b);
	maxi = max(a,b);
	for(int x=mini; x<=maxi; x++)
	   {
		 if(isPal(x))
		   {
			 double cuad = sqrt(x);
			 int cuadInt = (int)cuad;
			 if(cuad -(double)cuadInt == 0.0)
			    {
				 if(isPal(cuadInt))
					 total++;

			    }
		   }
	   }
	cout<<"Case #"<<h<<": "<<total<<endl;
   }
return 0;
}
