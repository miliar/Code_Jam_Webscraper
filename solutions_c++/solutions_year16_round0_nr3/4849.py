#include <stdio.h>
#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;

string updateCoin(string jamcoin)
{
	string newcoin = jamcoin;
	for( int i = newcoin.size() - 2; i > 0; i-- ) {
		if( newcoin[i] == '0' ) {
			newcoin[i] = '1';
			break;
		} else {
			newcoin[i] = '0';
		}
	}
	return newcoin;
}

bool divisor(string jamcoin, string &divstr)
{
	stringstream result;
	for( int n = 2; n <= 10; n++ ) {
		bool prime = true;
		unsigned long long coinnum = 0;
		unsigned long long base = 1;
		for( int i = jamcoin.size() - 1; i >=0 ; i-- ) {
			if( jamcoin[i] == '1' ) {
				coinnum += base;
			}
			base *= n;
		}
		int sum = 0;
		int tmp = coinnum;
		while( tmp ) {
			sum += tmp % 10;
			tmp /= 10;
		}
		unsigned long long upper = sqrt(coinnum);
		for( unsigned long long div = 2; div < upper; div++ ) {
			if( coinnum % div == 0 ) {
				result << div << " ";
				prime = false;
				break;
			}
		}
		if( prime ) {
			return false;
		}
	}
	divstr = result.str();
	return true;
}

string solve(int N, int J)
{
	int num = 0;
	string ans;
	string jamcoin = "1";
	for( int i = 1; i < N - 1; i++ ) {
		jamcoin += "0";
	}
	jamcoin += "1";

	while( num != J ) {
		string divstr;
		cout << jamcoin << endl;
		if( divisor(jamcoin, divstr) ) {
			ans += jamcoin;
			ans += ' ';
			ans += divstr;
			ans += '\n';
			cout << ans << endl;
			num++;
		}
		jamcoin = updateCoin(jamcoin);
	}
	return ans;
}

int main(int argc, char *argv[]) {

    int T, N, J;

    ifstream ifs(argv[1]);
    ofstream ofs(argv[2]);

    string line;
    std::getline(ifs, line);
    T = stoi(line);

    for( int i = 1; i <= T; i++ ) {
    	std::getline(ifs, line);
    	stringstream ss(line);
    	ss >> N >> J;
    	ofs << "Case #" << i << ": " << endl;
    	ofs << solve(N, J);
    }

    return 0;
}





