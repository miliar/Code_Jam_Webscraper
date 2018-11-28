#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A_output_large.txt","w",stdout);
    char s[1100];
    int T;
    scanf("%d",&T);
    list<char> ans;
    for (int index=1;index<=T;index++)
    {
        scanf("%s",s);
        ans.clear();
        ans.push_back(s[0]);
        int N=strlen(s);
        for (int i=1;i<N;i++)
        {
            if (s[i]>=ans.front())
            {
                ans.push_front(s[i]);
            }else{
                ans.push_back(s[i]);
            }
        }
        printf("Case #%d: ",index);
        for (list<char>::iterator it=ans.begin();it!=ans.end();it++)
        {
            printf("%c",*it);
        }
        printf("\n");
    }
    return 0;
}
