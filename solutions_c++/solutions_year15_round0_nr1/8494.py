#include<iostream>
#include<fstream>
using namespace std;

#define LL long long
#define number(c) (c)-'0';

ifstream fin("A-large.in");
ofstream fout("small_A.out");
int main(void){
	int N;
	fin >> N;
	for(int t=1;t<=N;t++){

		int S,res = 0, sum = 0;
		char cnum;
		int num;

		fin >> S;
		for (int i = 0; i <= S; i++){
			fin >> cnum; 
			num = number(cnum);
			if (num>0&&sum < i){
				res += i-sum;
				sum = i;
			}
			sum += num;
		}
		fout << "Case #"<< t<<": "<< res << endl;

	}
}