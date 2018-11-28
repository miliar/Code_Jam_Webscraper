#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<string>
#include<cstring>
#include <cmath>
#include<algorithm>
#include<stack>
using namespace std;

int T;
int N;
double na[1010];
double ke[1010];
int sn;
int sk;
int sn2;
int sk2;
void solve()
{
    sn=0;
    sk=0;
    sn2=0;
    sk2=0;
    sort(na,na+N);
    sort(ke,ke+N);
//    for(int i=0;i<N;i++)
//        cout<<na[i]<<endl;
    //War
    int st=0;
    for(int i=0;i<N;i++)
    {
        for(int j=st;j<N;j++)
        {
            if(ke[j]>na[i])
            {
                sk++;
                st=j+1;
                break;
            }
        }
    }
   // cout<<sk<<"++"<<endl;
    sn=N-sk;
    st=0;
    //D-War
    for(int i=0;i<N;i++)//Ke
    {
        for(int j=st;j<N;j++)//Na
        {
            if(na[j]>ke[i])
            {
                sn2++;
                st=j+1;
                break;
            }
        }
    }

}
int main()
{
    freopen("D-large.in","r",stdin);
   // freopen("input.txt","r",stdin);
    freopen("d-large.out","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        scanf("%d",&N);
        for(int i=0;i<N;i++) scanf("%lf",&na[i]);
        for(int i=0;i<N;i++) scanf("%lf",&ke[i]);
        solve();
        printf("Case #%d: %d %d\n",i,sn2,sn);
    }
    return 0;
}
