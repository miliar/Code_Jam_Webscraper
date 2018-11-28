#include<iostream>

using namespace std;


int main(){
	int T, l1,l2;
	cin >> T;
	for(int it=1; it<=T; it++){
		int m1[4][4];
		int m2[4][4];

		cin >> l1;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++){
				int v; scanf("%d", &v);
				m1[i][j] = v;
			}

		cin >> l2;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++){
				int v; scanf("%d", &v);
				m2[i][j] = v;
			}
				
		l1--; l2--;
		int res = -1;
		bool badMag = false;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++){
				if(m1[l1][i] == m2[l2][j]){
					if(res != -1){	badMag = true;	goto vaza;	}
					else	res = m1[l1][i];
				}
			}

	vaza:
		if (badMag)
			cout << "Case #" << it << ": Bad magician!" << endl;
		else if(res == -1)
			cout << "Case #" << it << ": Volunteer cheated!" << endl;
		else
			cout << "Case #" << it << ": " << res << endl;		

	}

}
