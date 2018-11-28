#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <cstring>
#include <fstream>
using namespace std;

int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-large.out");
	int jud[10];
	int N;
	fin >> N;
	int n;
	string t;
	int flag = 0;
	int ans;
	for (int i = 0; i < N; i++){
		memset(jud, 0, sizeof(jud));
		flag = 0;
		fin >> n;
		if (n == 0){
			fout << "Case #" << i + 1 << ": INSOMNIA"<< endl;
			continue;
		}
		int tem = n;
		int num;
		for (int k = 1; k < 100001; k++){
			tem = n;
			tem *= k;
			ans = tem;
			while (tem != 0){
				
				num = tem % 10;
				//cout << num<<" ";
				tem /= 10;
				if (jud[num] == 0){
					jud[num] = 1;
				}
			}
			//cout << endl;
			flag = 1;
			for (int j = 0; j < 10; j++){
			//	cout << jud[j] << " ";
				if (jud[j] == 0){
					flag = 0;
					break;
				}
			}
			//cout << endl;
			if (flag == 0){
				continue;
			}
			else{
				fout << "Case #" << i + 1 << ": " << ans << endl;
				break;
			}
		}
	}
	//system("pause");
	return 0;
}