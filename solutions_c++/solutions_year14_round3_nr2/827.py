//program A

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cmath>
#include<set>
using namespace std;

void print(int i){cout << i << " ";}
void print(string s){cout << s << " ";}
template<class T>void print(vector<T> v){for(int i=0;i<v.size();++i)print(v[i]);cout << endl;}

bool valid(string s)
{
    //cout << endl << s << " ";
    vector<bool> v(26,false);
    char last=' ';
    for(int i=0;i<s.size();++i)
    {
        //cout << i << " ";
        if(last!=s[i])
        {
            char c=s[i]-'a';
            if(v[c])
                return false;
            v[c]=true;
            last=s[i];
        }
    }
    //cout << "T";
    return true;
}

int func(vector<string> v,string prev="")
{
    if(!valid(prev))
        return 0;
    int count=0;int nvaz=false;
    for(int i=0;i<v.size();++i) if(!v[i].empty())
    {
        nvaz=true;
        vector<string> novo=v;
        novo[i]="";
        count+=func(novo,prev+v[i]);
    }
    if(nvaz)
        return count;
    return 1;
}

int main()
{
    freopen("B.in","r",stdin);
    //freopen("B.out","w",stdout);
    int totaltest;
    cin >> totaltest;
    for(int test=1;test<=totaltest;test++)
    {
        printf("Case #%d: ",test);
        
        int n;
        cin >> n;
        vector<string> inp(n);
        for(int i=0;i<n;++i) cin >> inp[i];
        
        cout << func(inp) << endl;
    }
    return 0;
}
