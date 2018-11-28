#include <iostream>
#include <fstream>
#include <cstring>
#include <algorithm>
#define sol "Case #"

using namespace std;

int prod[][3]={{-1,'k',-(int)'j'},{-(int)'k',-1,'i'},{'j',-(int)'i',-1}};

int product(int a,int b)
{
    if(a<0) return -product(-a,b);
    if(b<0) return -product(a,-b);
    if(a==1) return b;
    if(b==1) return a;
    return prod[a-'i'][b-'i'];
}
char str[10010],a[10010];bool a1,a2,a3,ans[10010];
int main()
{
    int i,j,t,k,l,x,cur=1;
    fstream fin,fout;
    fin.open("A.in",ios::in);
    fin>>t;
    for(i=0;i<t;i++)
    {
        memset(a,0,sizeof(a));
        memset(str,0,sizeof(str));
        fin>>l>>x;
        fin>>a;
        a1=a2=a3=0;
        for(j=0;j<x;j++)
            for(k=0;k<l;k++)
                str[j*l+k]=a[k];
        cur=1;ans[i]=0;
        for(j=0;j<l*x;)
        {
            while(cur!='i' && j<l*x)
            {cur=product(cur,str[j]);j++;}
            if(cur=='i') a1=1;
            cur=1;
            while(cur!='j' && j<l*x)
            {cur=product(cur,str[j]);j++;}
            if(cur=='j') a2=1;
            cur=1;
            while(j<l*x)
            {cur=product(cur,str[j]);j++;}
            if(cur=='k') a3=1;
        }
        if(a1 && a2 && a3) ans[i]=1;
    }
    fout.open("solution.out",ios::out);
    for(i=0;i<t;i++)
        {
            fout<<sol<<i+1<<": ";
            if(ans[i]) fout<<"YES";
            else fout<<"NO";
            fout<<'\n';
        }
    fout.close();
    return 0;
}
