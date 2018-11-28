#include <iostream>
#include <fstream>

using namespace std;

int main(){

	ifstream ifs("A-small-attempt1.in");
	if (!ifs){
		cerr << "error!" << endl;
	}
	


	int times;
	ifs >> times;
	for (int loop = 0; loop < times; ++loop){
		int shyMax;
		int need=0;
		int sum=0;
		ifs >> shyMax;

		for (int shy = 0; shy < shyMax + 1; ++shy){
			char num;
			ifs >> num;
			int amount = atoi(&num);
			if (sum < shy){
				need += (shy - sum);
				sum = shy;
			}
			sum += amount;
		}
		cout << "Case #" << loop + 1 << ": " << need << endl;

	}
}