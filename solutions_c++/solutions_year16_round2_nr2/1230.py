#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

bool ok(int num,string &s){
    string s1;
    while(num){
        s1 += num%10 +'0';
        num/=10;
    }
    while(s1.size() < s.size())
        s1.push_back('0');
    reverse(s1.begin(),s1.end());
    bool ret = true;
    for(int i=0;i<s1.size();i++)
        if(!((s[i] == '?')||s[i] == s1[i]))
            return false;
    return true;
}

string get(int num,string &s){
    string s1;
    while(num){
        s1 += num%10 +'0';
        num/=10;
    }
    while(s1.size() < s.size())
        s1.push_back('0');
    reverse(s1.begin(),s1.end());
    return s1;
}
int main()
{
    int T,cas = 1;
    int J;
    string a,b;
    freopen("C:\\Users\\L\\Downloads\\B-small-attempt0 (1).in","r",stdin);
    freopen("C:\\Users\\L\\Downloads\\B-small-attempt0 (1).out","w",stdout);
    scanf("%d",&T);
    while(T--){
        int besta = 0, bestb = 0,best = 1000;
        cin>>a>>b;
        int l1 = pow(10,a.size())+1;
        int l2 = pow(10,b.size())+1;
        for(int i=0;i<1000;i++)
            for(int j=0;j<1000;j++)
                if(abs(i-j)<best&&ok(i,a) && ok(j,b)){
                    best = abs(i-j);
                    besta = i;
                    bestb = j;
                }
        printf("Case #%d: ",cas++);
        string ans1 = get(besta,a);
        string ans2 = get(bestb,b);
        printf("%s %s\n",ans1.c_str(),ans2.c_str());
    }
    return 0;
}
