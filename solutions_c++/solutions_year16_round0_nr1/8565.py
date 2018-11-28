#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int numbers[10] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
bool check();
void find(int);
void clear();

int main(){
	ifstream file;
	file.open("A-large.in");
	
	ofstream outFile;
	outFile.open("output.txt");
	
	int a;
	file >> a;
	int b[a];
	for(int i = 0; i < a; i++)
		file >> b[i];
	
	for(int i = 0; i < a; i++){
		if(b[i] == 0){
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			outFile << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;		
		}

		else{
			for(int j = 1; j <= 2147483647; j++){
				find((b[i] * j));				
				
				if(check()){
					cout << "Case #" << i + 1 << ": " << b[i] * j << endl;
					outFile << "Case #" << i + 1 << ": " << b[i] * j << endl;
					break;				
				}
			}
			clear();
		}
	}
	file.close();
	outFile.close();
	return 0;
}
//[]
//{}

void find(int a){
	int b;
	for(int i = 0; a > 0;i++){
		b = a % 10;
		numbers[b] = b;
		a = a/10;
	}
}

bool check(){
	bool b = true;
	for(int i=0; i < 10; i++){
		if(numbers[i] != i){
			b = false;
		}
	}
	return b;
}

void clear(){
	for(int i = 0; i < 10; i++)
		numbers[i] = -1;
}
