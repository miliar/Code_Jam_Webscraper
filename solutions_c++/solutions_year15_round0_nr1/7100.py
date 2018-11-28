#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t, i, st,c, fr,smax,j;
    string in;
    scanf("%d", &t);
    for(i = 1; i<= t; i++)
    {
        fr=0; st=0;
        scanf("%d",&smax);
        cin>>in;
        for(j=0;j<=smax;j++)
        {
            c=in[j]-'0';
            if(st>=smax) break;
            if(st<j) {fr++; st++;}
            st+=c;
        }
        cout<<"Case #"<<i<<": "<<fr<<'\n';
    }
    return 0;
}
