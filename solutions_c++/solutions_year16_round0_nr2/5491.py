#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<set>
#include<map>
#include<climits>
#include<cstring>
#include<list>
#include<fstream>
#include<queue>
#include<sstream>
#include<stack>
#include<iomanip>

using namespace std;
typedef long long LL;

LL mod=1e9+7;

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);


    ifstream cin("B-large.in");
    ofstream cout("file.txt");

    int T;
    cin>>T;

    for(int I=0; I<T; I++)
    {
        string s;
        cin>>s;

        LL ctr=0;

        for(int i=0; i<s.length(); i++)
        {
            if( (i==0&&s[i]=='-')||(i<s.length()-1&&s[i+1]=='-'&&s[i]=='+'))
                ctr++;
        }

        if(s[0]=='+')
            cout<<"Case #"<<I+1<<": "<<2*ctr<<'\n';
        else cout<<"Case #"<<I+1<<": "<<2*(ctr-1)+1<<'\n';

    }
}

