#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <queue>
#include <map>

#define pb push_back
#define lm 510

using namespace std;
int n;
string s;
int main() {

    freopen("A-large.in","r",stdin);
    freopen("dataA.out","w",stdout);
    cin>>n;
    int l[11];
    for(int k=1; k<=n; k++)
    {
        cin>>s;
        for(int i=0; i<10; i++)
        {
            l[i]=0;
        }
        for(int i=0; i<s.size(); i++)
        {
            if(s[i]=='Z')
                l[0]++;
            else if(s[i]=='W')
                l[2]++;
            else if(s[i]=='H')
                l[3]++;
            else if(s[i]=='U')
                l[4]++;
            else if(s[i]=='V')
                l[5]++;
            else if(s[i]=='X')
                l[6]++;
            else if(s[i]=='S')
                l[7]++;
            else if(s[i]=='G')
                l[8]++;
            else if(s[i]=='O')
                l[1]++;
            else if(s[i]=='I')
                l[9]++;
        }
        l[1]-=l[0]+l[2]+l[4];
        l[3]-=l[8];
        l[7]-=l[6];
        l[5]-=l[7];
        l[9]-=l[5]+l[6]+l[8];
        cout<<"Case #"<<k<<": ";
        for(int i=0;i<10; i++)
        {
            for(int j=0; j<l[i]; j++)
            {
                cout<<i;
            }
        }
        cout<<'\n';
    }

    return 0;
}
