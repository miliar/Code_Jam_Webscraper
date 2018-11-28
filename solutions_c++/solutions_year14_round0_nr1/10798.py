#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <math.h>
using namespace std;
int tab[16];

void zeroes()
{
    for (int i = 0; i < 16; ++i){
        tab[i] = 0;
    }
}

int main()
{
    vector <string> outputStr;
    int T = 0;
    ifstream inFile;
    ofstream outFile;
    stringstream ss;
    string line;
    //stringstream ss;
    int temp;
    double dtemp;
    string output;

    inFile.open("A-small-attempt3.in");
    if(!inFile.is_open())
    {
        printf("Input file is invalid\n");
    }
    getline(inFile, line);
    //std::istringstream ss(line);
    ss << line;

    ss >> T;
    ss.clear();

    //cout << T << endl;

    for (int case_ = 0; case_ < T; case_++ ){
        //cout << "case: " << case_ << endl;
        zeroes();
        getline(inFile, line);
        std::stringstream stream(line);
        //cout << line << endl;
        int row1;
        stream >> row1;
        //cout << "row1: " << row1 << endl;
        for (int i = 0; i < 4; ++i){
            getline(inFile, line);
            //cout << "line: " << line << endl;
            //stream(line);
            stream.str(line);
            if (i == row1-1){
                int l;
                stream >> l;
                //cout << l << " ";
                tab[l-1]++;
                stream >> l;
                //cout << l << " ";
                tab[l-1]++;
                stream >> l;
                //cout << l << " ";
                tab[l-1]++;
                stream >> l;
                //cout << l << " ";
                tab[l-1]++;
            }
        }
        getline(inFile, line);
        stream.str(line);
        //cout << line << endl;
        int row2;
        stream >> row2;
        //cout << "row2: " << row2 << endl;
        for (int i = 0; i < 4; ++i){
            getline(inFile, line);
            //stream(line);
            stream.str(line);
            if (i == row2-1){
                int l;
                stream >> l;
                tab[l-1]++;
                //cout << l << " ";
                stream >> l;
                tab[l-1]++;
                //cout << l << " ";
                stream >> l;
                tab[l-1]++;
                //cout << l << " ";
                stream >> l;
                tab[l-1]++;
                //cout << l << endl;
            }
        }
        int count2 = 0;
        int answ = 0;
        for (int i = 0; i < 16; ++i){
            if (tab[i]==2){
                answ = i+1;
                count2++;
            }
        }
        string res;
        if (count2 == 0){
            res = string("Volunteer cheated!");
        }else if (count2 == 1){
            stringstream ss;
            ss << answ;
            res = ss.str();
        }else {
            res = string("Bad magician!");
        }

        string resLine("Case #");
        stringstream s2;
        s2 << case_+1;
        stringstream s3;
        s3 << res;
        resLine.append(s2.str()).append(": ");
        s2.clear();
        resLine.append(s3.str()).append("\n");
        //cout << resLine;
        outputStr.push_back(resLine);
    }
    inFile.close();
    fstream plik( "outputA.in", ios::out );

    for (int i = 0; i < T; i++){
        plik << outputStr.at(i);
    }
    plik.close();
    //cout << T << endl;
    return 0;
}
