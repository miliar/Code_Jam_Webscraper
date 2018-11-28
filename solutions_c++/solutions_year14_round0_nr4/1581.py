#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
    ifstream in("D-large.in");
    ofstream out("salD.out");

    int t,n,i,j,bien,mentir,h,quemado[1001];
    double naomi[1002],ken[1002];

    in>>t;

    for(i=1;i<=t;i++)
    {
        in>>n;
        for(j=0;j<n;j++)
        {
            in>>naomi[j];
        }
        for(j=0;j<n;j++)
        {
            in>>ken[j];
        }
        sort(naomi,naomi+n);
        sort(ken,ken+n);

        mentir=0;
        bien=0;

        for(j=0;j<=n;j++)
        {
            quemado[j]=1;
        }

        for(j=0;j<n;j++)
        {
          h=0;
          while(h<n)
          {
              if((naomi[j]>ken[h])&&(quemado[h]!=0))
          {
              quemado[h]=0;
              mentir=mentir+1;
              h=n;
          }
         h++;
          }

        }

        for(j=0;j<=n;j++)
        {
            quemado[j]=1;
        }

           for(j=0;j<n;j++)
        {
          h=0;
          while(h<n)
          {
              if((ken[j]>naomi[h])&&(quemado[h]!=0))
          {
              quemado[h]=0;
              bien=bien+1;
              h=n;
          }
         h++;
          }

        }

        out<<"Case #"<<i<<": "<<mentir<<" "<<n-bien<<endl;

    }

    in.close();
    out.close();
    return 0;
}
