/*
 * OminousOmino.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: tushar
 */

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

        int x=0,r=0,c=0;
        vector<string> line=f.fileread();
        x=atoi(line[0].c_str());
        r=atoi(line[1].c_str());
        c=atoi(line[2].c_str());
        string result = "RICHARD";
        int sum = r*c;
        switch(x)
        {
        	case 1: result = "GABRIEL";

        		break;

        	case 2: if((sum%2 ) == 0)
					{
        				result = "GABRIEL";
					}
        	    break;

        	case 3:if((sum==6) || (sum==9) || (sum==12) )
					{
						result = "GABRIEL";
					}
        	    break;

        	case 4:if((sum==12) || (sum==16))
					{
						result = "GABRIEL";
					}
        	    break;

        }


        f.filewrite("Case #" + to_string(i+1)+": "+result+"\n");


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



