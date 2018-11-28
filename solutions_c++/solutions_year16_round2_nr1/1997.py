#include<iostream>
#include<map>
#include<set>
#include<algorithm>
#include<string.h>
using namespace std;

int main()
{

    int i,j,k,x,z,y;
    int test;
    int ans[1200];
    char str[2005];
    cin>>test;
    int ind=0;
    while(test--)
    {
        cin>>str;
        ind++;
        cout<<"Case #"<<ind<<": ";
        int len=strlen(str);
        map<char,int> gg;
        for(i=0;i<len;i++)
        {
                gg[str[i]]++;
        }
        k=0;
        if(gg['Z']>0)
        {

            x=gg['Z'];
            for(i=0;i<x;i++)
            ans[k++]=0;
            gg['Z']=0;
            gg['E']-=x;
            gg['R']-=x;
            gg['O']-=x;
        }
        if(gg['W']>0)
        {

            x=gg['W'];
            for(i=0;i<x;i++)
            ans[k++]=2;
            gg['W']=0;
            gg['T']-=x;
            gg['O']-=x;
        }
        if(gg['U']>0)
        {

            x=gg['U'];
            for(i=0;i<x;i++)
            ans[k++]=4;
            gg['U']=0;
            gg['F']-=x;
            gg['O']-=x;
            gg['R']-=x;

        }
         if(gg['X']>0)
        {

            x=gg['X'];
            for(i=0;i<x;i++)
            ans[k++]=6;
            gg['X']=0;
            gg['S']-=x;
            gg['I']-=x;
        }
        if(gg['G']>0)
        {

            x=gg['G'];
            for(i=0;i<x;i++)
            ans[k++]=8;
            gg['G']=0;
            gg['E']-=x;
            gg['I']-=x;
            gg['H']-=x;
            gg['T']-=x;
        }
        if(gg['O']>0)
        {

            x=gg['O'];
            for(i=0;i<x;i++)
            ans[k++]=1;
            gg['O']=0;
            gg['N']-=x;
            gg['E']-=x;
        }
         if(gg['T']>0)
        {

            x=gg['T'];
            for(i=0;i<x;i++)
            ans[k++]=3;
            gg['T']=0;
            gg['H']-=x;
            gg['R']-=x;
            gg['E']-=2*x;
        }
          if(gg['F']>0)
        {

            x=gg['F'];
            for(i=0;i<x;i++)
            ans[k++]=5;
            gg['F']=0;
            gg['I']-=x;
            gg['V']-=x;
            gg['E']-=x;
        }
        if(gg['V']>0)
        {

            x=gg['V'];
            for(i=0;i<x;i++)
            ans[k++]=7;
            gg['V']=0;
            gg['S']-=x;
            gg['N']-=x;
            gg['E']-=2*x;
        }
        if(gg['N']>0)
        {

            x=gg['N'];
            for(i=0;i<x/2;i++)
            ans[k++]=9;
            gg['N']=0;
            gg['I']-=x;
            gg['E']-=2*x;
        }
        sort(ans,ans+k);
        for(i=0;i<k;i++)
            cout<<ans[i];
        cout<<endl;


    }
}

