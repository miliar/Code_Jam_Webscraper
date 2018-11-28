#include <fstream>
#include <string>

int numInvites (std::ifstream& in) {
	int maxShyness;
	in >> maxShyness;
	std::string shynesss;
	std::getline(in, shynesss);

	int ret = 0;
	int standing = 0;

	for (int i = 0; i <= maxShyness; ++i) {
		int invites = ((i - standing > 0) ? i - standing : 0);
		ret += invites;
		standing += invites;
		// +1 because space left in shyness
		standing += shynesss[i + 1] - '0';
	}
	return ret;
}


int main (int argc, char** argv) {
	std::ifstream in {argv[1]};
	int cases;
	in >> cases;

	std::ofstream res ("ovation.out");

	for (int i = 1; i <= cases; ++i) {
		int people = numInvites(in);
		res << "Case #" << i << ": " << people << "\n";
	}
}