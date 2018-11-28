#include <fstream>
#include <iostream>
#include <sstream>
#include <math.h>

bool isFair(int number){
    //check if number is a palindrome

    std::stringstream ss;
    ss << number;
    std::string strNum = ss.str();
    //std::cout << strNum << std::endl;

    std::string strNumRev = "";
    for (int i = strNum.length()-1; i >= 0; i--){
        strNumRev += strNum.at(i);
    }
    //std::cout << strNumRev << std::endl;

    return (strNum == strNumRev);
}

int main(int argc, char *argv[])
{
    //Fair and Square
    std::cout << "Starting solution of problem C..." << std::endl;

    //file names for input and output
    //std::string filenameIn = "C-large.in";
    //std::string filenameOut = "C-large.out";
    //std::string filenameIn = "C-small-practice.in";
    //std::string filenameOut = "C-small-practice.out";
    std::string filenameIn = "C-small-attempt0.in";
    std::string filenameOut = "C-small-attempt0.out";

    std::ofstream os(filenameOut.c_str());

    std::ifstream is(filenameIn.c_str());
    if (is.is_open()){
        int numTestCases = 0;
        is >> numTestCases;

        for (int nCase = 1; nCase <= numTestCases; nCase++){
            std::cout << "Process case #" << nCase << std::endl;
            int intervalStart = 0;
            int intervalEnd = 0;
            is >> intervalStart >> intervalEnd;

            int numFaS = 0;
            for (int num = intervalStart; num <= intervalEnd; num++){
                //std::cout << "Number " << num << std::endl;

                if (!isFair(num)){
                    continue;
                }
                //std::cout << "    fair" << std::endl;

                int sqrtNum = sqrt(num);
                //std::cout << "    root " << sqrtNum << std::endl;
                if (int(pow(double(sqrtNum), 2.0)) != num){
                    continue;
                }
                if (!isFair(sqrtNum)){
                    continue;
                }
                //std::cout << "    root is fair" << std::endl;

                //number is fair and its square root is fair, too
                numFaS++;
            }

            //write result for test case into file
            os << "Case #" << nCase << ": " << numFaS << std::endl;
            std::cout << "Case #" << nCase << ": " << numFaS << std::endl;
        }

    }
    is.close();

    os.close();

    return 0;
}
