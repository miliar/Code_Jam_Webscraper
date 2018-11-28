#include <iostream>
#include <fstream>
using namespace std;

void test(int i) {
	int br = 0;
	int odg;
	int ans;
	int zanemari;
	int moguce[4];
	
	cin >> ans;
	for(int k=0; k<4; k++)
		if(k == ans-1)
			for(int i=0; i<4; i++) cin >> moguce[i];
		else
			for(int i=0; i<4; i++) cin >> zanemari;
	
	cin >> ans;
	for(int k=0; k<4; k++)
		if(k == ans-1)
			for(int j=0; j<4; j++) {
				cin >> zanemari;
				for(int i=0; i<4; i++)
					if(zanemari == moguce[i]) {
						br++;
						odg = zanemari;
					}
			}
		else
			for(int i=0; i<4; i++) cin >> zanemari;
	
	if(br==1)
		cout << "Case #" << i << ": " << odg << endl;
	else if(br==0)
		cout << "Case #" << i << ": Volunteer cheated!" << endl;
	else
		cout << "Case #" << i << ": Bad magician!" << endl;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int n; cin >> n;
	for(int i=1; i<=n; i++) test(i);
	fclose(stdin);
	fclose(stdout);
	return 0;
}
