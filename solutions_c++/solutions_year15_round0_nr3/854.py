//#include <stdio.h>
//#include <fstream>
//
//using namespace std;
//
//ifstream fin("2.in");
//ofstream fout("2.out");
//
//char str[100000];
//
//long long int mul[5][5];
//
//const long long int i = 2;
//const long long int j = 3;
//const long long int k = 4;
//
//
//
//long long int multiply(long long int x, long long int y){
//	bool neg = false;
//	if(x<0){
//		neg = !neg;
//		x = -x;
//	}
//	if(y<0){
//		neg = !neg;
//		y = -y;
//	}
//	return (neg?-1:1)*mul[x][y];
//}
//
//long long int conv[256];
//
//long long int main(){
//mul[1][1] = 1;
//mul[1][i] = i;
//mul[1][j] = j;
//mul[1][k] = k;
//mul[i][1] = i;
//mul[j][1] = j;
//mul[k][1] = k;
//mul[i][i] = -1;
//mul[i][j] = k;
//mul[i][k] = -j;
//mul[j][j] = -1;
//mul[j][k] = i;
//mul[j][i] = -k;
//mul[k][k] = -1;
//mul[k][j] = -i;
//mul[k][i] = j;
//conv['1'] = 1;
//conv['i'] = i;
//conv['j'] = j;
//conv['k'] = k;
//
//	long long int nCases;
//	fin >> nCases;
//	for(long long int t=1;t<=nCases;t++){
//		long long int x, l;
//		fin >> l >> x;
//		long long int total = 1;
//		for(long long int i=0;i<l;i++){
//			fin >> str[i];
//			total = multiply(total, conv[str[i]]);
//		}
//
//		long long int totaltotal = 1;
//		for(long long int i=0;i<(x%4);i++){
//			totaltotal = multiply(totaltotal, total);
//		}
//
//		if(totaltotal != -1){
//			fout << "Case #" << t << ": " << "NO" << endl;
//			continue;
//		}
//
//		bool found = false;
//		long long int rep = max(x,25);//24, but 25 for good measure
//		long long int iter;
//		total = 1;
//
//		for(iter=0;iter<rep*l;iter++){
//			total = multiply(total, conv[str[iter%l]]);
//			if(total == i){
//				found = true;
//				iter++;
//				break;
//			}
//		}
//		if(!found){
//			fout << "Case #" << t << ": " << "NO" << endl;
//			continue;
//		}
//		
//		total = 1;
//		for(;iter<rep*l;iter++){
//			total = multiply(total, conv[str[iter%l]]);
//			if(total == j){
//				found = true;
//				iter++;
//				break;
//			}
//		}
//		if(!found){
//			fout << "Case #" << t << ": " << "NO" << endl;
//			continue;
//		}
//		
//		total = 1;
//		for(;iter<rep*l;iter++){
//			total = multiply(total, conv[str[iter%l]]);
//			if(total == k){
//				found = true;
//				iter++;
//				break;
//			}
//		}
//		if(!found){
//			fout << "Case #" << t << ": " << "NO" << endl;
//			continue;
//		}
//		fout << "Case #" << t << ": " << "YES" << endl;
//	}
//	return 0;
//}

#include <stdio.h>
#include <fstream>

using namespace std;

ifstream fin("2.in");
ofstream fout("2.out");

char str[100000];

long long int mul[5][5];

const long long int i = 2;
const long long int j = 3;
const long long int k = 4;



long long int multiply(long long int x, long long int y){
	bool neg = false;
	if(x<0){
		neg = !neg;
		x = -x;
	}
	if(y<0){
		neg = !neg;
		y = -y;
	}
	return (neg?-1:1)*mul[x][y];
}

long long int conv[256];

int main(){
mul[1][1] = 1;
mul[1][i] = i;
mul[1][j] = j;
mul[1][k] = k;
mul[i][1] = i;
mul[j][1] = j;
mul[k][1] = k;
mul[i][i] = -1;
mul[i][j] = k;
mul[i][k] = -j;
mul[j][j] = -1;
mul[j][k] = i;
mul[j][i] = -k;
mul[k][k] = -1;
mul[k][j] = -i;
mul[k][i] = j;
conv['1'] = 1;
conv['i'] = i;
conv['j'] = j;
conv['k'] = k;

	long long int nCases;
	fin >> nCases;
	for(long long int t=1;t<=nCases;t++){
		long long int x, l;
		fin >> l >> x;
		long long int total = 1;
		for(long long int i=0;i<l;i++){
			fin >> str[i];
			total = multiply(total, conv[str[i]]);
		}

		long long int totaltotal = 1;
		for(long long int i=0;i<(x%4);i++){
			totaltotal = multiply(totaltotal, total);
		}

		if(totaltotal != -1){
			fout << "Case #" << t << ": " << "NO" << endl;
			continue;
		}

		bool found = false;
		long long int rep = min(x,(long long)25);//24, but 25 for good measure
		long long int iter;
		total = 1;

		for(iter=0;iter<rep*l;iter++){
			total = multiply(total, conv[str[iter%l]]);
			if(total == i){
				found = true;
				iter++;
				break;
			}
		}
		if(!found){
			fout << "Case #" << t << ": " << "NO" << endl;
			continue;
		}
		
		found = false;
		total = 1;
		for(;iter<rep*l;iter++){
			total = multiply(total, conv[str[iter%l]]);
			if(total == j){
				found = true;
				iter++;
				break;
			}
		}
		if(!found){
			fout << "Case #" << t << ": " << "NO" << endl;
			continue;
		}
		
		found = false;
		total = 1;
		for(;iter<rep*l;iter++){
			total = multiply(total, conv[str[iter%l]]);
			if(total == k){
				found = true;
				iter++;
				break;
			}
		}
		if(!found){
			fout << "Case #" << t << ": " << "NO" << endl;
			continue;
		}
		fout << "Case #" << t << ": " << "YES" << endl;
	}
	return 0;
}