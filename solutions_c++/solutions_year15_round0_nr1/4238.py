#include <cmath>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <stack>

using namespace std;

int main()
{
    freopen("A-large-practice.in","r", stdin);
    freopen("result.out","w", stdout);

    int T;
    int N,X,r1,r2,r3,t,c1,c2=0,c=0,c10=0,large;
    string s="",s1="";

    cin>>T;
    for(int i=1;i<=T;i++)
    {
        c = 0;
        c1 = 0;
        cin>>N>>s;

        for(int j=0;j<=N;j++)
        {
            s1=s.at(j);
            r1 = atoi(s1.c_str());
            if(j == 0)
               c1=r1;
            else
            {
                //c1=c1+r1;
                if(c1 < j)
                {
                    c = c + (j-c1);
                    c1 = c1 + (j-c1) + r1;
                }
                else
                {
                    c1=c1+r1;
                }
            }
            //cout<<c<<" ";

        }
        cout<<"Case #"<<i<<": "<<c<<"\n";
    }

    fclose(stdout);
    fclose(stdin);
    return 0;
}
