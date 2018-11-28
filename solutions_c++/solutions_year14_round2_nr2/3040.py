#include <cstdlib> //atoi
#include <fstream> //reading files, writing to files
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
 
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::string;
using std::stringstream;
using std::vector;
 
int getNumTrials(ifstream &input);
void getParams(int &one, int &two, int &k, ifstream &input);
void resultOut(ofstream &output, int trialNum, int wins);
 
int main()
{
    ifstream input("input.txt");
    ofstream output("output.txt");
    int one, two, k;
    int numTrials = getNumTrials(input);

    int trial = 1, count = 0;
    vector<int> result;

    while (trial < numTrials + 1) {
        //empty the vector before the start of a new trial
        result.clear();
        //get the parameters for the new trial
        getParams(one, two, k, input);
        //bit-wise and each combination of numbers
        for (int x = 0; x < one; x++) {
            for (int y = 0; y < two; y++) {
                result.push_back(x&y);
            }
        }

        count = 0;
        //count total numbers less than k
        for (int x = 0; x < result.size(); x++)
            if (result[x] < k)
                ++count;
        //write result to file
        resultOut(output, trial++, count);
    }    
    input.close();
    output.close();
     
    return 0;
}
 
int getNumTrials(ifstream &input)
{
    string temp;
    int numTrials;
    getline(input, temp);
    //convert temp to a c string then to an integer
    numTrials = atoi(temp.c_str());
    return numTrials;
}
 
void getParams(int &one, int &two, int &k, ifstream &input)
{
    string temp;
    stringstream line;
    getline(input, temp);
    line << temp;
    line >> one >> two >> k;
}
 
void resultOut(ofstream &output, int trialNum, int wins)
{
    output << "Case #" << trialNum << ": " << wins << endl;
}