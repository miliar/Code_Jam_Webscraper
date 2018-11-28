#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <math.h>
using namespace std;


 /*int sqrt(int x) {
        if (x==0) {return 0;}
        if (x==1) {return 1;}
        int x0 = 1;
        int x1;
        while (true){
            x1 = (x0+ x/x0)/2;
            if (abs(x1-x0)<1){return x1;}
            x0=x1;
        }
}*/

bool isp(long long num){
    long long resv=0;
    long long tmp = num;
    while (tmp!=0){
        resv= resv*10;
        resv = resv + tmp%10;
        tmp = tmp/10;
    }
    if (resv == num){return true;}
    else {return false;}
}

int main(){
	ifstream input;
	input.open("C-small-attempt1.in");
	ofstream output("output.txt");
    int casenum;
    input >>casenum;
	//for each case
	for (int k=0;k<casenum;k++){
        long long a;
        long long b;
        input >> a;
        input >> b;
        int count = 0;

        long long ar = ceil(sqrt(a));

        while (ar*ar <= b){
            if (isp(ar) && isp(ar*ar)){
                count++;
                //cout << ar*ar << endl;
            }
            ar++;
        }
        output << "Case #" << k+1 << ": " << count << endl;
    }
    input.close();
    output.close();
}
