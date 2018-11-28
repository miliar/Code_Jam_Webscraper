#include<iostream>
#include<iomanip>
#include<fstream>
using namespace std;

ifstream File("B-small-attempt0.in");
ofstream oFile("output.io");
double opti(double);
int i = 0, j = 0, t = 0, it = 0;
double c = 0, f = 0, x = 0;

int main(){
    oFile.precision(13);
    File>>t;
    for(it=0;it<t;it++){
        c = 0.0;
        f = 0.0;
        x = 0.0;
    	// oFile<<"Enter cookie amount to buy farm: ";
    	File>>c;
    	// oFile<<"Enter cookie rate increase: ";
    	File>>f;
    	// oFile<<"Enter cookie amount required to win: ";
    	File>>x;
    	oFile<<"Case #"<<it+1<<": "<<opti(2)<<endl;
    }
    // File>>i;
    return 0;
}

double opti(double cf){
	double s = 0.0, nf = 0.0;
	// double o1, o2;
    nf = f + cf;
    // oFile<<(x / cf)<<"::::"<<((c / cf)+(x / nf))<<endl;
	if((x / cf) > ((c / cf)+(x / nf))){ //Purchase is better option
        s = (c / cf) + opti(nf); //After purchase
        // oFile<<"::opt::"<<endl;
    }
    else{ //Wait it out
        s = x / cf;
    }
	return s;
}
