#include <iostream>
#include <vector>
#include <assert.h> 
#include <string.h> 
#include <stdlib.h> 

#define LSIZE_MAX (100)

using namespace std;

class lposition 
{
public:
	lposition(int r, int c)
	 : row(r), col(c)
	{
	}
	int row, col;
};

class lmover
{
public:
	lmover();
	int lawn_parse();
	bool lawn_pattern_check();
	int lawn_status(int i, bool isYes);

private:
	int row;
	int col;
	int pattern[LSIZE_MAX][LSIZE_MAX];
	vector<lposition> pos_bucket[LSIZE_MAX];
};

lmover::lmover()
{
	row=col = 0;
}

int lmover::lawn_parse()
{
	int m, n;

	cin>>n;
	cin>>m;
	
	row = n;
	col = m;
	for(int i=0; i<n; i++) {
		for(int j=0; j<m; j++) {
			cin>> pattern[i][j];
			lposition pos(i, j);
			pos_bucket[pattern[i][j]-1].push_back(pos);
		}
	}

	return 0;
}

bool lmover::lawn_pattern_check()
{
	// loop over the position vector
	for (int i=0; i < LSIZE_MAX; ++i) {
		for(vector<lposition>::iterator pos_iter=pos_bucket[i].begin();
			pos_iter!=pos_bucket[i].end();
			pos_iter++) {

			bool isYesR = true;
			// check whether the row or column in the this position has all elements less or equal to this value
			for(int r=0; r<row; r++) {
				if ( pattern[r][(*pos_iter).col] > pattern[(*pos_iter).row][(*pos_iter).col] ) {
					isYesR = false;
				}
			}

			// check for column
			bool isYesC = true;
			for(int c=0; c<col; c++) {
				if ( pattern[(*pos_iter).row][c] > pattern[(*pos_iter).row][(*pos_iter).col] ) {
					isYesC = false;
				}
			}
			
			if (!( isYesC || isYesR) ) {
				// If both row and colum has it wrong, this pattern is not possible
				return false;
			}
		}
	}
	return true;
}

int lmover::lawn_status(int i, bool isYes)
{
	cout<<"Case #"<<i;
	if ( isYes )
		cout << ": YES" <<endl;
	else
		cout << ": NO" <<endl;

	return 0;
}

int main()
{
	int n;
	bool isYes;
	cin>>n;

	for(int i = 0; i < n; ++i) {
		lmover lm;

		lm.lawn_parse();
		isYes = lm.lawn_pattern_check();
		lm.lawn_status(i+1, isYes);
	}

	return 0;
}
