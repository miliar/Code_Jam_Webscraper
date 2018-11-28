#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    ifstream fInput("C:\\Users\\AM185352\\Downloads\\A-large.in");
    ofstream fOutput("C:\\Output.txt");

    int tc;
    fInput>>tc;

    for(int i=1;i<=tc;i++)
    {
        char ch;
        int maxshy; fInput>>maxshy;fInput.get(ch);

        string s;getline(fInput, s);        

        int slen = s.length();

        int tempStand = s[0] - '0';
        int friends=0;
        for(int j=1;j<slen;j++)
        {
            int diff = j -tempStand;
            if((diff>0) && (s[j]!='0'))
            {               
                friends+= diff;  
                tempStand += diff;
            }
            tempStand += s[j]-'0';                            
        }
        fOutput<<"Case #"<<i<<": "<<friends<<endl;
    }
    return 0;
}
