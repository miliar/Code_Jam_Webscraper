#include <bits/stdc++.h>

#define mod 1000000007
#define inf 1000000000000
#define root2 1.41421
#define root3 1.73205
#define pi 3.14159
#define MAX 100001
#define ll long long int
#define PII pair<int, int>
#define f first
#define s second

using namespace std;

int alphacnt[26], digitcnt[10], n;
string S;
int main()
{
    ifstream in("A-large(2).in");
    ofstream out("output.txt");
    int i, t, x, j, k=1;
    in>>t;
    while(k<=t)
    {
        out<<"Case #"<<k<<": ";
        in>>S;
        n=S.size();
        for(i=0;i<26;i++)
            alphacnt[i]=0;
        for(i=0;i<10;i++)
            digitcnt[i]=0;
        for(i=0;i<n;i++)
        {
            alphacnt[S[i]-65]++;
        }
        x=alphacnt['Z'-65];
        digitcnt[0]=x;
        alphacnt['Z'-65]=0;
        alphacnt['E'-65]-=x;
        alphacnt['R'-65]-=x;
        alphacnt['O'-65]-=x;
        x=alphacnt['W'-65];
        digitcnt[2]=x;
        alphacnt['W'-65]=0;
        alphacnt['T'-65]-=x;
        alphacnt['O'-65]-=x;
        x=alphacnt['U'-65];
        digitcnt[4]=x;
        alphacnt['U'-65]=0;
        alphacnt['F'-65]-=x;
        alphacnt['O'-65]-=x;
        alphacnt['R'-65]-=x;
        //6
        x=alphacnt['X'-65];
        digitcnt[6]=x;
        alphacnt['X'-65]=0;
        alphacnt['S'-65]-=x;
        alphacnt['I'-65]-=x;
        //8
        x=alphacnt['G'-65];
        digitcnt[8]=x;
        alphacnt['G'-65]=0;
        alphacnt['E'-65]-=x;
        alphacnt['I'-65]-=x;
        alphacnt['H'-65]-=x;
        alphacnt['T'-65]-=x;
        //1
        x=alphacnt['O'-65];
        digitcnt[1]=x;
        alphacnt['O'-65]=0;
        alphacnt['N'-65]-=x;
        alphacnt['E'-65]-=x;
        //3
        x=alphacnt['H'-65];
        digitcnt[3]=x;
        alphacnt['H'-65]=0;
        alphacnt['T'-65]-=x;
        alphacnt['R'-65]-=x;
        alphacnt['E'-65]-=2*x;
        //5
        x=alphacnt['F'-65];
        digitcnt[5]=x;
        alphacnt['F'-65]=0;
        alphacnt['I'-65]-=x;
        alphacnt['V'-65]-=x;
        alphacnt['E'-65]-=x;
        //7
        x=alphacnt['S'-65];
        digitcnt[7]=x;
        alphacnt['S'-65]=0;
        alphacnt['V'-65]-=x;
        alphacnt['E'-65]-=2*x;
        alphacnt['N'-65]-=x;

        //9
        x=alphacnt['I'-65];
        digitcnt[9]=x;
        alphacnt['I'-65]=0;
        alphacnt['N'-65]-=2*x;
        alphacnt['E'-65]-=x;

        for(i=0;i<10;i++)
            for(j=0;j<digitcnt[i];j++)
                out<<i;
        out<<endl;
        k++;
    }
}
