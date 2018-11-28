#include <iostream>
#include <vector>
#include <fstream>
#include <stdexcept>
#include <string>
#include <cassert>
#include <set>
#include <cstdlib>


using namespace std;

char exceptionBuffer[10000];
#define throwException(s, ...)                  \
  sprintf(exceptionBuffer, s, ##__VA_ARGS__);   \
  throw std::runtime_error(exceptionBuffer);

enum class TrimStyle {DontTrim, Trim};

// retrieved from http://oxaric.wordpress.com/2008/11/23/3-simple-c-functions/
std::string trim( std::string line ) {
  if ( line.empty() ) {
    return "";
  }
  int string_size = (int)(line.length());
  int beginning_of_string = 0;
  // the minus 1 is needed to start at the first character
  // and skip the string delimiter
  int end_of_string = string_size - 1;
  bool encountered_characters = false;
  // find the start of chracters in the string
  while ( (beginning_of_string < string_size) && (!encountered_characters) ) {
    // if a space or tab was found then ignore it
    if ( (line[ beginning_of_string ] != ' ') &&
         (line[ beginning_of_string ] != '\t') ) {
      encountered_characters = true;
    } else {
      beginning_of_string++;
    }
  }
  // test if no characters were found in the string
  if ( beginning_of_string == string_size ) {
    return "";
  }
  encountered_characters = false;
  // find the character in the string
  while ( (end_of_string > beginning_of_string) &&
          (!encountered_characters) ) {
    // if a space or tab was found then ignore it
    if ( (line[ end_of_string ] != ' ') && (line[ end_of_string ] != '\t') ) {
      encountered_characters = true;
    } else {
      end_of_string--;
    }
  }
  // return the original string with all whitespace removed from
  // its beginning and end
  // + 1 at the end to add the space for the string delimiter
  return line.substr( beginning_of_string,
                      end_of_string - beginning_of_string + 1 );
}

std::vector<std::string> tokenize(const std::string& str, const std::string& delimiters,
                                  const TrimStyle doTrim) {
  // Skip delimiters at beginning.
  std::vector<std::string> tokens;
  std::string::size_type lastPos = str.find_first_not_of(delimiters, 0);
  // Find first "non-delimiter".
  std::string::size_type pos     = str.find_first_of(delimiters, lastPos);
  while (std::string::npos != pos || std::string::npos != lastPos) {
    // Found a token, add it to the vector.
    std::string candidate = str.substr(lastPos, pos - lastPos);
    if (doTrim == TrimStyle::Trim) {
      candidate = trim(candidate);
    }
    tokens.push_back(candidate);
    // Skip delimiters.  Note the "not_of"
    lastPos = str.find_first_not_of(delimiters, pos);
    // Find next "non-delimiter"
    pos = str.find_first_of(delimiters, lastPos);
  }
  return tokens;
}
