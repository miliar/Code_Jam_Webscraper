#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <fstream>
using namespace std;

int main(){
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	int N;
	fin >> N;
	string t;
	int flag = 0;
	int ans;
	for (int i = 0; i < N; i++){
		fin >> t;
		ans = 0;
		if (t[0] == '+'){
			flag = 0;
		}
		else{
			flag = 1;
		}
		if (t.length() == 1){
			fout << "Case #" << i + 1 << ": "<< flag << endl;
		}
		else{
			for (int j = 1; j < t.length(); j++){
				if (t[j] == '+' && flag == 1){
					flag = 0;
					ans++;
				}
				else if (t[j] == '+' && flag == 0){
					//ans++;
				}
				else if (t[j] == '-' && flag == 1){

				}
				else if (t[j] == '-' && flag == 0){
					flag = 1;
					ans++;
				}
				else{

				}
			}
			if (t[t.length() - 1] == '-'){
				ans++;
			}
			fout << "Case #" << i + 1 << ": " << ans << endl;
		}
	}
	//system("pause");
	return 0;
}