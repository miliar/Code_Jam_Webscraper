#include <iostream>

using namespace std;
int main(int argc, char *argv[]) {
    int n;
    cin >> n;
    for (int x=0; x<n; x++) {
        int a1[4][4];
        int row;
		cin >> row;
		row--;
		for (int y=0; y<4; y++) {
			for (int z=0; z<4; z++) {
				cin >> a1[y][z];
			}
		}
		int z1,z2,z3,z4;
        z1=a1[row][0];
        z2=a1[row][1];
        z3=a1[row][2];
        z4=a1[row][3];
		int a2[4][4];
		        int row2;
				cin >> row2;
				row2--;
				for (int y=0; y<4; y++) {
					for (int z=0; z<4; z++) {
						cin >> a2[y][z];
					}
				}
				int u1,u2,u3,u4;
		        u1=a2[row2][0];
		        u2=a2[row2][1];
		        u3=a2[row2][2];
		        u4=a2[row2][3];
		int m=0;
		int q=0;
		if (z1==u1 or z1==u2 or z1==u3 or z1==u4) {
			m++;
			q=z1;
		}
		if (z2==u1 or z2==u2 or z2==u3 or z2==u4) {
					m++;
					q=z2;
				}
				if (z3==u1 or z3==u2 or z3==u3 or z3==u4) {
							m++;
							q=z3;
						}
						if (z4==u1 or z4==u2 or z4==u3 or z4==u4) {
									m++;
									q=z4;
								}
		if(m==0) {
			cout << "Case #" << x+1 << ": Volunteer cheated!" << endl;
		}
		if(m==1) {
					cout << "Case #" << x+1 << ": " << q << endl;
				}
				if(m>1) {
							cout << "Case #" << x+1 << ": Bad magician!" << endl;
						}
    }
}
