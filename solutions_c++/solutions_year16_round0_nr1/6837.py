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
int maxtest = 10000000;
//Data class for each test case
//EDIT_THIS


class data
{
public:
    unsigned long long number;
    string result="";
    vector<string> strList;
    array<bool,10> digits;

    bool isComplete()
    {
        for(int i=0;i<10;i++)
        {
            if(!digits[i])
                return false;
        }
        return true;
    }

    void markDigits(unsigned long long input)
    {
        unsigned long long tmp;
        while(input!=0)
        {
            tmp = input%10;
            digits[tmp] = true;
            input/=10;
        }
    }

    void execute(int testCaseNumber)
    {
        result= "Case #"+to_string(testCaseNumber+1)+": ";
        //Perform work for the test case here
        if(number==0)
        {
            result+="INSOMNIA";
            return;
        }
        unsigned long long product;
        for(int i=1;i<maxtest;i++)
        {
            product = number* i;
            markDigits(product);
            if(isComplete())
            {
                result+=to_string(product);
                return;
            }
        }
        result+="INSOMNIA";
        return;
    }
    void readData()
    {
        cin>>number;
        for(int i=0;i<10;i++)
        {
            digits[i]=false;
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

