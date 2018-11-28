#!/usr/bin/bash

# This is a self compiling file
# Run with `cat file.in | ./$filename [debug|plot] > file.out`

# debug - Show a progress bar and stuff
# plot - Stream performance information to gnuplot

filename=$(echo $0 | sed 's:./::g')
flags="-xc++ -Ofast"
debug="cat"
if [ $filename -nt .$filename ] || [ "$1" != "" ]; then
	if [ "$1" == "debug" ]; then
		debug="sed '1i\#define DEBUG\n#include \"debug.cpp\"'"
		flags="$flags -g"
	elif [ "$1" == "plot" ]; then
		debug="sed '1i\#define DEBUG\n#define DEBUG_PLOT\n#include \"debug.cpp\"'"
		flags="$flags -g"
	fi
	sed -n '/^#include <cstdlib>/,$p' $filename | eval $debug | g++ -o .$filename $flags -
	if [ $? -ne 0 ]; then
		(echo "Error compiling") 1>&2
		exit 1
	fi
fi

if [ "$1" == "plot" ]; then
	eval ./.$filename 2> >(./stream_plot.py >> /dev/null 2>&1)
	exit $?
fi
exec ./.$filename


#include <cstdlib>
#include <cstdio>
#include <ctime>
#include <cassert>

#include <iostream>
#include <string>
#include <sstream>

#include <map>
#include <vector>
#include <algorithm>

typedef long long unsigned LLUint;

using namespace std;

int main(int argc, char ** argv)
{
	// number of cases
	#ifdef DEBUG
	debug_init(argc, argv);
	#endif //DEBUG
	
	int nCases;
	cin >> nCases;
	// do cases
	for (int c = 1; c <= nCases; ++c)
	{
		// get stuff
		LLUint r; LLUint t;
		cin >> r; cin >> t;
		
		//solve case
		
		
		LLUint n = 1;
		
		while (true)
		{
			LLUint t0 = 2*(n*r + n*n) - n;
			if (t0 == t)
			{
				cout << "Case #" << c << ": " << n << "\n";	
				break;
			}
			else if (t0 > t)
			{
				cout << "Case #" << c << ": " << n-1 << "\n";	
				break;
			}
			++n;	
		}
		
		#ifdef DEBUG_PLOT
		debug_time(c);
		#elif defined DEBUG
		debug_progress(c, nCases);
		#endif //DEBUG_PLOT
		
	}
	
	#ifdef DEBUG
	debug_finish();
	#endif //DEBUG
	return 0;	
}