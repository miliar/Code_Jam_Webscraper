#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

std::vector<std::string> g_output;
void WriteToOut(std::string &toWrite) {
    static int caseNum = 1;
    char bufferOut[20];
    sprintf_s(bufferOut, "Case #%d: ", caseNum++);
    g_output.push_back(bufferOut + toWrite);
}

void FriendsToInvite(char* crowdShyness){
    std::stringstream ss(crowdShyness);
    std::string word;
    std::vector<std::string> vec;
    while (ss.good()) {
        ss >> word;
        vec.push_back(word);
    }
    int numOfCrowd = atoi(vec[0].c_str());
    int numToInvite(0), remainingCrowd(0), totalCrowd(0);
    for(int i=0; i<numOfCrowd; ++i) {
        char currentCrowd = vec[1][i];
        int crowdOfShy = atoi(&currentCrowd);
        totalCrowd += crowdOfShy;
        if( (totalCrowd<=i)) {
            numToInvite++;
            totalCrowd++;
        }
        
    }
    WriteToOut(std::to_string(numToInvite));
}


int main(int argc, char **argv){
    std::string fileName;
    if (argc > 1) {
        fileName = argv[1];
    }
    else {
        fileName = "file.txt";
    }

    std::ifstream inFile(fileName.c_str());
    int numOfLines(0), numOfCrowd(0);
    char buffer[1005];
    if(inFile.is_open()){
        inFile.getline(buffer, 1005);
        numOfLines = atoi(buffer);
        for(int i=0; i < numOfLines; ++i) {
            inFile.getline(buffer, 1005);
            FriendsToInvite(buffer);
        }
    }

    std::ofstream outFile("output.txt");
    auto endIter  = g_output.end();
    for (auto iter = g_output.begin(); iter != endIter; ++iter)
    {
        outFile << *iter << std::endl;
    }

    outFile.close();
    inFile.close();

}