#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>

using namespace std;

int alphabet[100];
char input[2002];
vector<char> res;
int ptr;

void zero() {
	if (alphabet['Z'] && alphabet['E'] && alphabet['R'] && alphabet['O']) {
		alphabet['Z']--;
		alphabet['E']--;
		alphabet['R']--;
		alphabet['O']--;
		res.push_back(0);
		zero();
	}
}
void one() {
	if (alphabet['O'] && alphabet['N'] && alphabet['E']) {
		alphabet['O']--;
		alphabet['N']--;
		alphabet['E']--;
		res.push_back(1);
		one();
	}
}
void two() {
	if (alphabet['T'] && alphabet['W'] && alphabet['O']) {
		alphabet['T']--;
		alphabet['W']--;
		alphabet['O']--;
		res.push_back(2);
		two();
	}
}void three() {
	if (alphabet['T'] && alphabet['H'] && alphabet['R'] && (alphabet['E'] >= 2)) {
		alphabet['T']--;
		alphabet['H']--;
		alphabet['R']--;
		alphabet['E']--;
		alphabet['E']--;
		res.push_back(3);
		three();
	}
}
void four() {
	if (alphabet['F'] && alphabet['O'] && alphabet['U'] && alphabet['R']) {
		alphabet['F']--;
		alphabet['O']--;
		alphabet['U']--;
		alphabet['R']--;
		res.push_back(4);
		four();
	}
}
void five() {
	if (alphabet['F'] && alphabet['I'] && alphabet['V'] && alphabet['E']) {
		alphabet['F']--;
		alphabet['I']--;
		alphabet['V']--;
		alphabet['E']--;
		res.push_back(5);
		five();
	}
}
void six() {
	if (alphabet['S'] && alphabet['I'] && alphabet['X']) {
		alphabet['S']--;
		alphabet['I']--;
		alphabet['X']--;
		res.push_back(6);
		six();
	}
}
void seven() {
	if (alphabet['S'] && alphabet['E'] >= 2&& alphabet['V'] && alphabet['N']) {
		alphabet['S']--;
		alphabet['E']--;
		alphabet['V']--;
		alphabet['E']--;
		alphabet['N']--;
		res.push_back(7);
		seven();
	}
}
void eight() {
	if (alphabet['E'] && alphabet['I'] && alphabet['G'] && alphabet['H'] && alphabet['T']) {
		alphabet['E']--;
		alphabet['I']--;
		alphabet['G']--;
		alphabet['H']--;
		alphabet['T']--;
		res.push_back(8);
		eight();
	}
}
void nine() {
	if (alphabet['N'] >= 2 && alphabet['I'] && alphabet['E']) {
		alphabet['N']--;
		alphabet['I']--;
		alphabet['N']--;
		alphabet['E']--;
		res.push_back(9);
		nine();
	}
}
int main() {
	int T, n, i, testcase = 1;

	FILE *finput = freopen("input.txt", "r", stdin);
	FILE *foutput = freopen("output.txt", "w+", stdout);

	scanf("%d", &T);

	while (T--) {
		scanf("%s", input);
		memset(alphabet, 0, sizeof(alphabet));
		res.clear();
		ptr = 0;
		n = strlen(input);

		for (i = 0; i < n; i++) {
			alphabet[input[i]]++;
		}

		zero();
		six();
		two();
		four();
		five();
		eight();
		nine();
		seven();
		three();
		one();

		sort(res.begin(),res.end());
		n = res.size();
		printf("Case #%d: ", testcase++);
		for(i=0;i<n;i++) printf("%d",res[i]);
		printf("\n");
	}

	return 0;
}