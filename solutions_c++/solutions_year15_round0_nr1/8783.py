#include <iostream>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <vector>
#include <stdio.h>

#define READERROR   1
#define WRITEERROR  2

using namespace std;

int Ovation(int length,string people);
int getData(string filePath);
int SearchTrick(vector<string> *DataSet,int TotalCount,int countNum);
int writeData(string result);

int main()
{
    string filePath = "/home/anniel/A-large.in";
    getData(filePath);
    return 0;
}

int getData(string filePath){
    int fileSize;
    char * buf;

    int fp = open(filePath.c_str(),O_RDONLY);

    off_t temp = lseek(fp,0,SEEK_END);
    fileSize = temp;
    temp = lseek(fp,0,SEEK_SET);

    buf = (char*)malloc(fileSize);

    size_t bufR = read(fp,buf,fileSize);

    if(bufR != fileSize){
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
    while(ptr = strtok(NULL,"\n")){
        bufSet.push_back(ptr);
        num++;
    }

    SearchTrick(&bufSet,testTotal,num);

    return 0;
}

int SearchTrick(vector<string> *DataSet,int TotalCount,int countNum){

    int i = 0,total=0;
    int ans1=0,ans2=0;
    string number,people,tempStr;

    string resultStr="";

    char resultBuf[1024];

    for(i=0;i<TotalCount;i++){
        tempStr = DataSet->at(i);

        number = tempStr.substr(0,tempStr.find(" "));
        people = tempStr.substr(tempStr.find(" ")+1);

        int int_number = atoi(number.c_str());

        total++;

        int int_temp = Ovation(int_number,people);

        if(total == 100)
            sprintf(resultBuf,"Case #%d: %d",total,int_temp);
        else
            sprintf(resultBuf,"Case #%d: %d\n",total,int_temp);

        resultStr = resultStr + resultBuf;
    }

    writeData(resultStr);

    return 0;
}

int Ovation(int length,string people){
    int numPeople = 0;
    int totalPeople = atoi(people.substr(0,1).c_str());

    if(length == 0)
        return 0;

    for(int i=1;i<=length;i++){
            int first = atoi(people.substr(i-1,1).c_str());
            int second = atoi(people.substr(i,1).c_str());

            if(second != 0){

            if(totalPeople < i){
                    numPeople = numPeople + (i - totalPeople);
                    totalPeople = totalPeople +  (i - totalPeople);
            }
            }
            totalPeople = totalPeople + second;
    }
    return numPeople;
}

int writeData(string result){
    string filePath = "/home/anniel/out.txt";
    int fp = creat(filePath.c_str(),0644);
    fp = open(filePath.c_str(),O_WRONLY);

    int resultLength = strlen(result.c_str());
    ssize_t wBuf = write(fp,result.c_str(),resultLength);

    if(wBuf != resultLength){
        close(fp);
        cout << "Write Error!" << endl;
        return WRITEERROR;
    }
    return 0;
}
