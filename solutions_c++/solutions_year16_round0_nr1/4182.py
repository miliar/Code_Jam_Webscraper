#include <iostream>
using namespace std;

int main(int argc, char ** argv){
	int n;
	int v;
	int orig;
	cin >> n;
	long list[10];
	for(int i = 0; i < n; i++){
		for(int k=0; k < 10; k++){
			list[k] = 0;
		}
		v = 0;
		cin >> orig;
		if(orig == 0){
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		int done = 0;
		while(done < 10){
			v+= orig;
			done = 0;
			int tmp = v;
			while(tmp != 0){
				list[(tmp % 10)]++;
				tmp /= 10;
			}
			for(int k = 0; k < 10; k++){
				if(list[k] != 0){
					done++;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << v << endl;
	}
}