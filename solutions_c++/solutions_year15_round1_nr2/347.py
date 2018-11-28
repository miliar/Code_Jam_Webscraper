#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

ifstream fin("2.in");
ofstream fout("2.out");

long long int mk[2000];
int barber;
long long int n, b;

long long int eval(long long int t){
	if(t<0)
		return 0;
	long long int result = 0;
	long long int barber = -1;
	for(int i=b-1;i>=0;i--){
		result += 2*(t/mk[i])+2;
		if(t % mk[i] == 0){
			barber = i;
		}
	}
	if(barber == -1){
		result += 1;
	}
	return result;
}

long long int binarySearch(long long int start, long long int end, long long int target){
	if(end - start == 1){
		long long int f1 = eval(start);
		if(f1 == target)
			return start;
		return end;
	}

	long long int mid = (start+end)/2;
	long long int f = eval(mid);
	if(f > target)
		return binarySearch(start, mid, target);
	else if(f < target)
		return binarySearch(mid, end, target);
	else
		return mid;
}



int main(){
	int nCases;
	fin >> nCases;
	for(int tt=1;tt<=nCases;tt++){

		fin >> b >> n;

		for(int i=0;i<b;i++){
			fin >> mk[i];
		}
		
		long long int t = binarySearch(0, 10e15, 2*n);
		long long int firstPersonToGo = eval(t-1)/2 + 1;

		long long int barber = -1;
		for(int i=0;i<b;i++){
			if(t % mk[i] == 0){
				if(firstPersonToGo == n){
					fout << "Case #" << tt << ": " << i+1 << endl;
					break;
				}
				else{
					firstPersonToGo++;
				}
			}
		}

	}
	return 0;
}