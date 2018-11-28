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
    int T,N,t;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> T;

    for(t=1;t<=T;t++)
    {
        cin >> N;
        cout << "Case #"<<t<<": ";
        int check = 0;
        if(N==0)
            cout << "INSOMNIA" << endl;
        else
        {
            int i=1;
            while(check!=1023)
            {
                int temp = i*N;
                while(temp)
                {
                    check = check | (1<<(temp%10));
                    temp/=10;
                }
                i++;
            }
            cout << (i-1)*N << endl;

        }
    }

    return 0;
}
