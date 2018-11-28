#include <iostream>
#include <fstream>
using namespace std;
/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int cases;
	cin >> cases;
	unsigned long int mv;
	bool flag [10];
	bool done;
	int current;
	int tmp;
	ofstream fout ("countSheep.txt", ofstream::out);
	for (int i = 1; i <= cases; i++){
		cin >> mv;
		
		if (mv == 0){
			fout << "Case #"<<i<<": INSOMNIA"<<endl;
			continue;
		}
		for (int j = 0; j < 10; j++){
			flag[j] = false;
		}
		current = mv;
		do{
			done = true;
			tmp = current;
			while (tmp>0){
				flag[tmp%10] = true;
				tmp /= 10;
			}
			for (int j = 0; j < 10; j++){
				if (flag[j] == false){
					done = false;
					break;
				}
			}
			
			if (done){
				break;
			}
			else{
				current += mv;
			}
		}while (true);
		fout << "Case #"<<i<<": "<<current<<endl;
	}
	return 0;
}
