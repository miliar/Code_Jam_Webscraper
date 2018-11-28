
#include <string.h>
#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <cstdio>
#include <cmath>
#include <queue>
#include <fstream>
#define  LL long long
#define MOD 1000000007

using namespace std;


int main()
{
    int T;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j;
    int cas=1;
    string s;
    string cur;
    string str;
    string tmp;

    cin>>T;
    while(T--)
        {
            cin>>s;
            i=0;
            cur=s.substr(0,1);
            for(i=1;i<s.size();i++)
                {
                    str=s.substr(i,1);
                    tmp=cur.substr(0,1);

                    if(tmp.compare(str)>0) cur=cur+str;
                    else cur=str+cur;
                  // cout<<str<<"  "<<tmp<<endl;
                    //cout<<i<<" "<<cur<<endl;
                }
            cout<<"Case #"<<cas++<<": "<<cur<<endl;
        }
    return 0;
}
