#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<vector>

#define pii pair<int,int>
#define F first
#define S second
#define MOD 1000000007
#define itt iterator
#define ritt reverse_iterator
#define LL long long

using namespace std;

int t;
char s[1005];
list<char> mlist;

int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);

    scanf("%d",&t);
    for(int z=1;z<=t;z++)
    {
        mlist.clear();
        scanf("%s",s);
        mlist.push_back(s[0]);
        for(int i=1;s[i]!='\0';i++)
        {
            if(mlist.front()>s[i])      mlist.push_back(s[i]);
            else                        mlist.push_front(s[i]);
        }
        printf("Case #%d: ",z);
        for(list<char>::itt it=mlist.begin();it!=mlist.end();it++)      printf("%c",*it);
        printf("\n");
    }
    return 0;
}
