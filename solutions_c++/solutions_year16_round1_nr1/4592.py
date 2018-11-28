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


vector<string> recursiveFill(string ip,vector<char> charList)
{
    vector<string> output;
    if(charList.size()==0)
    {
        output.push_back(ip);
        return output;
    }
    char c = charList[0];
    string s= ip;
    s.push_back(c);
    string t="";
    t.push_back(c);
    t+=ip;
    charList.erase(charList.begin());
    vector<string> output_s = recursiveFill(s,charList);
    vector<string> output_t = recursiveFill(t,charList);
    output.insert(output.begin(),output_s.begin(),output_s.end());
    output.insert(output.begin(),output_t.begin(),output_t.end());
    return output;
}


//Data class for each test case
//EDIT_THIS
class data
{
public:

    string input;
    string result;

    vector<char> charList;
    void execute(int testCaseNumber)
    {

        result= "Case #"+to_string(testCaseNumber+1)+": ";
        //Perform work for the test case here

        for(int i=0;i<input.size();i++)
        {
            charList.push_back(input[i]);
        }

        vector<string> combinations = recursiveFill("",charList);
        sort(combinations.begin(),combinations.end());



        result +=combinations[combinations.size()-1];


        return;
    }
    void readData()
    {
        getline(cin,input);
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

