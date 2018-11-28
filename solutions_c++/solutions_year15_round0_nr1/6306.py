#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <cstdlib>
#include <string.h>
#include <time.h>
#include <stdio.h>
#include<sstream>

using namespace std;

class file_op
{

    ifstream infile;
    ofstream outfile;

public:
    bool isopen;
    vector<string> fileread();
    void closefiles();
    void filewrite(string);

};


int main(int argc, const char * argv[])
{
    vector<string> read;
    file_op f;
    int test_cases= atoi(f.fileread()[0].c_str());
    for(int i =0;i<test_cases ;i++)
    {

        int max_req=0,stood_up=0,called=0;
        vector<int> audience;

        vector<string> line=f.fileread();
        max_req=atoi(line[0].c_str());
        for (int x=0;x<line[1].size();x++)
        {
        	int temp;
        	stringstream ss;
        	ss << line[1][x];
        	ss >>temp;
        	audience.push_back(temp);
        }

        for(int j=0;j<audience.size();j++)
        {
        	if(audience[j]!=0 && j> stood_up)
        	{
        		called = called + j - stood_up ;
        		stood_up = j;

        	}
        	stood_up = stood_up + audience[j];

        	if(stood_up >= max_req)
        	{
        		break;
        	}
        }


        f.filewrite("Case #" + to_string(i+1)+": "+to_string(called)+"\n");

        cout<<"\nCase "<<to_string(i+1)<<"\nMax shyness - "<<line[0].c_str()<<"\nAudience - ";
        for(int x=0;x<line[1].size();x++)
        {
        	cout <<to_string(audience[x])<<" ";
        }
        cout<<"\n---------------------------\n";

    }
    f.closefiles();
    return 0;

}

vector<string> file_op::fileread()
{
    vector<string> ret;

    string line;
    char* ch;
    if(!(isopen))
    {
        infile.open ("Input.in");

        isopen=true;
    }

    getline(infile,line);

    ret.push_back(strtok((char*)line.c_str()," "));
    ch=strtok(NULL," ");
    while(ch!=NULL)
    {
        ret.push_back(ch);
        ch=strtok(NULL," ");
    }

    return ret;
}

void file_op::closefiles()
{
    infile.close();
    outfile.close();
}

void file_op::filewrite(string s)
{


    if (!(outfile.is_open()))
    {
        outfile.open ("Output.in");
    }
    outfile<<s;


}
