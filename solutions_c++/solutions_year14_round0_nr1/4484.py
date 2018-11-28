#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include <algorithm>
#include <vector>

#include <boost/algorithm/string.hpp>


int main(int argc, char** argv) { 
	std::shared_ptr<std::istream> in;
	std::ifstream infile; 
	if( argc > 1 ) { 
		in.reset(new std::ifstream(argv[1])); 
	} else { 
		in.reset(&(std::cin),[](...){});
	}
	int testcases,firstanswer,secondanswer;
	std::vector<int> firstrow,secondrow,results;
	std::vector<std::string> placeholder; 
	std::string line; 

	std::getline(*in,line);
	testcases = std::stoi(line);
	//std::cout << "There are " << testcases << " testcases " << std::endl; 
	for( int i = 0 ; i < testcases ; i++ ) { 
		std::getline(*in,line);
		firstanswer = std::stoi(line); 
		//std::cout << "Firstanswer: " << firstanswer << std::endl; 

		for(int j = 0 ; j < 4; j++ ) { 
			if( j+1 == firstanswer ) { 
				std::getline(*in,line);
				std::remove(line.begin(),line.end(),'\n');
				//std::cout << "First answer line is: " << line << std::endl; 
				boost::split(placeholder,line, boost::is_any_of(" "));
				std::transform(placeholder.begin(),placeholder.end(),std::back_inserter(firstrow), [](const std::string& s) { return std::stoi(s); } );
			} else { 
				std::getline(*in,line);
			}
		}

		std::getline(*in,line);
		secondanswer = std::stoi(line);
		//std::cout << "Secondanswer: " << secondanswer << std::endl; 
		for(int j = 0 ; j < 4; j++ ) { 
			if( j+1 == secondanswer ) { 
				std::getline(*in,line);
				std::remove(line.begin(),line.end(),'\n');
				//std::cout << "Second answer line is: " << line << std::endl; 
				boost::split(placeholder,line, boost::is_any_of(" "));
				std::transform(placeholder.begin(),placeholder.end(),std::back_inserter(secondrow), [](const std::string& s) { return std::stoi(s); } );
			} else { 
				std::getline(*in,line);
			}
		}


		std::sort(firstrow.begin(),firstrow.end());
		std::sort(secondrow.begin(),secondrow.end());
		std::set_intersection(firstrow.begin(),firstrow.end(),secondrow.begin(),secondrow.end(),std::back_inserter(results));

		std::cout << "Case #" << i+1 << ": ";
		if(results.size() == 1) { 
			std::cout << results[0]; // Answer
		} else if (results.size() > 1) { 
			std::cout << "Bad magician!";
		} else { 
			std::cout << "Volunteer cheated!";
		}
		std::cout << std::endl;
 
		results.clear();
		firstrow.clear();
		secondrow.clear();
	}

	return 0; 
}
