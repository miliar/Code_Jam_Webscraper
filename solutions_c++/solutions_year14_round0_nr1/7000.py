//RandomUsername(Nikola Jovanovic)
//Google Code Jam 2014
//Qualification Round
//A : Magic Trick

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <stack>

using namespace std;

int cnt[17];
int t;
int rw,pom;
int ret;
bool badma;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    //cout<<t<<endl;
    for(int tt=1;tt<=t;tt++)
    {
       for(int i=1;i<=16;i++)
        cnt[i]=0;
       scanf("%d",&rw);
       for(int i=0;i<=15;i++)
         {
             scanf("%d",&pom);
             if(i/4+1==rw)
              cnt[pom]++;
         }
       scanf("%d",&rw);
       for(int i=0;i<=15;i++)
         {
             scanf("%d",&pom);
        // cout<<"KRAJ"<<i<<" "<<pom<<" "<<rw<<endl;
             if(i/4+1==rw)
              cnt[pom]++;
         }
       ret=-1;
       badma=false;
       for(int i=1;i<=16;i++)
         {//cout<<cnt[i]<<" ";
            if(cnt[i]==2)
            {
                if(ret==-1)
                    ret=i;
                else
                {
                   badma=true;
                   break;
                }
            }
         }
       if(badma)
        printf("Case #%d: Bad magician!\n",tt);
       else if(ret==-1)
        printf("Case #%d: Volunteer cheated!\n",tt);
       else
        printf("Case #%d: %d\n",tt,ret);
    }
    return 0;
}
