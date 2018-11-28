#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>

using namespace std;

int main() {
	int testcases;
	int slen;
	char str[2005];
	
	vector <int> lettcount;
	priority_queue <int, vector <int>, greater <int> > nums;
	
	scanf("%d", &testcases);
	
	for(int t = 1; t <= testcases; ++t) {
		scanf("%s", str);
		
		lettcount.assign(27, 0);
		
		slen = strlen(str);
		for(int i = 0; i < slen; ++i) {
			lettcount[str[i] - 'A']++;
		}
		
		// First pass, check z, g, u, x, w
		if(lettcount['Z' - 'A'] > 0) {
			// Zero
			for(int j = 0; j < lettcount['Z' - 'A']; ++j) {
				nums.push(0);
			}
			
			lettcount['E' - 'A'] -= lettcount['Z' - 'A'];
			lettcount['R' - 'A'] -= lettcount['Z' - 'A'];
			lettcount['O' - 'A'] -= lettcount['Z' - 'A'];
			lettcount['Z' - 'A'] = 0;
		}
		
		if(lettcount['G' - 'A'] > 0) {
			// Eight
			for(int j = 0; j < lettcount['G' - 'A']; ++j) {
				nums.push(8);
			}
			
			lettcount['E' - 'A'] -= lettcount['G' - 'A'];
			lettcount['I' - 'A'] -= lettcount['G' - 'A'];
			lettcount['H' - 'A'] -= lettcount['G' - 'A'];
			lettcount['T' - 'A'] -= lettcount['G' - 'A'];
			lettcount['G' - 'A'] = 0;
		}
		
		if(lettcount['U' - 'A'] > 0) {
			// Four
			for(int j = 0; j < lettcount['U' - 'A']; ++j) {
				nums.push(4);
			}
			
			lettcount['F' - 'A'] -= lettcount['U' - 'A'];
			lettcount['O' - 'A'] -= lettcount['U' - 'A'];
			lettcount['R' - 'A'] -= lettcount['U' - 'A'];
			lettcount['U' - 'A'] = 0;
		}
		
		if(lettcount['X' - 'A'] > 0) {
			// Six
			for(int j = 0; j < lettcount['X' - 'A']; ++j) {
				nums.push(6);
			}
			
			lettcount['S' - 'A'] -= lettcount['X' - 'A'];
			lettcount['I' - 'A'] -= lettcount['X' - 'A'];
			lettcount['X' - 'A'] = 0;
		}
		
		if(lettcount['W' - 'A'] > 0) {
			// Two
			for(int j = 0; j < lettcount['W' - 'A']; ++j) {
				nums.push(2);
			}
			
			lettcount['T' - 'A'] -= lettcount['W' - 'A'];
			lettcount['O' - 'A'] -= lettcount['W' - 'A'];
			lettcount['W' - 'A'] = 0;
		}
		
		// Second pass
		if(lettcount['O' - 'A'] > 0) {
			// One
			for(int j = 0; j < lettcount['O' - 'A']; ++j) {
				nums.push(1);
			}
			
			lettcount['N' - 'A'] -= lettcount['O' - 'A'];
			lettcount['E' - 'A'] -= lettcount['O' - 'A'];
			lettcount['O' - 'A'] = 0;
		}
		
		if(lettcount['H' - 'A'] > 0) {
			// Three
			for(int j = 0; j < lettcount['H' - 'A']; ++j) {
				nums.push(3);
			}
			
			lettcount['T' - 'A'] -= lettcount['H' - 'A'];
			lettcount['R' - 'A'] -= lettcount['H' - 'A'];
			lettcount['E' - 'A'] -= lettcount['H' - 'A'];
			lettcount['E' - 'A'] -= lettcount['H' - 'A'];
			lettcount['H' - 'A'] = 0;
		}
		
		if(lettcount['V' - 'A'] > 0) {
			if(lettcount['S' - 'A'] > 0) {
				// Seven
				for(int j = 0; j < lettcount['S' - 'A']; ++j) {
					nums.push(7);
				}
				
				lettcount['E' - 'A'] -= lettcount['S' - 'A'];
				lettcount['V' - 'A'] -= lettcount['S' - 'A'];
				lettcount['E' - 'A'] -= lettcount['S' - 'A'];
				lettcount['N' - 'A'] -= lettcount['S' - 'A'];
				lettcount['S' - 'A'] = 0;
			}
			
			if(lettcount['F' - 'A'] > 0) {
				// Five
				for(int j = 0; j < lettcount['F' - 'A']; ++j) {
					nums.push(5);
				}
				
				lettcount['I' - 'A'] -= lettcount['F' - 'A'];
				lettcount['V' - 'A'] -= lettcount['F' - 'A'];
				lettcount['E' - 'A'] -= lettcount['F' - 'A'];
				lettcount['F' - 'A'] = 0;
			}
		}
		
		// The rest, if it exists, is a nine
		if(lettcount['I' - 'A'] > 0) {
			// Nine
			for(int j = 0; j < lettcount['I' - 'A']; ++j) {
				nums.push(9);
			}
			
			lettcount['N' - 'A'] -= lettcount['I' - 'A'];
			lettcount['N' - 'A'] -= lettcount['I' - 'A'];
			lettcount['E' - 'A'] -= lettcount['I' - 'A'];
			lettcount['I' - 'A'] = 0;
		}
		
		printf("Case #%d: ", t);
		while(!nums.empty()) {
			printf("%d", nums.top());
			nums.pop();
		}
		printf("\n");
	}
	
	return 0;
}