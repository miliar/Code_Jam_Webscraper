#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <queue>

#define pb push_back
#define lm 510

using namespace std;
int t,n,c;
string s;
bool ok;
int main() {

    freopen("B-large.in","r",stdin);
    freopen("data.out","w",stdout);
    cin>>t;
    for(int j=1; j<=t; j++)
    {
        cin>>s;
        ok=true;
        c=0;
        while(ok)
        {
            ok=false;
            for(int i=0; i<s.size(); i++)
            {
                if(s[i]=='-')
                    ok=true;
                if(s[i]=='+' && ok)
                {
                    break;
                }
                if(s[i]=='-')
                    s[i]='+';
                else
                    s[i]='-';
            }
            if(!ok)
            {
                break;
            }
            else
                c++;
        }
        printf("Case #%d: %d\n",j,c);
    }
    return 0;
}
