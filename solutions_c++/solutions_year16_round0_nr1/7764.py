/* بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ */
/* رَّبِّ زِدْنِى عِلْمًا */



#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <iostream>
#include <string>

using namespace std;

#define OUTPUT freopen("myfile.txt","w",stdout);
#define INPUT freopen("A-large.in","r",stdin);
#define DEBUG(a) cout<<a<<endl;
#define PI acos(-1.0)
#define MAX 100005
#define MOD 1000000007
#define EPS 1e-9
#define BIGGER(a,b) (a>=b ? a : b)
#define SMALLER(a,b) (a<=b ? a : b)
#define getInt(a) scanf("%d",&a);
#define getLong(a) scanf("%lld",&a);
#define pb push_back

int cal(long long int num);

int cal(long long int num)
{
    long long int multy=1;
    int array[20]={0,};
    long long int temp;
    int i;

    while(1)
    {
        temp=multy*num;

        while(1)
        {
            if(temp==0)
            {
                break;
            }

            array[temp%10]=1;
            temp/=10;
        }

        int cnt=0;

        for( i =0 ;i <10;i++)
        {
            if(array[i]==1)
                cnt++;
        }
//printf("%d\n",cnt);
        if(cnt==10)
            return multy;

        multy++;

        if(multy>100)
            return -1;
    }
}


int main()
{
    int T,tp=1;
    long long int N,multy;


    //INPUT
    //OUTPUT

    getInt(T)


    while(T--)
    {
        getLong(N)

        multy=cal(N);

        if(multy==-1)
            printf("Case #%d: INSOMNIA\n",tp);

        else
            printf("Case #%d: %lld\n",tp,multy*N);

        tp++;

    }

    return 0;
}


