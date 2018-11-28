#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <map>

using namespace std;
int main()
{
    int n;
    cin>>n;
    int m;
    string s;
    int nmn = 0;
    int sum = 0;
    for(int i = 0;i < n;i++)
    {
        sum = 0;
        nmn = 0;
        cin>>m>>s;
        for(int j = 0; j < s.length();j++)
        {
            if(j <= nmn )
            {
                nmn+=int(s[j]-48);
            }
            else if(j > nmn)
            {
                while(nmn != j)
                {nmn++;
                sum++;}
                nmn+=int(s[j]-48);
            }
            if(nmn >= m)
                {cout<<"case #"<<i+1<<": "<<sum<<endl;
                break;}

        }


    }

}
