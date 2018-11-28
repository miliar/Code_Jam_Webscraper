#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;


string intToString(int number)
{
   stringstream ss;
   ss << number;
   return ss.str();
}

int main(){
	int K;
	cin >> K;

	for(int k = 0; k< K; k++){
		long A,B, tot;
		tot = 0;
		cin >> A >> B;
		for (int i = A; i <= B; ++i)
		{
			bool isit = true;
			//is fair
			string number = intToString(i);
			for (int p = 0; p < number.length() / 2 ; ++p){
				if (number[p] != number[number.length()-1-p]){
						isit = false;                         
						break;
				}
			}

			if(!isit) continue;

			//is square
			double s = sqrt(i);
			if(s != (int)s){
				isit = false;
				continue;
			}

			if(!isit) continue;

			//is square fair
			string square = intToString((int)s);
			for (int p = 0; p < square.length() / 2 ; ++p){
				if (square[p] != square[square.length()-1-p]){
						isit = false;                             
						break;
				}
			}
			
			if(!isit) continue;
			tot++;
		}
		cout << "Case #" << k+1 << ": " << tot << endl;
	}
}