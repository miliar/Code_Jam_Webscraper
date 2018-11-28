#include<iostream>
#include<fstream>
#include<map>
#include<algorithm>
using namespace std;

map <int,int> treecheck;
map <string,int> s;

void maketree(string root,int m,int n)
{
    if(m==n){return;}
    for(int i=1;i<=n;++i)
    {
        string str=root.substr(0,i);
        reverse(str.begin(),str.end());
        for(int j=0;j<i;++j)
        if(str[j]=='+'){str[j]='-';}else{str[j]='+';}
        str+=root.substr(i,n-i);
        if(str.find('-')!=string::npos)
        {
            if(m+1<s[str]||s[str]==0){s[str]=m+1;maketree(str,m+1,n);}
        }
    }

}
void construct(int n)
{
    treecheck[n]=1;
    string str;
    for(int i=1;i<=n;++i)
        str+='+';
    maketree(str,0,n);
}
int main()
{
    ifstream ins;
    ofstream outs;
    ins.open("q2.in",ios::in);
    outs.open("q2.out",ios::out);
    int t;
    ins>>t;
    for(int i=1;i<=t;++i)
    {
        string k;
        ins>>k;
        int sz=k.size();
        if(!treecheck[sz]){construct(sz);}
        outs<<"Case #"<<i<<": "<<s[k]<<endl;
    }
    ins.close();
    outs.close();
}
