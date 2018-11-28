#ifndef CONFIG_H
#define CONFIG_H

#ifndef RELEASE_VERSION //1st time
#define RELEASE_VERSION
#endif //RELEASE_VERSION 1st time

#include <string>
#include <vector>

namespace GLOBALS { //values used throughout or for easy finding
std::string ifname = "input.txt"; //may need to be changed at a moments notice
std::vector<unsigned int> theFile; //contains everything from the input file

}



#ifndef RELEASE_VERSION //2nd time
  #ifndef DEBUG
  #define DEBUG
  #endif // DEBUG
  #ifndef CLEANINPUT_VERBOSE
//  #define CLEANINPUT_VERBOSE
  #endif  //CLEANINPUT_VERBOSE
#endif //RELEASE_VERSION 2nd time

#endif //include guard
