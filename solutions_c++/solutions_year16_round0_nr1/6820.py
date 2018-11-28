#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>    
#include <string>
using namespace std;
int not_all_true(int *a){
	for(int i = 0; i < 10; i++){
		if(!a[i]){
			cout << i<<endl;
			return 0;
		}
	}
	
	return 1;
}
int main()
{
	long long n, N;
	cin >> n;
	for(long long i = 0; i < n; i ++){
		cin >> N;
		if(N == 0){
			cout << "Case #";
			cout << i + 1;
			cout << ": INSOMNIA"<<endl;
			continue;
		}
		int a[10] = {0};
		int j = 0;
		while(1){
			int flag = 1;
			for(int i = 0; i < 10; i++){
				if(!a[i]){
					flag = 0;
					j += N;
					string line = to_string(j);
					for(std::string::iterator it = line.begin(); it != line.end(); ++it) {
						int int_to_remove = *it - '0';
						a[int_to_remove] = 1;
					}
					break;
				}
			}
			if(flag){
				break;
			}
		}
		cout << "Case #";
		cout << i + 1;
		cout << ": ";
		cout << j <<endl;
		
	}
	char c1 = 'a';
   return 0;
}
