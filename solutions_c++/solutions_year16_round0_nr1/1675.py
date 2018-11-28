//-----------------------------------------------------------------------------
// Template for G00gle C0de Jam :-)
//-----------------------------------------------------------------------------

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <iterator>
#include <deque>
#include <set>
#include <sstream>


void solution(int test, std::deque<std::string>& data, std::ofstream& ofs) {
	std::cout << "Case #" << test+1 << std::endl;
    ofs << "Case #" << test+1 << ": ";
    /* Start coding here */

	std::string NInStr = data.front();
	data.pop_front();
    char* pEnd;
	long NIn = strtol(NInStr.c_str(), &pEnd, 10);
	long N = 0;

	if (NInStr == "0")
        ofs << "INSOMNIA";
	else
	{
		std::set<char> digits;
		int i = 0;
		std::string NStr = NInStr;
		while (digits.size() != 10)
		{
			++i;
			char* pEnd;
			N = NIn*i;
			std::cout << "i=" << i << " N=" << N << std::endl;
			std::ostringstream ss;
			ss << N;
			NStr = ss.str();
			std::cout << "i="<< i << " NStr=" << NStr << std::endl;

			for (std::string::iterator it = NStr.begin(); it != NStr.end(); ++it)
			{
				digits.insert(*it);
			}
		};
		ofs << NStr;
	}

    /* End */
	std::cout << std::endl;
    ofs << std::endl;
}


int
main(int argc, char *argv[])
{
    std::string bin_name(argv[0]);

    if(argc < 2) {
        std::cerr << "Usage : " << bin_name << " [dataFile]" << std::endl;
        return EXIT_FAILURE;
    }

    std::ifstream data_file(argv[1]);
    std::deque<std::string> data((std::istream_iterator<std::string>(data_file)), std::istream_iterator<std::string>());

    //for(std::deque<std::string>::iterator it = data.begin(); it != data.end(); ++it)
    //    std::cout << *it << ' ' << std::endl;

	std::string outputFileName = std::string("output/") + bin_name + std::string(".out");
    std::ofstream ofs(outputFileName.c_str(), std::ofstream::out);

	const std::string nb_tests_case_str = data.front();
	data.pop_front();
    const int nb_tests_case = atoi(nb_tests_case_str.c_str());

    for(int i = 0; i < nb_tests_case; ++i) {
        solution(i, data, ofs);
    }

    ofs.close();

    return EXIT_SUCCESS;
}
