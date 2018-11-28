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


    ifstream cin("A-large.in");
    ofstream cout("file.txt");

    int T;
    cin>>T;

   for(int I=0; I<T; I++)
   {
        string s;
        cin>>s;

        string ret;

        ret+=s[0];

        for(int i=1; i<s.length(); i++)
        {
            if(s[i]>=ret[0])
               ret=s[i]+ret;
            else
                ret=ret+s[i];
        }

        cout<<"Case #"<<I+1<<": "<<ret<<'\n';

   }

}

