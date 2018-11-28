#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <sstream>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;

unsigned long long calculate(vector<int>& coinjam, int base)
{
	unsigned long long decimalbase = 0;
	for ( int i = coinjam.size() - 1; i >= 0; i--)
		decimalbase += coinjam[i]*pow(base,i);
	return decimalbase;
}

bool checkComposite(vector<int>& coinjam, int base, vector<int>& divisors, int N)
{	
	if(base>10)
		return true;
	else {
		unsigned long long currValue = calculate(coinjam,base);
		//cout<<setprecision(100)<<currValue<<endl;
		for ( unsigned long long j = 2; j < sqrt(currValue); j++ ){
			if ( fmod(currValue,j) == 0 ){
				divisors.push_back(j);
				if ( checkComposite(coinjam , base+1, divisors, N) == true )
					return true;
				else return false;
			}
		}
	}
		return false;
}

int main()

{
    freopen("C-small.in","rt",stdin);
	freopen("C-small.out","wt",stdout);

    int T,N,J,counter=0;
    cin >> T;
    cin >> N >> J;
	cout << "Case #" << T << ":"<<endl;

	vector<int> coinjam;
	vector<int> divisors;
	
	unsigned long long range = 0,currValue = 0;
	for (int i = 0; i < N - 2; i++)
		range += pow (2,i);
	currValue = pow(2,N-1)+1;
	//cout<<range<<" "<<currValue<<endl;

	for (int i = 1; i <= range; i++){
		if(counter < J){
			int k=0;
			while ( currValue > 0 && k < N){
				coinjam.push_back(fmod(currValue,(double)2));
				currValue /= 2;
				k++;
			}
			
			if(checkComposite(coinjam,2,divisors,N) == true){
				counter++;
				for(int m = coinjam.size() - 1; m >= 0; m--)
					cout<<coinjam[m];
				
				for(int p = 0; p< divisors.size(); p++)
					cout<<" "<<divisors[p];
				cout<<endl;
			}
			currValue = pow(2,N-1)+1 + (2 * i);

			divisors.clear();
			coinjam.clear();
		}
		else break;
		
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;

}
