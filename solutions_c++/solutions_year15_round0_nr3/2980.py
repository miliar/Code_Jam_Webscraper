#include <iostream>
#include <cstdio>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<std::string> StringVector;
typedef vector<long> LongVector;
typedef std::vector<long>::iterator iter;

std::string func(std::string strVal,char ch)
{
    if(strcmp(strVal.c_str(),"i") == 0)
    {
        if(ch == 'i')
            return "-1";
        if(ch == 'j')
            return "k";
        if(ch == 'k')
            return "-j";

    }

    else if(strcmp(strVal.c_str(),"-i") == 0)
    {
        if(ch == 'i')
            return "1";
        if(ch == 'j')
            return "-k";
        if(ch == 'k')
            return "j";
    }

    else if(strcmp(strVal.c_str(),"j") == 0)
    {
        if(ch == 'i')
            return "-k";
        if(ch == 'j')
            return "-1";
        if(ch == 'k')
            return "i";
    }

    else if(strcmp(strVal.c_str(),"-j") == 0)
    {
        if(ch == 'i')
            return "k";
        if(ch == 'j')
            return "1";
        if(ch == 'k')
            return "-i";
    }

    else if(strcmp(strVal.c_str(),"k") == 0)
    {
        if(ch == 'i')
            return "j";
        if(ch == 'j')
            return "-i";
        if(ch == 'k')
            return "-1";
    }

    else if(strcmp(strVal.c_str(),"-k") == 0)
    {
        if(ch == 'i')
            return "-j";
        if(ch == 'j')
            return "i";
        if(ch == 'k')
            return "1";
    }

    else if(strcmp(strVal.c_str(),"1") == 0)
    {
        if(ch == 'i')
            return "i";
        if(ch == 'j')
            return "j";
        if(ch == 'k')
            return "k";
    }

    else if(strcmp(strVal.c_str(),"-1") == 0)
    {
        if(ch == 'i')
            return "-i";
        if(ch == 'j')
            return "-j";
        if(ch == 'k')
            return "-k";
    }
}


std::string funcReverse(std::string strVal,char ch)
{
    if(strcmp(strVal.c_str(),"i") == 0)
    {
        if(ch == 'i')
            return "-1";
        if(ch == 'j')
            return "-k";
        if(ch == 'k')
            return "j";

    }

    else if(strcmp(strVal.c_str(),"-i") == 0)
    {
        if(ch == 'i')
            return "1";
        if(ch == 'j')
            return "k";
        if(ch == 'k')
            return "-j";
    }

    else if(strcmp(strVal.c_str(),"j") == 0)
    {
        if(ch == 'i')
            return "k";
        if(ch == 'j')
            return "-1";
        if(ch == 'k')
            return "-i";
    }

    else if(strcmp(strVal.c_str(),"-j") == 0)
    {
        if(ch == 'i')
            return "-k";
        if(ch == 'j')
            return "1";
        if(ch == 'k')
            return "i";
    }

    else if(strcmp(strVal.c_str(),"k") == 0)
    {
        if(ch == 'i')
            return "-j";
        if(ch == 'j')
            return "i";
        if(ch == 'k')
            return "-1";
    }

    else if(strcmp(strVal.c_str(),"-k") == 0)
    {
        if(ch == 'i')
            return "j";
        if(ch == 'j')
            return "-i";
        if(ch == 'k')
            return "1";
    }

    else if(strcmp(strVal.c_str(),"1") == 0)
    {
        if(ch == 'i')
            return "i";
        if(ch == 'j')
            return "j";
        if(ch == 'k')
            return "k";
    }

    else if(strcmp(strVal.c_str(),"-1") == 0)
    {
        if(ch == 'i')
            return "-i";
        if(ch == 'j')
            return "-j";
        if(ch == 'k')
            return "-k";
    }
}

bool isMatchingJ(std::string strInput,long startIndex,long endIndex)
{
    int index;
    std::string strCurResult = "1";


    for(index=startIndex;index<=endIndex;index++)
    {
        strCurResult = func(strCurResult,strInput[index]);

    }
    if(strcmp(strCurResult.c_str(),"j")==0)
        return true;

    return false;

}

int main()
{
     long testCase,curTestCase;
    //cin >> testCase;
    std::string line;
    std::istringstream iss;

    ifstream myfile;
    myfile.open("input.txt",ios::in);

    ofstream outfile;
    outfile.open("out.txt");

    if (std::getline(myfile, line)) {
    iss.str(line);
    iss >> testCase;
    }

    //fscanf(fpt,"%ld\n",&testCase);
   // cout << testCase;
    for(curTestCase=0;curTestCase<testCase;curTestCase++)
    {
        long l,x;
        std::string strVal;
        //cin >> cursize;

        std::istringstream iss2;

        if (std::getline(myfile, line))
            {
        //        cout << line;
            iss2.str(line);
            iss2 >> l;
            iss2 >> x;
            }

         std::istringstream iss3;

        if (std::getline(myfile, line))
            {
        //        cout << line;
            iss3.str(line);
            iss3 >> strVal;
            }

    std::string strInput;
    int inn;
    for(inn=0;inn<x;inn++)
       strInput = strInput+strVal;
    //std::string strInput = "kji";
    long strlen = strInput.length();
    long index,index2;
    std::string strCurResult = "1";

    LongVector veci,veck;
    for(index=0;index<strlen;index++)
    {
        strCurResult = func(strCurResult,strInput[index]);
      //  cout << strCurResult << endl;
        if(strcmp(strCurResult.c_str(),"i")==0)
        {
      //      cout << index <<" ";
            veci.push_back(index);
        }
    }

    strCurResult = "1";
    //cout<< "newline"<< endl;
    for(index=strlen-1;index>=0;index--)
     {
        strCurResult = funcReverse(strCurResult,strInput[index]);
  //      cout << strCurResult << endl;
        if(strcmp(strCurResult.c_str(),"k")==0)
        {
        //    cout << index <<" ";
            veck.push_back(index);
        }
     }

    std::reverse(veck.begin(),veck.end());

    //cout << endl;
  //  cout << veci.size() << " "<< veck.size()<< endl;
    int isMatch = 0;
    std::string strRes = "NO";
    long count = 0;
    iter it;
    if(veci.size() != 0 && veck.size() != 0)
    {

    for(index=0;index<veci.size();index++)
    {
        long lCurValI = veci[index];
        strCurResult = "1";
        for(index2=lCurValI+1;index2<strlen;index2++)
        {
        strCurResult = func(strCurResult,strInput[index2]);
      //  cout << strCurResult << endl;
            if(strcmp(strCurResult.c_str(),"j")==0)
            {


               it = std::find(veck.begin(),veck.end(),index2+1);
               if(it != veck.end())
                {
                    strRes  = "YES";
                    isMatch = 1;
                    index2 = strlen;
                    index = veci.size();
                    break;
                }
               // cout << index <<" ";
            }
        }
    }
    }

    outfile << "Case #"<<curTestCase+1<<": "<<strRes<<endl;
    //cout << isMatch << endl;
    }
    return 0;
}
