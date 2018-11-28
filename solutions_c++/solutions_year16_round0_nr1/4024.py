#include <iostream>
#include <string>
#include <memory.h>
#include <map>
#include <vector>
#include <math.h>
#include <fstream>
using namespace std;
map<int,int> m;
int Count;
int pos;
bool IsOk()
{
    for(int i=0;i<10;i++)
    {
        if(m[i]==0)
            return false;
    }
    return true;
}
bool desolve(int num)
{
    while(num)
    {
        int temp = num % 10;
        m[temp]++;
        num=num/10;
    }
    if(IsOk())
        return true;
    return false;

}
int main()
{
    cin>>Count;
    int Case=0;
    ofstream file;
    file.open("output.txt");
    while(Count--)
    {
        Case++;
        bool flag = false;


        m.clear();
        int num;
        cin>>num;
        file<<"Case #"<<Case<<": ";
        int pos =0;
        int temp = num;
        while(temp)
        {
            pos++;
            temp = temp/10;
        }
        for(int i=1;i<=1*pow(10,pos+1);i++)
        {
            temp = num*i;
            if(desolve(temp))
            {
                flag = true;

                file<<temp<<'\n';
                break;
            }

        }
        if(!flag)
            file<<"INSOMNIA"<<'\n';
    }
    file.close();
    return 0;
}
