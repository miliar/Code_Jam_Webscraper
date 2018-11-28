#include <iostream>
using namespace std;


int main()
{
	int t, r, n, i, j, k, b[4][4], c[20];
	
	cin >> n;
	for (t=0; t<n; t++) {
		for (i=0; i<20; i++) c[i]=0;
		cin >> r;
		for (i=0; i<4; i++) 
			for (j=0; j<4; j++) 
				cin >> b[i][j];		
		for (j=0; j<4; j++) 
			c[b[r-1][j]]++;		
		cin >> r;
		for (i=0; i<4; i++) 
			for (j=0; j<4; j++) 
				cin >> b[i][j];		
		for (j=0; j<4; j++) 
			c[b[r-1][j]]++;		
		k=0;	
		for (i=0; i<20; i++) if (c[i]==2) k++;
		for (i=0; i<20; i++) if (c[i]==2) j=i;
		
		if (k==0) cout << "Case #" << t+1 << ": Volunteer cheated!" <<  endl;
		if (k==1) cout << "Case #" << t+1 << ": " << j <<  endl;
		if (k>=2) cout << "Case #" << t+1 << ": Bad magician!" <<  endl;
	}	
	return 0;
}
