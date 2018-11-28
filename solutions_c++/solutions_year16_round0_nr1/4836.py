#include <iostream>
#include <fstream>

using namespace std;
int main() {
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t;
	fin >> t;
	int n,i,j;
	for(int test=1;test<=t;test++){
		fin >> n;
		if(n==0){
			fout << "Case #" << test << ": INSOMNIA" << endl;
			continue;
		}
		int seen = 0;
		int current=0,number;
		bool numbers[10];
		for(i=0;i<10;i++){
			numbers[i] = false;
		}
		for(i=1;;i++){
			
			seen = 0;
			for(j=0;j<10;j++){
				if(numbers[j]==true){
					seen++;
				}
			}
			if(seen==10){
				fout << "Case #" << test << ": " << (i-1)*n << endl;
				break;
			}
			current = n*i;
			while(current > 0){
				number = current%10;
				current = current/10;
				numbers[number] = true;
			}
		}
		
	}
	return 0;
}
