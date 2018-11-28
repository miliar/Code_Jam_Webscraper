#include<iostream>
#include<algorithm>
using namespace std;

typedef struct pairset {
	int a;
	int b;
};

bool cmp(pairset a, pairset b) {
	return a.b > b.b;
}

int main() {
	int cnt;
	cin >> cnt;
	for (int itr = 0; itr < cnt; itr++)
	{
		cout << "Case #" << itr + 1 << ": ";
		int num;
		pairset* input;
		cin >> num;
		int total = 0;
		input = new pairset[num];
		for (int i = 0; i < num; i++)
		{
			input[i].a = i;
			cin >> input[i].b;
			total = total + input[i].b;
		}
		char* result = new char[total];
		sort(input, input + num, cmp);
		int max = input[0].b;
		int idx = 0;
		while (max!=0) {
			for (int i = 0; i < num; i++)
			{
				if (max != input[i].b) {
					break;
				}
				result[idx] = 'A' + input[i].a;
				input[i].b--;
				idx++;
			}
			max--;
		}
		int start;
		if (total % 2 == 1) {
			start = 1;
			cout << result[0] << " ";
		}else{
			start = 0;
		}
		while (start<total) {
			cout << result[start] << result[start + 1] << " ";
			start = start + 2;
		}
		cout << endl;
	}
	return 0;
}