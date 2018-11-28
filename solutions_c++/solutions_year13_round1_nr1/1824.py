#include <stdio.h>
#include <vector>


using namespace std;


///////////////
// constants //
///////////////
bool DEBUG = false;


///////////////
// variables //
///////////////
int T = 0;
long long r = 0;
long long t = 0;


///////////////
// functions //
///////////////
inline long long black_area (long long white_r)
{
//	int black_r = white_r + 1;
//	return (black_r * black_r) - (white_r * white_r);
	return 2 * white_r + 1;
}


inline int num_disk()
{
	if (DEBUG) {
		fprintf (stderr, "r: %lld, t: %lld\n", r, t);
	}
	int num = 0;
	for (long long white_r = r; t > 0; white_r += 2) {
		t -= black_area (white_r);
		if (t >= 0) {
			++num;
		}
		if (DEBUG) {
			fprintf (stderr, "\tnum: %d, white_r: %lld, t: %lld\n", num, white_r, t);
		}
	}
	return num;
}


//////////
// main //
//////////
int main (int argc, char** argv)
{
	FILE* input = (argc > 1) ? fopen ("input.txt", "rt") : stdin;

	fscanf (input, "%d\n", &T);
	for (int tc = 1; tc <= T; ++tc) {
		fscanf (input, "%lld %lld\n", &r, &t);
		printf ("Case #%d: %d\n", tc, num_disk());
	}

	fclose (input);
	return 0;
}
