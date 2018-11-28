//.cpp
//Yaohung Mike Tsai 1.1.2015
//Description: 

#include<iostream>
#include<vector>
#include<stdio.h>
using namespace std;
int main(int argc, char* argv[])
{
    int cases;
    int aud;
    char temp;
    int level;
    int sum;
    int max;
    string s;
    cin >> cases;
    for (int i=0;i<cases;i++)
    {
        int need=0;
        int up=0;
        cin >> level;
        cin >> s;
        sum=0;
        max=0;
        for (int j=0;j<level;j++)
        {
            temp=s[j];
            aud=temp-'0';
            sum+=aud;
            if(max<j+1-sum)
                max=j+1-sum;
        }
        cout << "Case #" << i+1 << ": " << max << endl;
        
    }






    return 0;
}
