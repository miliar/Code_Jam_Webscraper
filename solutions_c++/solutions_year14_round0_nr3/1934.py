#include <iostream>
using namespace std;

int r, c, m, k, a[60][60], b[50][50];

int solve(int i, int j)
{
	int mm, ii, jj, z;
//	cout << i<<j<<endl;
	if (j>c) solve(i+1,1);
	else if (i>r) {
		mm=0;
		for (ii=1; ii<=r; ii++)
			for (jj=1; jj<=c; jj++) {
				z=1;
				if (a[ii+1][jj]==1) z=0;
				if (a[ii-1][jj]==1) z=0;
				if (a[ii][jj+1]==1) z=0;
				if (a[ii][jj-1]==1) z=0;
				if (a[ii+1][jj+1]==1) z=0;
				if (a[ii+1][jj-1]==1) z=0;
				if (a[ii-1][jj+1]==1) z=0;
				if (a[ii-1][jj-1]==1) z=0;
				
				if (z) mm++;

//				if (z) cout <<ii<<jj<<endl;
			}
//		cout << mm << endl;
		if (mm==m) {	
//			cout << "solved !!!" << endl;
			k=1;
			for (ii=1; ii<=r; ii++)
				for (jj=1; jj<=c; jj++) {
					b[ii][jj]=a[ii][jj];

					z=1;
					if (a[ii+1][jj]==1) z=0;
					if (a[ii-1][jj]==1) z=0;
					if (a[ii][jj+1]==1) z=0;
					if (a[ii][jj-1]==1) z=0;
					if (a[ii+1][jj+1]==1) z=0;
					if (a[ii+1][jj-1]==1) z=0;
					if (a[ii-1][jj+1]==1) z=0;
					if (a[ii-1][jj-1]==1) z=0;
				
					if (z) b[ii][jj]=9;
					
				}
		}
				
	}
	else {
		solve(i,j+1);
		if (a[i-1][j]+a[i][j-1]) {
			a[i][j]=1;
			solve(i,j+1);
			a[i][j]=0;
		}
	}
	
	return 0;
}


int main()
{
	int t, n, i, j; 
	
	cin >> n;
	for (t=0; t<n; t++) {
		cin >> r >> c >> m;
		for (i=0; i<=r; i++) 
			for (j=0; j<=c; j++) 
				a[i][j]=0;		
		
		k=0;
		if (m==r*c-1) {
			k=1;
			for (i=1; i<=r; i++) 
				for (j=1; j<=c; j++) 
					b[i][j]=9;
		}

		else {
			a[0][0]=1;
			a[1][1]=1;
			solve(1, 2);
		}
		
		b[1][1]=5;
		cout << "Case #" << t+1 << ":" << endl;
		if (k==0) cout << "Impossible" <<  endl;
		else {
			for (i=1; i<=r; i++) {
				for (j=1; j<=c; j++) {
					if (b[i][j]==1) cout << ".";
					if (b[i][j]==0) cout << ".";
					if (b[i][j]==5) cout << "c";
					if (b[i][j]==9) cout << "*";
				}
				cout << endl;	
			}	
		}
	}	
	return 0;
}
