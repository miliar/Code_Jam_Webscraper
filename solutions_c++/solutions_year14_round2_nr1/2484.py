#include <iostream>
#include <cstdio>

using namespace std;
char buff[105];

int ab(int x)
{
    if(x<0) return -x; else return x;
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    gets(buff);
    sscanf(buff,"%d",&t);
    for(int qwerty=1;qwerty<=t;qwerty++)
    {
        bool ok=true;
        gets(buff);
        int n;
        sscanf(buff,"%d",&n);
        int d[100][100];
        gets(buff);
        char a[101];
        int l=1;
        int i=1;
        a[0]=buff[0];
        d[0][0]=1;
        while(buff[i]>='a' && buff[i]<='z')
        {
            if(buff[i]==a[l-1]) {d[0][l-1]++; } else
                {
                    a[l]=buff[i];
                    d[0][l++]=1;
                }
            i++;
        }
        int m=l;
        for(int q=1;q<n;q++)
        {
            gets(buff);
            if(a[0]!=buff[0]){ok=false; break;}
            i=1;
            l=1;
            d[q][0]=1;

            while(buff[i]>='a' && buff[i]<='z')
            {
                if(buff[i]==a[l-1]) {d[q][l-1]++; } else
                {
                    if(a[l]!=buff[i]) {ok=false; break;}
                    d[q][l++]=1;
                }
                i++;
            }
            if(l!=m) {ok=false;}
            if(!ok) break;
        }
        if(!ok) {cout << "Case #"<<qwerty<<": Fegla Won"<<endl;  continue;}

        int res=0;
        for(int j=0;j<m;j++)
        {
            do
            {
                ok=false;
                for(int i=0;i<n-1;i++)
                    if(d[i][j]>d[i+1][j]) {ok=true; int t=d[i][j]; d[i][j]=d[i+1][j]; d[i+1][j]=t;}
            }while(ok);
            int mid=d[n/2][j];
            for(int i=0;i<n;i++)
                res+=ab(d[i][j]-mid);
        }
        cout << "Case #"<<qwerty<<": "<<res<<endl;
    }
    return 0;
}
