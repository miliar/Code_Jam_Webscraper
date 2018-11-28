#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<vector>
using namespace std;
int pmax=1001;
int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        int D;
        cin>>D;
        vector<int> pancake;//number of people with index pancakes
        pancake.reserve(pmax);
        pancake.assign(pmax,0);//initialize to 0
        int mx=0;//max pancake number
        int P[D];//array in question
        for(int i=0;i<D;i++)
        {
            cin>>P[i];
            pancake[P[i]]++;
            mx=max(mx,P[i]);
        }//input

        int minmin=10000;
        int tempmm=0;
        for(int currmx=mx;currmx>0;currmx--)//max number of cake allowed for each person
        {
            tempmm=currmx;
            for(int currcake=currmx+1;currcake<=mx;currcake++)//special minutes calculation: sp
            {
                tempmm+=pancake[currcake]*((currcake-1)/currmx);
            }
            minmin=min(minmin,tempmm);
        }
        printf("Case #%d: %d\n",t,minmin);
    }
}
