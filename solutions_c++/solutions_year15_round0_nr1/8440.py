// StandingOvation.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <vector>

#include <boost/filesystem.hpp>
using namespace boost::filesystem;

#include <iostream>
//#include <boost/iostreams/stream.hpp>
//#include <boost/iostreams/device/mapped_file.hpp>
//namespace io = boost::iostreams;

//#define _DEBUG_ 1

int _tmain(int argc, _TCHAR* argv[])
{
	if (argc > 1) {
		path p(argv[1]);   // p reads clearer than argv[1] in the following code

		if (exists(p) && is_regular_file(p)) {   // does p actually exist?

#ifdef _DEBUG_
			std::cerr << "Reading data [" << argv[1] << "]"<< std::endl;
#endif

			//io::stream<io::mapped_file_source> str(argv[1]);
			std::ifstream str(argv[1]);

			// you can read from str like from any stream, str >> x >> y >> z
			int nb_prob;
			str >> nb_prob;
#ifdef _DEBUG_
			std::cerr << "[" << nb_prob << "] Problem found\n";
#endif
			for (int i = 0; i < nb_prob;i++) {
				int smax;
				std::string shyness;
				std::vector<char> shyn;

				str >> smax >> shyness;
#ifdef _DEBUG_
				std::cerr << "Shyness max [" << smax << "] Shyness list ";
#endif
				for (int j = 0; j <= smax; j++) {
					shyn.push_back(shyness[j]-48);
				}

#ifdef _DEBUG_
				for (int j = 0; j <= smax; j++) {
					std::cerr << "[" << shyn[j] << "] ";
				}
				std::cerr << std::endl;
#endif

				int is_up = 0;
				int nb_inv = 0;
				for (int j = 0; j <= smax; j++) {
					if (shyn[j]>0 && is_up < j) {
						nb_inv = nb_inv + ( j - is_up );
						is_up = is_up + (j - is_up);
					} 
					is_up = is_up + shyn[j];
				}
				std::cout << "Case #" << (i+1) << ": " << nb_inv << std::endl;
			}

		}
		else {
			std::cerr << "File [" << argv[1] << "] Not found\n";
		}
	}
	else {
		std::cerr << "Missing argument : standingovation file_pb_description\n";
	}
	return 0;
}

