#include <cstdio>
#include <string>
using namespace std;
FILE *f,*g;


int key(char c)
{
    if (c=='i') return 2;
    if (c=='j') return 3;
    if (c=='k') return 4;
}

int produs(int x,int y)
{
    int inv,inv2;
    if (x==1)
        return y;
    if (x==-1)
        return -y;
    if (x==2 || x==-2)
    {
        if (x==-2) inv=-1; else inv=1;
        if (y<0) {inv2 = -1; y=-y;} else inv2=1;

        if (y==1) return 2*inv*inv2;
        if (y==2) return -1*inv*inv2;
        if (y==3) return 4*inv*inv2;
        if (y==4) return -3*inv*inv2;
    }
    if (x==3 || x==-3)
    {
        if (x==-3) inv=-1; else inv=1;
        if (y<0) {inv2 = -1; y=-y;} else inv2=1;

        if (y==1) return 3*inv*inv2;
        if (y==2) return -4*inv*inv2;
        if (y==3) return -1*inv*inv2;
        if (y==4) return 2*inv*inv2;
    }
    if (x==4 || x==-4)
    {
        if (x==-4) inv=-1; else inv=1;
        if (y<0) {inv2 = -1; y=-y;} else inv2=1;

        if (y==1) return 4*inv*inv2;
        if (y==2) return 3*inv*inv2;
        if (y==3) return -2*inv*inv2;
        if (y==4) return -1*inv*inv2;
    }
}

int main()
{
    f=fopen("dijkstra.in","r");
    g=fopen("dijkstra.out","w");


    int t,q,l,x,i,j,nr1,nr2,nr3,k;
    bool fata[100100];
    bool spate[100100];
    bool ok;
    char a[100100];
    string ax,s;

    fscanf(f,"%d",&t);


    for (q=1;q<=t;q++)
    {
        fscanf(f,"%d%d",&l,&x);
        fscanf(f,"%s",a);
        ax = a;
        s= "";

        for (i=1;i<=x;i++) s+=ax;

        ok = false;
        nr1 = 1; nr2=1; nr3=1;

        for (i=0;i<=s.size();i++)
            fata[i] = spate[i] = false;

        for (i=0;i<=s.size();i++)
        {
            nr1 = produs(nr1,key(s[i]));
            if (nr1 == 2) fata[i] = true;
        }

        for (i=s.size()-1;i>=0;i--)
        {
            nr3 = produs(key(s[i]),nr3);
            if (nr3 == 4) spate[i] = true;
        }

        for (i=0;i<s.size();i++)
        {
            if (fata[i])
            {
                nr2 = 1;
                for (j=i+1;j<s.size();j++)
                {
                    nr2 = produs(nr2,key(s[j]));
                    if (nr2 == 3 && spate[j+1] == true)
                    {
                        ok = true;
                    }
                }
            }
        }

        printf("%d\n",q);

        if (ok)
            fprintf(g,"Case #%d: YES\n",q);
        else
             fprintf(g,"Case #%d: NO\n",q);
    }


    return 0;
}
