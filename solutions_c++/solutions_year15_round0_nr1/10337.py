#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <string>
#include <cstring>
#include <fstream>
using namespace std;

int *char_int(char ch[])
{
    int num[sizeof(ch)];
    for(int i=0;i<sizeof(ch);i++)
    {
        num[i] = ch[i]-'0';
    }

    return num;
}


int main()
{

    int t;
    cin>>t;

    int n;
    int result[t];
    for(int i=0;i<t;i++)
    {

        cin>>n;

        int lis[n+1],need[n+1];
        int sum = 0;
        int sum1 = 0;
        int counter = 0;
        int counter1 = 0;
        string s;

        cin>>s;

        char c[n+1];
        strncpy(c, s.c_str(), sizeof(c));


        for(int k=0;k<sizeof(c);k++)
        {
            lis[k] = c[k]-'0';
        }

    for(int k=0;k<n+1;k++)
        {
            sum = 0;
            if(lis[k]!=0)
            {
                need[k] = k;
            }
            else
            {
                need[k] = 0;
            }
            if(counter<=need[k])
            {
                sum = need[k]-counter;
            }
            counter += lis[k] + sum;
            sum1 += sum;
        }
          result[i] = sum1;
    }

    ofstream file;
    file.open("file.txt");

    for(int i=0;i<t;i++)
    {
        file<<"Case"<<" #"<<i+1<<": "<<result[i]<< endl;
    }

    file.close();


    return 0;
}
