#include<stdio.h>
#include<set>
#include<cstring>
using namespace std;
set<char> vowels;
int count[1000011],n;
char name[1000011];
void precalc();
bool getcount(int,int);
int main ()
{
    vowels.insert('a');
    vowels.insert('e');
    vowels.insert('o');
    vowels.insert('i');
    vowels.insert('u');
    freopen("out.txt","w",stdout);
    freopen("A-small-attempt0.in","r",stdin);
    int t,w=1;
    scanf ("%d",&t);
    int cou;
    while (t--){

        memset(count,0,sizeof count);
        scanf ("%s %d",name,&n);
        precalc();
        int len=strlen(name);
//        printf("%d",getcount(0, 8));
        cou=0;
        for (int i=0;i<len;i++)
        {
            for (int j=i;j<len;j++)
            {
                cou+=getcount(i,j);
            }
        }
        printf("Case #%d: %d\n",w,cou);
        w++;
    }
}
void precalc()
{
    int var=0;
    int len=strlen (name);
    count [len]=0;
    for (int i=len-1;i>=0;i--)
    {
        if (vowels.count (name[i])==0)
            var++;
        count[i]=var;
    }
    return ;
}
bool getcount(int a,int b)
{
    int var=0,maxcount=0;
    for (int i=a;i<=b;i++)
    {
        if (vowels.count(name[i]))
            var=0;
        else
        {
            var++;
            maxcount=max(var,maxcount);
        }
    }
    return maxcount>=n;
}
