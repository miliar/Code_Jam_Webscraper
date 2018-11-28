#include <iostream>
#include <thread>
#include<algorithm>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
int NUMBER_OF_THREADS=7;
int NUMBER_OF_TEST_CASES;
void worker(int id,int start,int end);


//Data class for each test case
//EDIT_THIS
class data
{
public:
    string line;
    string result="";
    vector<bool> strList;

    void execute(int testCaseNumber)
    {
        result= "Case #"+to_string(testCaseNumber+1)+": ";
        //Perform work for the test case here
        int deltaCount=0;
        if(strList.size()==1)
        {
            if(strList[0])
                result+="0";
            else
                result+="1";
            return;
        }
        for(int i=1;i<strList.size();i++)
        {
            if(strList[i]!=strList[i-1])
                deltaCount++;
        }
        if(!strList[strList.size()-1])
        {
            deltaCount++;
        }
        result+=to_string(deltaCount);
        return;
    }
    void readData()
    {
        getline(cin,line);
        for(int i=0;i<line.size();i++)
        {
            if(line[i]=='+')
                strList.push_back(true);
            else
                strList.push_back(false);
        }
    }
};
vector<data> input_data;


//NO EDIT
int main()
{
    cin>>NUMBER_OF_TEST_CASES;
    cin.ignore();
    input_data.resize(NUMBER_OF_TEST_CASES);

    //Collect input;
    for(int i=0;i<NUMBER_OF_TEST_CASES;i++)
    {
        input_data[i].readData();
    }

    //Initialize threads
    std::vector<std::thread> threadList(NUMBER_OF_THREADS);
    int delta=(NUMBER_OF_TEST_CASES/NUMBER_OF_THREADS)+1;
    int count=0;
    for(int i=0; i<NUMBER_OF_THREADS; i++)
    {
        threadList.at(i)=thread(worker,i,count,count+delta);
        count+=delta;
    }
    for(int i=0;i<NUMBER_OF_THREADS;i++)
    {
        threadList.at(i).join();
    }
    for(int i=0; i<NUMBER_OF_TEST_CASES; i++)
    {
        cout<<input_data[i].result<<"\n";
    }
}


void worker(int id,int start,int end)
{
    for(int i=start; i<end; i++)
    {
        if(i<input_data.size())
        {
            input_data[i].execute(i);
        }
    }
    return;
}

