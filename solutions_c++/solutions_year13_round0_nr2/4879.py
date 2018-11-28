#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <list>

using namespace std;

bool checkVal(const vector<vector<int> > & matrix, int x, int y) {
     int val = matrix[x][y];
     int xSize = matrix.size();
     int ySize = matrix[0].size();
//     if(x == 0 || x == xSize - 1|| y == 0 || y == ySize - 1 ) {
//          return true;
//     }     
     bool isThereAWay = true;
     for(int itX = 0; itX < xSize; ++itX)
     {
         if(matrix[itX][y] > val) {
             isThereAWay = false;
             break;
         }
     }
     if(isThereAWay) {
         return true;
     }     
     isThereAWay = true;
     for(int itY = 0; itY < ySize; ++itY)
     {
         if(matrix[x][itY] > val) {
             isThereAWay = false;
             break;
         }
     }
     if(isThereAWay) {
         return true;
     }  
     return false;
}

bool checkResult(const vector<vector<int> > & matrix) {
     for(int itX = 0; itX < matrix.size(); ++itX)
     {
         const vector<int> & matrixLine = matrix[itX];
         for(int itY = 0; itY < matrixLine.size(); ++itY)
         {
                 if(!checkVal(matrix, itX, itY))
                 {
                     return false;
                 }
         }
     }
     return true;
}

bool readInput(list<string> & results) {
    string line;
    ifstream inFile;
    inFile.open ("B-large.in", ifstream::in);
    if(inFile.good())
    {
        getline(inFile, line);
        int numberOfTestCases;
        istringstream(line) >> numberOfTestCases;
        for(int i = 0; i < numberOfTestCases; ++i)
        {
                int matrixX, matrixY;
                getline(inFile, line);
                istringstream matrixXYStream(line);
                matrixXYStream>>matrixX;
                matrixXYStream>>matrixY;
                vector<vector<int> > matrix;
                for(int indexX = 0; indexX < matrixX; ++indexX)
                {
                    getline(inFile, line);
                    istringstream matrixXYValStream(line);
                    vector<int> matrixLine;
                    for(int indexY = 0; indexY < matrixY; ++indexY)
                    {
                            int val;
                            matrixXYValStream>>val;
                            matrixLine.push_back(val); 
                    }
                    matrix.push_back(matrixLine);
                }
                ostringstream preResultString;
                preResultString<<"Case #"<<i+1<<": ";
                string result;
                
                if(checkResult(matrix))
                {
                    results.push_back(preResultString.str() + "YES");
                }
                else
                {
                    results.push_back(preResultString.str() + "NO");
                }
        }
        inFile.close();
    }
    else
    {
        cout<<"File couldnt open : "<<endl;
        return false;
    }
    return true;
}

void writeOutput(const list<string> & results)
{
    ofstream outFile("out.txt", ios_base::binary);
    for(list<string>::const_iterator it = results.begin(); it != results.end(); ++it)
    {
        outFile<<(*it)<<'\n';
    }
    outFile.close();
}

int main(int argc, char *argv[])
{
    system("PAUSE");
    list<string> results;
    readInput(results);
    writeOutput(results);
    return EXIT_SUCCESS;
}
