#include <iostream>
#include <string>
#include <memory.h>
#include <map>
#include <vector>
#include <math.h>
#include <fstream>
using namespace std;
int NUM;

int main()
{
    cin>>NUM;
    int Case = 0;
    ofstream file;
    file.open("output.txt");
    while(NUM--)
    {
        Case++;
        string s;
        cin>>s;
        file<<"Case #"<<Case<<": ";
        int Len = s.length();
        int num=0;
        char before;
        char now;
        for(int i=Len-1;i>=0;i--)
        {
            if(i==Len-1)
            {
                now = s[i];
                if(now=='+')
                    num=0;
                else num=1;
                before=now;
                continue;
            }
            now = s[i];
            if(now==before)
            {
                continue;
            }
            else{
                before=now;
                num++;
            }
        }
        file<<num<<"\n";




    }
    file.close();
    return 0;
}
