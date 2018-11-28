#include<cstdio>
#include<cstring>
#include<algorithm>
#include<iostream>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
using namespace std;

vector<long long> a;

int check(long long p)
{
    stringstream ss;
    string str;
    ss << p;
    ss >> str;
    for (int i=0;i<str.length()/2;i++)
        if (str[i]!=str[str.length()-1-i]) return 0;
    return 1;
}

int main()
{
    freopen("C.out","w",stdout);
    a.clear();
    for (int i=1;i<=10000000;i++)
        if (check(i) && check((long long)i*i)) a.push_back(i);
    printf("%d\n",a.size());
    for (int i=0;i<a.size();i++)
        printf("%I64d\n",a[i]);
    freopen("C.in","r",stdin);
    return 0;
}
