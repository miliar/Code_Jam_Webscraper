#include <iostream>
using namespace std;

int height[100][100];
bool cutted[100][100];

int main()
{
	int nTests;
	cin>>nTests;
	for(int tc=1; tc<=nTests; tc++) {

		int nRows, nColumns;
		cin>>nRows>>nColumns;

		for(int r=0; r<nRows; r++) {
			for(int c=0; c<nColumns; c++) {
				cin>>height[r][c];
				cutted[r][c] = false;
			}
		}

		for(int r=0; r<nRows; r++) {
			int maxHeight = -1;
			for(int c=0; c<nColumns; c++) {
				if( height[r][c] > maxHeight )
					maxHeight = height[r][c];
			}

			for(int c=0; c<nColumns; c++) {
				if( height[r][c] == maxHeight )
					cutted[r][c] = true;
			}
		}

		for(int c=0; c<nColumns; c++) {
			int maxHeight = -1;
			for(int r=0; r<nRows; r++) {
				if( height[r][c] > maxHeight )
					maxHeight = height[r][c];
			}

			for(int r=0; r<nRows; r++) {
				if( height[r][c] == maxHeight )
					cutted[r][c] = true;
			}
		}

		bool answer = true;
		for(int r=0; r<nRows; r++) {
			for(int c=0; c<nColumns; c++) {
				if( cutted[r][c] == false ) {
					answer = false;
					break;
				}
			}
			if( answer == false )
				break;
		}

		cout<<"Case #"<<tc<<": ";
		if( answer )
			cout<<"YES"<<endl;
		else
			cout<<"NO"<<endl;
	}

	return 0;
}