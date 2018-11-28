#include <fstream>
#include <iostream>

bool solveOne(int X, int R, int C) {
	//std::cout << X << " " << R << "x" << C << "\n";
	//losing case
	if (X == 1)
		return false;

	//make is a tall rectangle
	if (C > R)
		std::swap(R, C);

	//area can't be split into chunks of X
	if ((R*C) % X != 0)
		return true;
	//can be made not to fit
	if (X > R)
		return true;
	//smallest side less than L-shape min side
	if (C < X / 2+X%2)
		return true;
	//separates a cell inside itself
	if (X >= 7)
		return true;
	//can draw a cross such that it would leave chunks of less size
	if ((X>R + C - 2) &&
		(X>=R+2) &&
		(X>3))
		return true;
	//forces an orientation with one side, while filling the other
	if (X >= 4 &&
		X > C * 2 - 1)
		return true;
	return false;
}

void solve() {
	std::ifstream input("test.in");
	std::ofstream output("test.out");
	int T;
	input >> T;
	for (int step = 0; step < T; step++) {
		int X, R, C;
		input >> X >>R >>C;
		output << "case #" << step+1 << ": ";
		if (solveOne(X,R,C))
			output << "RICHARD\n";
		else
			output << "GABRIEL\n";
	}
	output.close();
}

int main()
{
	solve();
	return 0;
}

