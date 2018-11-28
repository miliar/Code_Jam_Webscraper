#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
using namespace std;
int main(){
	ifstream in("input.txt");
	ofstream out("output.txt");
	int times;
	;
	in >> times;
	;
	for(int te = 1; te <= times; te++){
		int n;
		in >> n;
		int *arr = new int[n];
		;
		for(int i = 0; i < n; i++){
			in >> arr[i];
		}
		;
		long long int tot1 = 0;
		int max_diff = 0;
		for(int i = 0;i < n-1;i++){
			int diff = arr[i] - arr[i+1];
			if(diff > 0){
				tot1 += diff;
			}
			if(diff > max_diff){
				max_diff = diff;
			}
		}
		;
		long long int tot2 = 0;
		for(int i = 0;i < n-1;i++){
			tot2 += min(max_diff, arr[i]);			
		}
		out << "Case #" << te << ": " << tot1 << " " << tot2 << endl;
	}
}
			
