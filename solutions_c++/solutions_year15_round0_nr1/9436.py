#include <iostream>
#include <sstream>

#ifdef _DEBUG
#define DPF(...) printf(__VA_ARGS__)
#else
#define DPF(...)
#endif

template <class T1, class T2>
T1 convert(const T2 &in){
	std::stringstream s;
	T1 out;

	s << in;
	s >> out;

	return out;
}

void StandingOvation()
{
	unsigned int numTestCases = 0;
	std::cin >> numTestCases;
	DPF("numTestCases: %u\n", numTestCases);

	for (unsigned int i = 0; i < numTestCases; ++i)
	{
		unsigned int maxShyness = 0;
		char szAttendees[1024];
		std::cin >> maxShyness >> szAttendees;
		DPF("Received %u people represented by \"%s\"\n", maxShyness + 1, szAttendees);
		if (maxShyness + 1 > strlen(szAttendees)) {
			DPF("MISMATCH: %u > %u", maxShyness + 1, szAttendees);
			continue;
		}

		int prevLevels = 0;
		int maxRequired = 0;
		for (unsigned int j = 0; j <= maxShyness; ++j)
		{
			int numRequired = j - prevLevels;
			if (numRequired > maxRequired)
				maxRequired = numRequired;
			prevLevels += convert<unsigned int>(szAttendees[j]);
		}
		std::cout << "Case #" << i+1 << ": " << maxRequired << std::endl;
	}
}

int main(int argc, char ** argv)
{
	StandingOvation();
	return 0;
}