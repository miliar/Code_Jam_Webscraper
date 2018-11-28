#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(void)
{
    ifstream inputFile;
    ofstream outputFile;
    string temp;
    char *count;
    char number[20];
    int a;
    int b;
    int possibilities;
    int caseNum = 1;

    outputFile.open("output.txt");
    inputFile.open("input.txt");
    getline(inputFile,temp);
    count = new char[temp.length()];
    for(unsigned int i=0;i<temp.length();i++){
        count[i] = temp.at(i);
    }

    for(int i=0;i<atoi(count);i++){
        possibilities = 0;
        getline(inputFile,temp);
        unsigned int pos = 0;
        unsigned int offset = 0;
        while(temp.at(pos) != ' '){
            number[pos] = temp.at(pos);
            pos++;
        }
        a = atoi(number);
        memset(number,0,20);
        offset = pos;
        pos = 0;
        while(pos+offset < temp.length()){
            number[pos] = temp.at(pos+offset);
            pos++;
        }
        b = atoi(number);
        memset(number,0,20);

        for(int j=a;j<=b;j++){
            string num = "";
            string rev = "";
            char buff[20];
            _itoa_s(j,buff,20,10);
            num.append(buff);
            for(unsigned int k=0;k<num.length();k++){
                rev.push_back(num.at(num.length()-k-1));
            }

            if(num.compare(rev) == 0){
                float tmp = sqrt((float)j);
                if(tmp == (int)tmp){
                    num = "";
                    rev = "";
                    _itoa_s((int)tmp,buff,20,10);
                    num.append(buff);
                    for(unsigned int k=0;k<num.length();k++){
                        rev.push_back(num.at(num.length()-k-1));
                    }
                    if(num.compare(rev) == 0){
                        possibilities++;
                    }
                }
            }
        }

        cout << "Case #" << caseNum << ": " << possibilities << endl;
        outputFile << "Case #" << caseNum++ << ": " << possibilities << endl;
    }

    return 0;
}

