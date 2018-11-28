#include <iostream>
#include <fstream>
#include<vector>

using namespace std;

bool isPalinUtil(int N, int *copy){
	if(N>=0 && N<=9)
		return (N == (*copy)%10);
	if(!isPalinUtil(N/10, copy))
		return false;
	*copy /= 10;
	return (N%10 == (*copy)%10);
}
bool isPalin(int N){
	int *copy = new int(N);
	return isPalinUtil(N, copy);
}
int main(){
	fstream file;
	file.open("./C-small-attempt0.in", fstream::in);
	if(!file){
		cout << "Error opening input file\n";
		return 1;
	}
	vector<int>V;
	V.reserve(32);
	for(int i = 1; i<=32; ++i){
		if(isPalin(i))
			V.push_back(i*i);
	}
	vector<int> FairAndSquareNos;
	for(int i=0; i<V.size(); ++i)
		if(isPalin(V[i]))
			FairAndSquareNos.push_back(V[i]);
	int T, caseNo = 0;
	file >> T;
	while(T--){
		int A, B, count = 0;
		file >> A >> B;
		for(int i = 0;  i < FairAndSquareNos.size(); ++i)
			if(FairAndSquareNos[i] >= A && FairAndSquareNos[i] <= B)
				++count;
		cout << "Case #" << ++caseNo << ": " << count << "\n";
	}
	return 0;
}

