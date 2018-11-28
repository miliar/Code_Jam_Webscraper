#include<bits/stdc++.h>
using namespace std;
char ar[100000];
int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out","w",stdout);
    int res[200],i,nw;
    //freopen("in.txt","r",stdin);
    int t,cs;
    scanf("%d",&t);
    getchar();
    for(cs=1;cs<=t;cs++)
    {
        memset(res,0,sizeof(res));
        vector<int> vc;
        scanf("%s",&ar);
        int l=strlen(ar);
        //printf("%s\n",ar);
        //cout<<l<<endl;
        for(i=0;i<l;i++)
        {
            res[ar[i]]++;
        }
        if(res['Z']!=0)
        {
            nw=res['Z'];
            for(i=0;i<nw;i++)
            {
                vc.push_back(0);
            }
            res['Z']-=nw; res['E']-=nw; res['R']-=nw; res['O']-=nw;
        }
        if(res['W']!=0)
        {
            nw=res['W'];
            for(i=0;i<nw;i++)
            {
                vc.push_back(2);
            }
            res['T']-=nw; res['W']-=nw; res['O']-=nw;
        }
        if(res['X']!=0)
        {
            nw=res['X'];
            for(i=0;i<nw;i++)
            {
                vc.push_back(6);
            }
            res['S']-=nw; res['I']-=nw; res['X']-=nw;
        }
        if(res['G']!=0)
        {
            nw=res['G'];
            for(i=0;i<nw;i++)
            {
                vc.push_back(8);
            }
            res['E']-=nw; res['I']-=nw; res['G']-=nw; res['H']-=nw; res['T']-=nw;
        }
        if(res['U']!=0)
        {
            nw=res['U'];
            for(i=0;i<nw;i++)
            {
                vc.push_back(4);
            }
            res['F']-=nw; res['O']-=nw; res['U']-=nw; res['R']-=nw;
        }
        if(res['R']!=0)
        {
            nw=res['R'];
            for(i=0;i<nw;i++)
            {
                vc.push_back(3);
            }
            res['T']-=nw; res['H']-=nw; res['R']-=nw; res['E']-=nw; res['E']-=nw;
        }
        if(res['S']!=0)
        {
            nw=res['S'];
            for(i=0;i<nw;i++)
            {
                vc.push_back(7);
            }
            res['S']-=nw; res['E']-=nw; res['V']-=nw; res['E']-=nw; res['N']-=nw;
        }
        if(res['V']!=0)
        {
            nw=res['V'];
            for(i=0;i<nw;i++)
            {
                vc.push_back(5);
            }
            res['F']-=nw; res['I']-=nw; res['V']-=nw; res['E']-=nw;
        }
        if(res['O']!=0)
        {
            nw=res['O'];
            for(i=0;i<nw;i++)
            {
                vc.push_back(1);
            }
            res['O']-=nw; res['N']-=nw; res['E']-=nw;
        }
        if(res['I']!=0)
        {
            nw=res['I'];
            for(i=0;i<nw;i++)
            {
                vc.push_back(9);
            }
            res['N']-=nw; res['I']-=nw; res['N']-=nw; res['E']-=nw;
        }

        int l2=vc.size();
        sort(vc.begin(),vc.end());
        printf("Case #%d: ",cs);
        for(i=0;i<l2;i++)
        {
            printf("%d",vc[i]);
        }
        printf("\n");

    }


    return 0;
}
