#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

int main(int argc, char** argv) {
	ifstream in("A-large.in", ios::in);
    ofstream out("A-small.out");
    
    int x, digit,digits; int k=0;
	long long int value;
    long long int last = 0;
    long long int N = 0;
    bool f=1;
	in>>x;
	for(int i = 0; i < x; i++)
    {
	f=1;	k=0;
	int a[10] = {0,0,0,0,0,0,0,0,0,0};
        in>>N;
        if(N==0) {	
		out<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;
		continue;
		}
        
		while(f){
		value = N;
        digits = log10((float)N) + 1; //this determines the number of digits
        
	for (int j = digits - 1; j > 0; j--) {
	int divisor = pow((float)10, j);
	int digit = value / divisor;
	value -= digit * divisor;
    a[digit]=1;
}
a[value]=1;

		f=false;
        for (int m=0; m<10;m++)
        {
        	if(a[m]==0) f=true;
		}
        
        
        if (f){		
        k++;
		N= (k+1)*N/k;
}
}
		out<<"Case #"<<i+1<<": "<< N <<endl;
		}
		
    
    return 0;
}

