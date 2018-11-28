#include <iostream>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <vector>
#include <stdio.h>
#include <sstream>

#define READERROR   1
#define WRITEERROR  2

using namespace std;

int SearchTrick(vector<string> *DataSet,int TotalCount,int countNum);

int writeData(string result)
{
    string filePath = "/home/anniel/out.txt";
    int fp = creat(filePath.c_str(),0644);
    fp = open(filePath.c_str(),O_WRONLY);

    int resultLength = strlen(result.c_str());
    ssize_t wBuf = write(fp,result.c_str(),resultLength);

    if(wBuf != resultLength)
    {
        close(fp);
        cout << "Write Error!" << endl;
        return WRITEERROR;
    }
    return 0;
}

int getData(string filePath)
{
    int fileSize;
    char * buf;

    int fp = open(filePath.c_str(),O_RDONLY);

    off_t temp = lseek(fp,0,SEEK_END);
    fileSize = temp;
    temp = lseek(fp,0,SEEK_SET);

    buf = (char*)malloc(fileSize);

    size_t bufR = read(fp,buf,fileSize);

    if(bufR != fileSize)
    {
        cout << "Read Error!" << endl;
        close(fp);
        return READERROR;
    }
    close(fp);

    char * tempbuf;
    char * ptr;
    tempbuf = buf;
    int testTotal=0,num=0;
    vector <string> bufSet;

    ptr = strtok(tempbuf,"\n");
    testTotal = atoi(ptr);
    while(ptr = strtok(NULL,"\n"))
    {
        bufSet.push_back(ptr);
        num++;
    }

    SearchTrick(&bufSet,testTotal,num);

    return 0;
}

std::string compareStr(std::string a, std::string b,std::string c){
    std::string res;

    if(strcmp(a.c_str(),b.c_str()) < 1){
        res = b+c;
    }else{
        res = c+b;
    }
    return res;
}

int SearchTrick(vector<string> *DataSet,int TotalCount,int countNum)
{

    long long i = 0,total=0,countN=0,resBufCount = 0;;
    long long length = 0,j=0,ans = 0,tempStrInt=0;

    string resultStr="";
    string tempStr1 = "",letter = "",targetStr = "", tempStr2 ="";

    char resultBuf[2048];
    int resBuf[10] = {0,};

    bool resBool = false;

    for(i=0; i<TotalCount; i++)
    {
        targetStr = DataSet->at(i);

        length = strlen(targetStr.c_str());
        letter = targetStr.substr(0,1);

        for(j=1;j<length;j++){
                tempStr1 = letter.substr(0,1);
                tempStr2 = targetStr.substr(j,1);

                letter = compareStr(tempStr1,tempStr2,letter);
        }

        sprintf(resultBuf,"Case #%d: %s\n",i+1,letter.c_str());
        resultStr = resultStr + resultBuf;
        memset(resBuf,0,sizeof(resBuf));

    }

    writeData(resultStr);

    return 0;
}

int main()
{
    string filePath = "/home/anniel/다운로드/A-large.in";
    getData(filePath);
    return 0;
}
