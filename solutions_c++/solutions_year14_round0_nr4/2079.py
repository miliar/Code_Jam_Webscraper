//Author: Siddharth Saluja
//Quote: "DIE FOR YOUR AIM"
#include <bits/stdc++.h>

using namespace std;


#define mod 1000000007
//#define DEBUG
#define inf 2147483647
#define ninf -2147483648
#define FOR(i,a,b) for(i=a;i<b;i++)
#define s(a) scanf("%d",&a)
#define lls(a) scanf("%lld",&a)
#define ss(a) scanf("%s",a)
#define p(a) printf("%d",a)
#define llp(a) printf("%lld",a)
#define sp(a) printf("%s",a)
#define cp(a) printf("%c",a)
#define nline printf("\n")
#define space printf(" ")
#define fs(a) fscanf(fp,"%d",&a)
#define flls(a) fscanf(fp,"%lld",&a)
#define fss(a) fscanf(fp,"%s",a)
#define fp(a) fprintf(fo,"%d",a)
#define fllp(a) fprintf(fo,"%lld",a)
#define fsp(a) fprintf(fo,"%s",a)
#define fcp(a) fprintf(fo,"%c",a)
#define fnline fprintf(fo,"\n")
#define fspace fprintf(fo," ")
#define ll long long


int main()
{
#ifdef DEBUG
    cout<<"Debugging\n";
#endif
//ios::sync_with_stdio(false);
FILE *fp,*fo;
fp=fopen("input.txt","r");
fo=fopen("output.txt","w");

int t,k=0,n,ans1=0,ans2=0,i,j,npos,kpos,maxpos;
fs(t);
while(t--)
{
    ans1=0,ans2=0;
    k++;
    fprintf(fo,"Case #%d: ",k);
    fs(n);
    ans2=n;
    vector<pair<double,bool> > noami,ken;
    double temp,minin,minik,maxk;
    for(i=0;i<n;i++)
    {
        fscanf(fp,"%lf",&temp);
        noami.push_back(make_pair(temp,false));
    }
    for(i=0;i<n;i++)
    {
        fscanf(fp,"%lf",&temp);
        ken.push_back(make_pair(temp,false));
    }
    sort(noami.begin(),noami.end());
    sort(ken.begin(),ken.end());
    for(i=0;i<n;i++)
    {
        temp=noami[i].first;
        for(j=0;j<n;j++)
        {
            if(ken[j].first>temp && ken[j].second==false)
            {
                ken[j].second=true;
                ans2--;
                break;
            }
        }
    }
    for(i=0;i<n;i++)
    {
        noami[i].second=ken[i].second=false;
    }
    while(1)
    {
        minik=1e9,minin=1e9,maxk=0;
        for(i=0;i<n;i++)
        {
            if(noami[i].second==false && minin>noami[i].first)
            {
                minin=noami[i].first;
                npos=i;
            }
        }
        for(i=0;i<n;i++)
        {
            if(ken[i].second==false && minik>ken[i].first)
            {
                minik=ken[i].first;
                kpos=i;
            }
        }
        for(i=0;i<n;i++)
        {
            if(ken[i].second==false && maxk<ken[i].first)
            {
                maxk=ken[i].first;
                maxpos=i;
            }
        }
        if(minin==1e9 && minik==1e9)
            break;
        if(minin>minik)
        {
            ans1++;
            noami[npos].second=true;
            ken[kpos].second=true;
        }
        else if(minin<minik)
        {
            noami[npos].second=true;
            ken[maxpos].second=true;
        }
    }
    fprintf(fo,"%d %d\n",ans1,ans2);
}
return 0;
}
