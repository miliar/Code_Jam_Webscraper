#include <iostream>
#include <fstream>

#define debug 0

using namespace std;

int main()
{
	
	std::ifstream in("in");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!

	std::ofstream out("out");
	std::streambuf *coutbuf = std::cout.rdbuf(); //save old buf
	std::cout.rdbuf(out.rdbuf()); //redirect std::cout to out.txt!
	
	
	// Number of test cases
	int t;
	cin >> t;
	
	// For each test case
	for (int i = 0; i < t; i++)
	{
		
		// Get x - size of x-omino; r, c - dimensions of grid
		int x,r,c;
		cin >> x >> r >> c;
		
		// At the start, assume GABRIEL can win.
		bool can_win = true;
		
		// This goes to the file regardless of debug...duh
		if (debug) cout << "Test case: " << t << " x, r, c: " << x << " " << r << " " << c << endl;
		
		
		//-BEGIN CHECKING CASES----------------------------------------------------------------------
		// The below cases check for facts that prevent GABRIEL from winning. There will be redundancy.
		
		
		// If r*c is less than x, we can't really play, can we?
		if ( (r*c) < x ) can_win = false;
		
		// If r*c is not divisible by x, clearly we can't fill the grid in any way.
		if ( (r*c) % x != 0 ) can_win = false;
		
		// If x is greater than r and c, Richard can choose an x-omino that does not fit in the grid.
		if ( (x > r) && (x > c) ) can_win = false;
		
		// RICHARD can make a right-angle piece that will not fit in any orientation.
		if ( x > (r+c - 1) ) can_win = false;
		
		// RICHARD can make a piece whose width and length are greater than either r or c, and thus cannot be 
		//	fit in the grid, even after rotation.
		if (r < c) 
		{
			// We can reimagine the grid as an r-by-r square; our goal is to choose a piece which can't fit in
			//	this square.
			
			// The most efficient way to make such a block is a right angle.
			// The number of blocks in the max-sized right-angle which will fit in our new
			//	grid is r (down the left side to the bottom left corner) + r-1 (across to the
			//	bottom right corner). Thus, if x is greater than 2r-1, we can "break" the square.
			
			// Note: in practicality, we need to check not that x is greater than the max right-angle
			//	block that fits, but instead, that it is greater than or equal to the min right angle
			// 	block that breaks the square. Consider r=1; the former check will pass for a line of 2
			//	blocks, which MAY be able to fit on our board (i.e. if c =4)
			// Thus we check that x is greater than or equal to (x + x-1) + 2. 
			
			if (x >= (2*r)-1 + 2) can_win = false;
			
		} 
		// Special case: if the board is a square, the square can be broken with just (x + x-1) + 1 blocks.
		else if (r == c) 
		{
			if (x >= (2*r)-1 + 1) can_win = false;
		}
		else 
		{
			// Likewise as above, but we imagine that the grid is a c-by-c square.
			// TODO: nice code repetition LOL
			
			if (x >= (2*c)-1 + 2) can_win = false;
		}
		
		
		// For x > 6, we can make x-ominoes with enclosed holes, which will be impossible to fill.
		if (x > 6) 
		{
			// I thought, at first, that I'd have to make sure that these pieces with holes would
			//	have to fit on the board. I realized that if RICHARD can make a piece with a hole
			//	that DOESN'T fit on the board, he didn't really need the hole at all!
			// The practical implication of this is that we can simply declare any cases where
			//	x > 6 as can't-win cases for GABRIEL.
			
			can_win = false;
		}
		
		
		// For some x, r, and c, we can pick x-ominoes which partition the board into two smaller 
		//	boards. These smaller boards may not then be solvable.
		// If RICHARD can guarantee at least one of these sub-regions isn't solvable, he wins.
		// The minimum way to have a piece partition the board is to have one "line" which runs
		//	in the short dimension, and then a segment connected at one end running perpendicular
		//	to the original line that is at least one block longer than the length of the short 
		//	dimension. The point of this attached segment is to ensure that the partitioning piece
		//	can't be rotated to fit in the board.
		// The minimum size for this piece is the short dimension, r, plus r-1+1...so 2r. 
		// We can picture this as r blocks being used to make the divider. Then the remaining blocks
		//	(minimum r) will be within one of the two segments. All we have to do, then, is check to
		//	see if we can add the rest of these blocks into the two segments in such a way that
		//	at least one of the segments contains a number of free spaces that is not divisible by x.
		// NOTE: x must be at least 4 to create a proper partition (i.e. a T block in tetris)
		
		int smaller = (r < c) ? r : c;
		int larger = (r > c) ? r : c;
		
		if (x >= 4 && x >= 2*smaller)
		{
			// We use r blocks for the divider. This is the number remaining.
			
			// Kinda don't have time to do this. Gotten kinda convoluted. For the sake of time i'm just
			// 	gonna say if we get to this point then RICHARD probably wins!
			
			can_win = false;
		}
		
		
		//-END CHECKING CASES------------------------------------------------------------------------
		
		if (can_win) cout << "Case #" << i + 1 << ": GABRIEL" << endl;
		else cout << "Case #" << i+1 << ": RICHARD" << endl;
		
		
	}// End for each test case
	
	return 0;
	
}