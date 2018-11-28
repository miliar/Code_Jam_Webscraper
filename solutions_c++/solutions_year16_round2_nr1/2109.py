#include <bits/stdc++.h>

#define ll long long int

const int mod=1000000007;

using namespace std;

int main()
{
    int t,i,j,k,m,n,p,s;
    ll a,b,c,d,g,h;

    FILE *f1,*f2;
    f1=fopen("Input.txt","r");
    f2=fopen("Output.txt","w");

    fscanf (f1,"%d",&t);
    fgetc(f1);
    for (int z=1;z<=t;++z)
    {
        char arr[2050];
        fscanf (f1,"%s",arr);
        int A[26]={0};
        for (i=0;arr[i]!='\0';++i)
            A[arr[i]-65]++;
        int cnt[10]={0};
        cnt[0]=A[25];
        A[4]-=A[25];
        A['R'-65]-=A[25];
        A['O'-65]-=A[25];
        A[25]=0;

        cnt[2]=A['W'-65];
        A['T'-65]-=cnt[2];
        A['O'-65]-=cnt[2];
        A['W'-65]=0;

        cnt[4]=A['U'-65];
        A['F'-65]-=cnt[4];
        A['O'-65]-=cnt[4];
        A['R'-65]-=cnt[4];
        A['U'-65]=0;

        cnt[6]=A['X'-65];
        A['S'-65]-=cnt[6];
        A['I'-65]-=cnt[6];
        A['X'-65]=0;

        cnt[8]=A['G'-65];
        A['E'-65]-=cnt[8];
        A['I'-65]-=cnt[8];
        A['H'-65]-=cnt[8];
        A['T'-65]-=cnt[8];
        A['G'-65]=0;

        cnt[1]=A['O'-65];
        A['N'-65]-=cnt[1];
        A['E'-65]-=cnt[1];
        A['O'-65]=0;

        cnt[3]=A['H'-65];
        A['T'-65]-=cnt[3];
        A['R'-65]-=cnt[3];
        A['E'-65]-=(2*cnt[3]);
        A['H'-65]=0;

        cnt[7]=A['S'-65];
        A['E'-65]-=(2*cnt[7]);
        A['V'-65]-=cnt[7];
        A['N'-65]-=cnt[7];

        cnt[5]=A['V'-65];
        A['I'-65]-=cnt[5];
        A['E'-65]-=cnt[5];

        cnt[9]=A['I'-65];

        fprintf (f2,"Case #%d: ",z);
        for (i=0;i<10;++i)
            for (j=0;j<cnt[i];++j)
                fprintf (f2,"%d",i);
        fprintf (f2,"\n");
    }

    fclose(f1);
    fclose(f2);
    return 0;
}
