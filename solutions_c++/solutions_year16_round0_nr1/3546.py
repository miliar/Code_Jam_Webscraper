#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream ii("A-large.in");
	ofstream oo("o.out");
	int T;
	bool collect[10] = {false,false,false,false,false,false,false,false,false,false};
	ii >> T;
	unsigned long long  N[100];

	for (int i = 0;i < T;i++){
		ii >> N[i];
	}
	for (int i = 0; i < T;i++){
		if (N[i] == 0){
			oo << "Case #" << i+1 << ": INSOMNIA" << endl;
		}
		else {
			bool flag = false;
			int times = 1;
			unsigned long long res;
			while(!flag){
				unsigned long long temp = times * N[i];
				res = temp;
				while (temp != 0){
					int digit = temp %10;
					collect[digit] = true;
					temp  = temp/10;
				}
				flag = true;
				for (int i = 0;i<10;i++)
					flag = flag & collect[i];
				times ++;
			}
			oo << "Case #" << i+1 << ": "  << res << endl;
			for (int i = 0;i < 10;i++){
				collect[i] = false;
			}
		}
	}

}