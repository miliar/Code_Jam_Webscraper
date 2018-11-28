#include<iostream>
#include<fstream>

using namespace std;

ifstream inFile("input.in");
ofstream outFile("output.out");

int senate(int* p, int n,int num){
	if(num>0){
		char out[3];
		int cnt = 0;
		int max = p[0];
		int pivot = 0;
		for(int i=0;i<n;i++){
			if(p[i]>max){
				max = p[i];
				pivot = i;
			}
		}
		--p[pivot];
		out[cnt]='A' + pivot;
		++cnt;
		max = p[pivot];
		if(num>1&&num!=3){
			for(int i=0;i<n;i++){
				if(p[i]>max){
					max = p[i];
					pivot = i;
				}
			}
			--p[pivot];
			out[cnt]='A' + pivot;
			++cnt;
		}
		out[cnt+1]='\0';
		outFile << out << " ";
		senate(p,n,num-cnt);
	}
	else
		return 0;

	return 0;
}


int main(void){

	int T;
	inFile >> T;
	int* result = new int[T];
	for(int i = 0;i<T;i++){
		int sum = 0;
		int n;
		inFile >> n;
		int* p = new int[n];
		outFile << "Case #"<<i+1<<": ";
		for(int j =0 ;j<n;j++){
			inFile >> p[j];
			sum += p[j];
		}
		senate(p,n,sum);
		outFile << endl;
	}
	return 0;
}
