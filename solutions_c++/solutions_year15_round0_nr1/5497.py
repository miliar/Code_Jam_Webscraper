#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<iostream>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
#include<cmath>
#include<queue>
#include<stack>
#include<deque>


using namespace std;

typedef pair<int,int> ii;
typedef set<int> si;
typedef map<string, int> msi;


int main()
{
    int cases =1;

    int t;

    while(cin >> t)
    {
        while(t--)
        {
            int cnt=0;

            int shyness;
            string peoples;

            cin >> shyness >> peoples;
            int total = 0;

            for(int i=0; i<=shyness; i++)
            {
                if(i > total + cnt)
                {
                    cnt+= i-(total+cnt);
                }

                total += peoples[i]-'0';
            }


            printf("Case #%d: %d\n", cases++, cnt);
        }
    }


    return 0;
}
