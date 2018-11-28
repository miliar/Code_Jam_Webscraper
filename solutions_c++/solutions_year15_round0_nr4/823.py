#include <string>
#include <iostream>

// Returns 1 if impossible piece can be picked, 0 if no impossible piece can be picked or -1 o/w
int testcase()
{
	int X, R, C;
	std::cin >> X >> R >> C;
	
	// REMOVE ME
	//std::cout << X << " " << R << " " << C << "   ";
	
	// Exclude identical cases; after this we have R <= C.
	if ( R > C )
	{
		int h = R; R = C; C = h;
	}
	
	// A priori just always impossible, regardless of piece picked.
	if ( 0 != ( (R*C) % X ) ) return 1;
	
	// Can pick a block that's longer than size of thing so will always stick out
	if ( X > R && X > C ) return 1;
	
	// Can only pick a 1x1 block, which is never a problem
	if ( X == 1 ) return 0;
	
	// Can only pick a 1x2 block, which is never a problem (except as covered above)
	if ( X == 2 ) return 0;
	
	// Sigh.
	if ( X == 3 )
	{
		if ( R == 1 ) return 1;
		if ( R == 2 && C == 3 ) return 0;
		if ( R == 3 && C == 3 ) return 0;
		if ( R == 3 && C == 4 ) return 0;
	}
	
	// Next.
	if ( X == 4 )
	{
		if ( R == 1 ) return 1; // Can pick the square
		if ( R <= 3 && C <= 3 ) return 1; // Can pick the long thing
		if ( R == 2 && C == 4 ) return 1; // The zig-zag is a problem
		if ( R == 3 && C == 4 ) return 0; // Can accomodate all.
		if ( R == 4 && C == 4 ) return 0; // By the above.
	}
	
	return -1;
}
	
int main()
{
	int n;
	std::cin >> n;
	for( int i = 0 ; i < n ; i++ )
	{
		int b = testcase();
		std::cout << "Case #" << i + 1 << ": " << 
			( b == 1 ? "RICHARD" : ( b == 0 ? "GABRIEL" : "???????" ) )
			<< std::endl;
	}
		
}