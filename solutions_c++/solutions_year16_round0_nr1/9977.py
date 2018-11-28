#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<map>
#include<set>
#include<vector>
#include<queue>
#include<stack>
#include<bitset>
#include<sstream>
using namespace std;

map<char,int>mp;

int main()
{
    long long t,tt=1,n;
    //freopen("read.txt","r",stdin);
    //freopen("A-smallwrite.txt","w",stdout);
    scanf("%lld",&t);
    while(tt<=t){
        scanf("%lld",&n);
        if(n==0){
            printf("Case #%lld: INSOMNIA\n",tt++);
            continue;
        }
        set<char>se;
        long long count=2,num=n;

        for(long long i=2;;i++){
            string s;
            ostringstream convert;
            convert<<num;
            s=convert.str();
            for(long long i=0;i<s.size();i++){
                if(mp[s[i]]==0){
                    mp[s[i]]=1;
                    se.insert(s[i]);
                }
            }
            if(se.size()==10)
                break;
            num=n*i;
        }
        se.clear();
        mp.clear();
        printf("Case #%lld: %lld\n",tt++,num);
    }
    //fclose(stdout);
    return 0;
}
