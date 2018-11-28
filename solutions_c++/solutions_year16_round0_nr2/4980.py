//
#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<map>
#include<set>
#include<climits>
#include<fstream>
#include<iomanip>
#include<queue>
#include<stack>
#define lli long long

using namespace std;


int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

     ifstream cin("B.in");
    ofstream cout("B.out");


    int T,l=0,br=0;
    cin>>T;
    string s;

    for(int t1=1;t1<=T;t1++)
    {
        cin>>s;

        l=0; br=0;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-'){l=1;}
        }

        if(l==0){cout<<"Case #"<<t1<<": "<<0<<"\n";continue;}

        for(int i=1;i<s.size();i++)
        {
            if(s[i]=='-' && s[i-1]=='+')br++;
        }
        br*=2;
        if(s[0]=='+')br--;
        br++;
        cout<<"Case #"<<t1<<": "<<br<<"\n";

    }

    return 0;
}


