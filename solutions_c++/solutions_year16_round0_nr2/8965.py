#define LOCAL
#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<iostream>
#include <algorithm>
#include <string>
using namespace std;


int find(int N, int target){
	int count = 1;
	while (true)
	{
		int k = count*N;
		while (k > 0){
			if (k % 10 == target){
				//cout << target << " " << count*N << endl;
				return count*N;
			}
			k = k / 10;

		}
		count++;
	}

	return 0;
}


int main(){
	std::ios_base::sync_with_stdio(false);

#ifdef LOCAL
	freopen("B-large.in", "r", stdin);
	freopen("result.in", "w", stdout);
#endif
	int M;
	scanf("%d", &M);
	string name;
	getline(std::cin, name);
	for (int i = 1; i <= M; i++){    
		
		getline(std::cin, name);
		//cout << i<<" "<<name;
		int count = 0;

		for (int j = 1; j < name.length(); j++){
			if (name[j] != name[j - 1]) count++;

		}

		if (name[0] == '+') cout << "Case #" << i << ": " << (count+1)/2 * 2 << endl;
		if (name[0] == '-') cout << "Case #" << i << ": " << count / 2 *2+1 <<endl;

	}

	return 0;

}