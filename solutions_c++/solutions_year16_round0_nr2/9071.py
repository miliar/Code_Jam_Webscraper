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
int findChar(std::string targetStr,std::string targetChr)
{
    int pos;

    if(targetStr.find(targetChr) != string::npos)
    {
        pos = targetStr.find_first_of(targetChr);
    }
    else
    {
        pos = -1;
    }

    return pos;
}

char*changePos(char targetBuf[], int plusPos,int minusPos,int length)
{
    char tempResbuf[100];
    char changeChr;
    memset(tempResbuf,0,sizeof(tempResbuf));
    int i=0,endPos;

    if(plusPos < minusPos)
    {
        endPos = minusPos;
        changeChr = '-';
    }
    else
    {
        endPos = plusPos;
        changeChr = '+';
    }

    for(i=0; i<endPos; i++)
    {
        tempResbuf[endPos-i-1] = changeChr;
    }

    for(i=0; i<endPos; i++)
    {
        targetBuf[i] = tempResbuf[i];
    }
    return targetBuf;
}

bool CheckBuf(int length,char targetBuf[])
{
    bool res = false;
    int i =0,CountN=0;
    for(i=0; i<length; i++)
    {
        if(targetBuf[i] == '+')
            CountN++;
    }

    if(CountN == length)
        res = true;
    else
        res = false;

    return res;
}
int SearchTrick(vector<string> *DataSet,int TotalCount,int countNum)
{
    long long i = 0,total=0,j=0;
    long long length = 0,pos = 0, minusPos = 0,countN = 0;

    string resultStr="";
    string targetStr = "";
    char *tempStr = "";

    char resultBuf[2048];
    char resBuf[100];

    bool res = false;

    for(i=0; i<TotalCount; i++)
    {
        targetStr = DataSet->at(i);
        countN = 0;
        res = false;

        length = strlen(targetStr.c_str());
        sprintf(resBuf,"%s",targetStr.c_str());

        if(length == 1)
        {
            if(targetStr == "+")
            {
                sprintf(resultBuf,"Case #%d: 0\n",i+1);
            }
            else
            {
                sprintf(resultBuf,"Case #%d: 1\n",i+1);
            }
        }
        else
        {
            while(res != true)
            {
                pos = findChar(targetStr,"+");
                minusPos = findChar(targetStr,"-");

                if(pos == -1)
                {
                    countN++;
                    res = true;
                    break;
                }

                if(minusPos == -1)
                {
                    res = true;
                    break;
                }

                countN++;
                tempStr = changePos(resBuf, pos,minusPos,length);
                sprintf(resBuf,"%s",tempStr);
                res = CheckBuf(length,resBuf);
                targetStr = tempStr;
            }

            sprintf(resultBuf,"Case #%d: %d\n",i+1,countN);
        }
        resultStr = resultStr + resultBuf;
    }

    writeData(resultStr);

    return 0;
}

int main()
{
    string filePath = "/home/anniel/다운로드/B-large.in";
    getData(filePath);
    return 0;
}
