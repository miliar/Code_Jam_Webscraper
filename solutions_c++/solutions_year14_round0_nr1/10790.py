#include <iostream>
#include <fstream>
#include "stdio.h"
#include "stdlib.h"
#include "string.h"

using namespace std;

class CString
{
    public:
    string Readline(const int& x, ifstream& file)
    {
        string sTemp;
        for(int i=0;i<x;i++)
        {
            getline(file,sTemp);
        }
        return sTemp;
    }

};
class MagicTrick
{
    public:
    long output(string str1, string str2,int &row)
    {
        int count = 0;
        int r1[4];
        int r2[4];

        sscanf(str1.c_str(),"%d %d %d %d",&r1[0],&r1[1],&r1[2],&r1[3]);
        sscanf(str2.c_str(),"%d %d %d %d",&r2[0],&r2[1],&r2[2],&r2[3]);
        for(int i = 0; i<4; i++)
        {
            for(int j = 0; j<4;j++)
            {
                if(r1[i] == r2[j])
                {
                    row = r1[i];
                    count++;
                }
            }
        }
        return count;

    }
};
int main()
{
    CString obj;
    MagicTrick magic;
    string str,str1,str2,sTemp;
    ifstream input;
    fstream output;
    output.open("Sample output.txt",ios::out);
    input.open("A-small-attempt3.in",ios::in);
    getline(input,str);
    int NoOfCase;
    int row1,row2,rowpos,cardno;
    long count;
    NoOfCase = 0;
    while(NoOfCase != atoi(str.c_str()))
    {
        NoOfCase++;
        getline(input,sTemp);
        row1 = atoi(sTemp.c_str());
        str1 = obj.Readline(row1,input);
        rowpos = 5-row1;
        row2 = atoi((obj.Readline(rowpos,input)).c_str());
        str2 = obj.Readline(row2,input);
        rowpos = 4-row2;
        obj.Readline(rowpos,input);
        count = magic.output(str1,str2,cardno);
        if(count==1)
        output<<"Case #"<<NoOfCase<<": "<<cardno<<endl;
        else if(count > 1)
        output<<"Case #"<<NoOfCase<<": "<<"Bad magician!"<<endl;
        else
        output<<"Case #"<<NoOfCase<<": "<<"Volunteer cheated!"<<endl;

    }
    return 0;
}
