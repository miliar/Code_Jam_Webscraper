#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;


void get_digits(std::vector<int>& d, unsigned long num) {
    if (num > 9) {
        get_digits(d, num / 10);
    }
    d.push_back(num % 10);
}

int main(int argc, char* argv[]) {
	int t;
	int n;
	int nn;
	int tot = 0;
	int done;
	std::vector<int> d;
//	int c[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

	
	freopen("input_file.in","r",stdin);
	freopen("output_file.out","w",stdout);
	cin >> t;

	for(int i = 0; i < t; i++){
		cin >> n;
		if(n == 0){
			cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			continue;
		}
		done = 0;
		tot = 0;
		d.clear();
		int c[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
		for(nn = 0; done < 10; ){
			nn += n;
		//	cout << "no Case #" << done << endl;
			get_digits(d, nn);
			tot++;
			for(int j = 0; j < d.size(); j++){				
				c[d[j]]++;				
			}
			done = 0;
			for(int k = 0; k < 10; k++){
				//cout << ' ' << c[k] << endl;
				if(c[k] > 0){
					done++;
				}
			}
		//	cout << "1 Case #" << nn << endl;
			
		}
		cout << "Case #" << i + 1 << ": " << nn << endl;
	}
	return 0;
}
