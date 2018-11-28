#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>

using namespace std;

char s[101];


int compare(const void *a,const void *b)
{
     return *(int*)b-*(int*)a;
}

int main()
{
    int a,b,x,p,g;
    freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);
	ios :: sync_with_stdio(false);
    int t,n;
    scanf("%d",&t);
    for (int k=1;k<=t;k++)
    {
        scanf("%s",s);
    //    cout<<s<<endl;
        int a=0;
        int i=0;
        while (s[i]!='/')
        {
            a=a*10+(s[i]-48);
            i++;
        }
        i++;
        b=0;
        while (i<strlen(s))
        {
            b=b*10+(s[i]-48);
            i++;
        }
     //   cout<<a<<endl;
      //  cout<<b<<endl;
        cout<<"Case #"<<k<<": ";
        int x=a;int y=b;
        while (y>0)
        {
            g=x%y;
            x=y;
            y=g;
        }
        g=x;
     //   cout<<"g:"<<g<<endl;
     //   cout<<g<<endl;
        a=a/g;
        b=b/g;
        x=b;
        p=0;
        while (x%2==0)
        {
            x=x/2;
            p++;
        }
        int pppp=0;
        int pp=1;
     //   cout<<x<<endl;
        while (pp<=a)
        {
            pp=pp*2;
            pppp++;
        }
        pppp--;
        if (x!=1)
        {
            cout<<"impossible"<<endl;
        }
        else
        {
            cout<<p-pppp<<endl;
        }
    }

    return 0;
}
