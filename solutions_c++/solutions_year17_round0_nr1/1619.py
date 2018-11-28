#include <iostream>
#include <fstream>
#include <set>
typedef long long Int;
using namespace std;
bool validate(const string & s)
{
    for(int i=0;i<s.length();i++)
        if(s[i]=='-')
            return false;
    return true;
}

void flip(string &s,const Int& st,const Int& k)
{
    for(int i=0;i<k;i++)
        s[i+st]=(s[i+st]=='+')?'-':'+';
}
Int solve(string s,Int K)
{
    int cur=0;
    int actions=0;
    while(cur<s.length())
    {
        while(s[cur]=='+'){cur++;if(cur==s.length())goto end_it;}
        if(cur+K>s.length()) break;
        flip(s,cur,K);
        actions++;
        //cur+=K;
        //cout<<s<<"  "<<cur<<endl;
    }
end_it:
    if(validate(s))
        return actions;
    return -1;
}
int main()
{
    ifstream in("A-large(2).in");
    ofstream out("A-small.out");
#define cin in
#define cout out
    int T;
    cin>>T;
    for(int iT=0;iT<T;iT++)
    {
        string s;
        Int n;
        cin>>s>>n;
        int k=solve(s,n);
        cout<<"Case #"<<iT+1<<": ";
        if(k==-1)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<k<<endl;
    }
    return 0;
    return 0;
}
