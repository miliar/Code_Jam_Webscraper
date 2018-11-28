#include <iostream>
#include <fstream>
using namespace std;

void main()
{
	ifstream in("c:\\doom\\B-large.in");
	ofstream out("c:\\doom\\out.txt");

	int numCases;
	in >> numCases;

	out.precision(15);
	for (int i = 1; i <= numCases; ++i)
	{
		double C, F, X;
		in >> C >> F >> X;

		// Initial best guess is if we buy no farms
		double currentTime = 0;
		double currentRate = 2.0;
		double bestTime = X / currentRate;
		while (currentTime < bestTime)
		{
			// Assume we buy a farm as soon as we can, then recalculate ETA
			double timeToNextFarm = C / currentRate;
			currentTime += timeToNextFarm;
			currentRate += F;
			double newEstimate = currentTime + X / currentRate;
			if (newEstimate < bestTime) bestTime = newEstimate;
		}

		out << "Case #" << i << ": " << bestTime << endl;
	}
}