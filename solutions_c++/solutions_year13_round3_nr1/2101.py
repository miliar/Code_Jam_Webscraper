#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std ;

char str[1000005];
int check[1000005];
int N;
int cnt ;
int len ;
struct aaa{ int pp , answer ; };

vector<aaa> dpV[100005];

bool checkFROMEND(int f , int e)
{
    if(f <0 || e <0 || f > len - 1 ||e > len -1) return false ;
    if(e - f +1 < N ) return false ;
    if(e < f) return false ;

    return true ;
}
int f(int ffrom , int eend) //1,6
{
    int Ans1 ;
    int Ans2 ;
    int Ans3 ;
    int AA;
    int BB;
    bool ffind ;

    AA = ffrom ;
    BB = eend - 1;
    ffind = false ;
    if(checkFROMEND(AA ,BB) == false)
    {
        Ans1 = 0 ;
        goto END_1;
    }
    for(int i = 0 ; i < dpV[AA].size() ; i++)
    {
        if(dpV[AA][i].pp == BB)
        {
            ffind = true ;
            Ans1 =dpV[AA][i].answer ;
            break;
        }
    }
    if(!ffind)
    {
        Ans1 = f(AA,BB);
    }
    END_1:

    AA = ffrom +1;
    BB = eend - 1;
    ffind = false ;
    if(checkFROMEND(AA ,BB) == false)
    {
        Ans2 = 0 ;
        goto END_2;
    }
    for(int i = 0 ; i < dpV[AA].size() ; i++)
    {
        if(dpV[AA][i].pp == BB)
        {
            ffind = true ;
            Ans2 =dpV[AA][i].answer ;
            break;
        }
    }
    if(!ffind)
    {
        Ans2 = f(AA,BB);
    }
    END_2:

    AA = ffrom +1;
    BB = eend ;
    ffind = false ;
    if(checkFROMEND(AA ,BB) == false)
    {
        Ans3 = 0 ;
        goto END_3;
    }
    for(int i = 0 ; i < dpV[AA].size() ; i++)
    {
        if(dpV[AA][i].pp == BB)
        {
            ffind = true ;
            Ans3 =dpV[AA][i].answer ;
            break;
        }
    }
    if(!ffind)
    {
        Ans3 = f(AA,BB);
    }
    END_3:

    if(Ans3 +Ans2 + Ans1 >= 1)
    {
        aaa tmp ;
        tmp.pp = eend ;
        tmp.answer = 1 ;
        dpV[ffrom].push_back(tmp);
        return 1 ;
    }
    else
    {
        aaa tmp ;
        tmp.pp = eend ;
        tmp.answer = 0 ;
        dpV[ffrom].push_back(tmp);
        return 0 ;
    }
}

int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);

    int cases;
    scanf("%d",&cases);

    for(int c = 1 ; c <= cases ; c++)
    {
        scanf("%s%d",str,&N);
        len = strlen(str);

        for(int i = 0 ; i <= len ; i++)
        dpV[i].clear();

        for(int i = 0 ; i <len ; i++)
        if(str[i] == 'a' || str[i] =='e' || str[i] =='i' || str[i] =='o' || str[i] =='u') check[i] = 0 ;
        else check[i] = 1 ;

        for(int i = 0 ; i < len ; i++)
        {
            int ccnt = 0 ;
            if(i+ N - 1 >= len) continue ;

            for(int j = i ; j <= i+ N - 1 ; j++)
            {
                ccnt += check[j];
            }
            aaa tmp ;
            tmp.pp = i+N-1 ;

            if(ccnt == N )
            {
                tmp.answer = 1 ;
                dpV[i].push_back(tmp);
            }
            else
            {
                tmp.answer = 0 ;
                dpV[i].push_back(tmp);
            }
        }

        cnt = 0 ;
        f(0,len-1);

        for(int i = 0 ; i < len ; i++)
        {
            for(int j = 0 ; j < dpV[i].size() ; j++)
            {
                cnt += (dpV[i][j].answer);
            }
        }

        printf("Case #%d: %d\n",c,cnt);
    }

    return 0 ;
}
