#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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

using namespace std;

string check(string s,string z)
{
    string s1;
    if(s[0]=='1' && z[0]=='1'){return "1";}
    else if(s[0]=='1' && z[0]=='i'){return "i";}
    else if(s[0]=='1' && z[0]=='j'){return "j";}
    else if(s[0]=='1' && z[0]=='k'){return "k";}
    else if(s[0]=='i' && z[0]=='1'){return "i";}
    else if(s[0]=='i' && z[0]=='i'){return "-1";}
    else if(s[0]=='i' && z[0]=='j'){return "k";}
    else if(s[0]=='i' && z[0]=='k'){return "-j";}
    else if(s[0]=='j' && z[0]=='1'){return "j";}
    else if(s[0]=='j' && z[0]=='i'){return "-k";}
    else if(s[0]=='j' && z[0]=='j'){return "-1";}
    else if(s[0]=='j' && z[0]=='k'){return "i";}
    else if(s[0]=='k' && z[0]=='1'){return "k";}
    else if(s[0]=='k' && z[0]=='i'){return "j";}
    else if(s[0]=='k' && z[0]=='j'){return "-i";}
    else if(s[0]=='k' && z[0]=='k'){return "-1";}
    else if(s[0]=='-'){s1=s; s.clear(); s+=s[1];
        if(s[0]=='1' && z[0]=='1'){return "-1";}
    else if(s[0]=='1' && z[0]=='i'){return "-i";}
    else if(s[0]=='1' && z[0]=='j'){return "-j";}
    else if(s[0]=='1' && z[0]=='k'){return "-k";}
    else if(s[0]=='i' && z[0]=='1'){return "-i";}
    else if(s[0]=='i' && z[0]=='i'){return "1";}
    else if(s[0]=='i' && z[0]=='j'){return "-k";}
    else if(s[0]=='i' && z[0]=='k'){return "j";}
    else if(s[0]=='j' && z[0]=='1'){return "-j";}
    else if(s[0]=='j' && z[0]=='i'){return "k";}
    else if(s[0]=='j' && z[0]=='j'){return "1";}
    else if(s[0]=='j' && z[0]=='k'){return "-i";}
    else if(s[0]=='k' && z[0]=='1'){return "-k";}
    else if(s[0]=='k' && z[0]=='i'){return "-j";}
    else if(s[0]=='k' && z[0]=='j'){return "i";}
    else if(s[0]=='k' && z[0]=='k'){return "1";}
    }
}
int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int l,x;
        string s,s1,s2;
        bool check1=0,checki=0,checkk=0,check_1=0;
        cin>>l>>x;
        vector <string> v,v2;
        cin>>s1;
        s2+='s';
        for(int j=0;j<x;j++)
        {
            for(int k=0;k<l;k++)
            {
                s2[0]=s1[k];
                if(s.size()==0){s+=s1[k];}
                else{s=check(s,s2);}
                if(s[0]=='i'){checki=1;}
                if(checki==1 && s[0]=='k'){checkk=1;}
                if(checki==1 && checkk==1 && j==x-1 && k==s1.size()-1 && s=="-1"){check1=1;}
            }
        }
        if(check1==0){cout<<"Case #"<<i+1<<": "<<"NO"<<endl;}
        else{cout<<"Case #"<<i+1<<": "<<"YES"<<endl;}
    }
    return 0;
}
