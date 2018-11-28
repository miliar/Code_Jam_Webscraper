#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#define F(i,n) for(int i=0;i<n;i++)
using namespace std;

int main()
{
    int T,t,i,j;
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> T;
    string str;
    for(t=1;t<=T;t++)
    {
        int flips=0;
        cin >> str;
        int n = str.length();
        cout << "Case #"<<t<<": ";
        while (true)
        {
            for(i=n-1;i>=0;i--)
            {
                if(str[i]=='-')
                    break;
            }
            if(i==-1)
                break;
            else
            {
                bool flip = false;
                for(j=0;j<i;j++)
                {
                    if(str[j]=='-')
                        break;
                    else
                    {
                        flip = true;
                        str[j]='-';
                    }
                }
                if(flip)
                    flips++;
                string temp = str;
                for(j=0;j<=i;j++)
                {
                    if(temp[j]=='-')
                        str[i-j]='+';
                    else
                        str[i-j]='-';
                }
                flips++;
        }
        }
        cout << flips << endl;
    }
    return 0;
}
