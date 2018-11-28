#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <numeric>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
using namespace std;
int main()
{
    freopen("A-small-attempt1.in", "rt", stdin);
  	freopen("outputA-small-attempt1.txt", "wt", stdout);
    long long int t;
    long long int smax,stand,frnd,num=0;
    char shy[1111];
    cin>>t;
    while(t--)
    {
        num++;
        cin>>smax;
        cin>>shy;
        stand=0;frnd=0;
        for(int i=0;i<=smax;i++)
        {
            if(stand<i && shy[i]!='0')
            {
                frnd+=i-stand;
                stand+=frnd;
            }

            stand+=shy[i]-'0';

        }


        cout<<"case #"<<num<<": "<<frnd<<endl;
    }
}
