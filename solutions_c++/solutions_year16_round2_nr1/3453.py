
///////////////////
//  Shamim Ehsan //
//  SUST CSE 12  //
//  2012331035   //
///////////////////
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<stdlib.h>
#include<limits.h>
#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#include<deque>
#include<algorithm>
#define PI (2* acos(0))
#define push_back pb
using namespace std;
//int X[]= {0,0,1,-1};
//int Y[]= {-1,1,0,0};
//int X[]= {0,0,1,1,1,-1,-1,-1};
//int Y[]= {-1,1,0,1,-1,0,1,-1};
int num[100];
int get(int pos)
{

    if(pos==1)
    {
        // printf("asd%d %d\n",num['Z'-'A'],'Z'-'A');
        return min(num['O'-'A'],min(num[-'A'+'N'],num[-'A'+'E']));

    }
    if(pos==2)
    {

        //printf("%d %d %d\n",num[-'A'+'O'],num[-'A'+'T'],num[-'A'+'W']);
        return min(num[-'A'+'O'],min(num[-'A'+'T'],num[-'A'+'W']));

    }if(pos==6)
    {

       // printf("%d %d %d\n",num[-'A'+'O'],num[-'A'+'T'],num[-'A'+'W']);
        return min(num[-'A'+'S'],min(num[-'A'+'I'],num[-'A'+'X']));

    }
    if(pos==3)
    {
        int ff =  min(num[-'A'+'T'],min(num[-'A'+'H'],num[-'A'+'R']));
        //printf("zer%d\n",num[-'A'+'T']);
        return min(ff, num['E'-'A']/2);
    }
    if(pos==4)
    {
        int ff =  min(num[-'A'+'F'],min(num[-'A'+'O'],num[-'A'+'U']));
        //printf("zer%d\n",num[-'A'+'T']);
        return min(ff, num['R'-'A']);
    }
    if(pos==5)
    {
        int ff =  min(num[-'A'+'F'],min(num[-'A'+'I'],num[-'A'+'V']));
        //printf("zer%d\n",num[-'A'+'T']);
        return min(ff, num['E'-'A']);
    }
    if(pos==9)
    {
        int ff =  min(num[-'A'+'N']/2,min(num[-'A'+'I'],num[-'A'+'E']));
        //printf("zer%d\n",num[-'A'+'T']);
        return ff;//min(ff, num['R'-'E']);
    }
    if(pos==7)
    {
        int ff =  min(num[-'A'+'S'],min(num[-'A'+'V'],num[-'A'+'N']));
        int ff2 =  num['E'-'A']/2; //min(num[-'A'+'S']/2,min(num[-'A'+'V'],num[-'A'+'N']));
        //printf("zer%d\n",num[-'A'+'T']);
        return min(ff,ff2);//min(ff, num['R'-'E']);
    }
    if(pos==8)
    {
        int ff =  min(num[-'A'+'E'],min(num[-'A'+'I'],num[-'A'+'G']));
        int ff2 =  min(num['H'-'A'],num['T'-'A']); //min(num[-'A'+'S']/2,min(num[-'A'+'V'],num[-'A'+'N']));
        //printf("zer%d\n",num[-'A'+'T']);
        return min(ff,ff2);//min(ff, num['R'-'E']);
    }
    if(pos==0)
    {
        int ff =  min(num['Z'-'A'],min(num['E'-'A'],num['R'-'A']));
       // printf("zer%d %d\n",num['Z'-'A'],'Z'-'A');
        //printf("zer%d\n",num['E'-'A']);
        //printf("zer%d\n",num['R'-'A']);
        //printf("zer%d\n",num['O'-'A']);
        return min(ff, num['O'-'A']);
    }





}
void  del(int pos)
{

    if(pos==1)
    {
        num['O'-'A']--;
        num['N'-'A']--;
        num['E'-'A']--;

       // return min(num['O'-'A'],min(num[-'A'+'N'],num[-'A'+'E']));

    }
    if(pos==2)
    {

        //printf("%d %d %d\n",num[-'A'+'O'],num[-'A'+'T'],num[-'A'+'W']);
       num['T'-'A']--;
        num['W'-'A']--;
        num['O'-'A']--;



    }if(pos==6)
    {
         num['S'-'A']--;
        num['I'-'A']--;
        num['X'-'A']--;

    }
    if(pos==3)
    {
         num['T'-'A']--;
        num['H'-'A']--;
        num['R'-'A']--;
        num['E'-'A']-=2;

    }
    if(pos==4)
    {
        num['F'-'A']--;
        num['O'-'A']--;
        num['U'-'A']--;
        num['R'-'A']--;
           }
    if(pos==5)
    {
        num['F'-'A']--;
        num['I'-'A']--;
        num['V'-'A']--;
        num['E'-'A']--;
    }
    if(pos==9)
    {
            num['N'-'A']--;
        num['I'-'A']--;
        num['N'-'A']--;
        num['E'-'A']--;

    }
    if(pos==7)
    {
        num['S'-'A']--;
        num['E'-'A']--;
        num['V'-'A']--;
        num['E'-'A']--;
        num['N'-'A']--;
       }
    if(pos==8)
    {
           num['E'-'A']--;
        num['I'-'A']--;
        num['G'-'A']--;
        num['H'-'A']--;
        num['T'-'A']--;
      }
    if(pos==0)
    {
       num['Z'-'A']--;
        num['E'-'A']--;
        num['R'-'A']--;
        num['O'-'A']--;

    }


return ;


}
int len;
bool rec(int pos)
{
    if(pos==2)
    {
        for(int i=0;i<26;i++)
        {
            if(num[i])
            {
                printf("%c %d\n",i+'A',num[i]);
                return false;
            }
        }
        return true;
    }
    int cur = get(pos);
    printf("cs%d %d\n",cur,pos);
    bool found =false;;
    if(cur)
    for(int i=cur && found==false;i>=0;i--)
    {
        printf("<>%d %d \n",i,pos);
        del(pos);
        found = rec(pos+1);
        if(found)
        {
            printf("ans ->%d %d\n",0,pos);

            return true;
        }
    }
    else
    rec(pos+1);
    if(found)
    {
        printf("ans ->%d %d\n",0,pos);
        return true;
    }
    return false;


}
int main()
{
    freopen("A-small-attempt3.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    char line[15000];
    for(int cs=1;cs<=t;cs++)
    {
        scanf("%s",line);

    //puts(line);
        int len = strlen(line);
    memset(num,0,sizeof num);

        for(int i=0;i<len;i++)
        {
            num[line[i]-'A']++;
            //printf("%d \n",line[i]-'A' , num[line[i]-'A']);
        }

   // del(0);
    //rec(0);
    int ans[100];
    printf("Case #%d: ",cs);

    ans[0]= get(0);
    for(int i=0;i<ans[0];i++)
    del(0);

    ans[2]= get(2);
    for(int i=0;i<ans[2];i++)
    del(2);
    ans[6]= get(6);
    for(int i=0;i<ans[6];i++)
    del(6);
    ans[4]= get(4);
    for(int i=0;i<ans[4];i++)
    del(4);
    //printf("%d %d %d %d\n",ans[0],ans[7],ans[2],ans[6],ans[4]);

    ans[1]= get(1);
    for(int i=0;i<ans[1];i++)
    del(1);
    ans[8]= get(8);
    for(int i=0;i<ans[8];i++)
    del(8);

    ans[3]= get(3);
    for(int i=0;i<ans[3];i++)
    del(3);
    ans[9]= get(9);
    for(int i=0;i<ans[9];i++)
    del(9);
    ans[7]= get(7);
    for(int i=0;i<ans[7];i++)
    del(7);
    ans[5]= get(5);
    for(int i=0;i<ans[5];i++)
    del(5);
    for(int i=0;i<=9;i++)
    for(int j=0;j<ans[i];j++)
    printf("%d",i);
    //for(int i=0;i<26;i++)
   // if(num[i])printf("%d ",num[i]);
    puts("");








    }



    return 0;
}

