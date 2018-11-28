//Counting Sheep
//Janice GU

#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <sstream>
#include <fstream>
/*
void print(std::vector<bool> vector) {
  std::cout << "Vector: ";
  for (std::vector<bool>::iterator i = vector.begin(); i != vector.end(); i++) {
    std::cout << *i << ' ';
  }
  std::cout << std::endl;
}
*/
void checkDigits(float n, std::vector<bool>& seen) {
  std::string numString;
  std::ostringstream convert;
  convert << n;
  numString = convert.str();

  float length = numString.length();
  //std::cout << "Length: " << length << '\n';

  for (float i = (length - 1); i >= 0; i--) {
    //std::cout << "N: " << n << '\n';
    float index = n/pow(10, i);
    index = floor(index);

    // Special case: Negative
    if (index < 0) {
      index = 0;
    }

    //std::cout << "Index: " << index << '\n';
    if (seen.at(index) == 0) {
      seen.at(index) = 1;
    }
    n = n - index*pow(10, i);
  }

  print(seen);
}

bool checkDone(std::vector<bool> seen) {
  bool done = true;
  for (std::vector<bool>::iterator i = seen.begin(); i != seen.end(); i++) {
    if (*i == 0) {
      done = false;
    }
  }

  return done;
}

//Main function: Gather input, run functions
int main(int argc, char** argv) {
  std::fstream file(argv[1]);

  std::ofstream out;
  out.open("1SheepOut.txt");

  float numTrials;
  file >> numTrials;

  for (float i = 1; i <= numTrials; i++) {
    float n;
    file >> n;

    if (n == 0) {
      out << "Case #" << i << ": " << "INSOMNIA\n";
      continue;
    }

    float current = n;
    std::vector<bool> seen(10, 0);
    bool done = false;
    while (!done) {
      //std::cout << current << '\n';
      checkDigits(current, seen);
      done = checkDone(seen);
      current = current + n;
    }

    current = current - n;
    out << "Case #" << i << ": " << current << '\n';
  }
}
