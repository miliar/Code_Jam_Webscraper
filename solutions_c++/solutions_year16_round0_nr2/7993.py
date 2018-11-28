#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<map>
#include<string>

using namespace std;
int main()
{
    freopen("InputB.txt", "r+", stdin);
    freopen("outputB.txt", "w+", stdout);
    int TestCase;
    cin>>TestCase;
    string str;
    int kase= 0;
    while(TestCase--)
    {
        cin>>str;
        str+="+";
        int kounter = 0;


        bool bFoundFirst = false;
        for(int i=0;i<str.size();i++)
        {
            if(str[i]=='-' && bFoundFirst == false)
            {
                kounter++;
                bFoundFirst = true;
            }

            if(str[i]=='+')
                bFoundFirst = false;
        }

        if(str[0]=='-')
            printf("Case #%d: %d\n", ++kase, kounter*2 - 1);
        else
            printf("Case #%d: %d\n", ++kase, kounter*2);


    }
    return 0;
}

