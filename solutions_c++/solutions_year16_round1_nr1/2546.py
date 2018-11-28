#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <cmath>
using namespace std;
string ans;
char s[1020];
int n,m;
int T;
int lastcmp;
bool cmp(string &ss, char t)
{
    if(t>ss[0])
    {
        lastcmp = 0;
        return true;
    }
    if(t<ss[0])
    {
        lastcmp = 0;
        return false;
    }
    
    int len = ss.length();
    //++lastcmp;
    for(int i=0;i<ss.length()-1;++i)
    {
        
        if(ss[i]>ss[i+1])return true;
        if(ss[i]<ss[i+1])return false;
    }
//    if(lastcmp)return true;else return false;
    
    if(ss[len-1]<t)return true;else return false;
}
int main()
{
//    freopen("A1in.txt","r",stdin);
//    freopen("A.out","w",stdout);
    
    scanf("%d\n",&T);
    for(int ii=1;ii<=T;++ii)
    {
        memset(s,0,sizeof(s));
        scanf("%s",s);
        
        int len= strlen(s);
        
    //    printf("%d\n",len);
        
        ans = "";
        
        lastcmp = 0;
        
        for(int i=0;i<len;++i)
        {
            char x = s[i];
            
            if(cmp(ans,x))
            {
                ans = x + ans;
            }else
            {
                ans = ans + x;
            }
            
        }
        printf("Case #%d: %s\n",ii,ans.c_str());
    }
    return 0;
}