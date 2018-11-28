#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>


using namespace std;

#define mp make_pair
#define fr first
#define sc second
#define pb push_back
#define LL long long
#define forn(a,b) for(LL a=0; a<b; a++)
#define FOR1(a,b) for(LL a=1; a<=b;a++)
#define file freopen("A-small-attempt1.in","r",stdin)

int a[101][101];
int main()
{
    file;
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    forn(l,t)
    {
        int n;
        cin>>n;
        for(int i=0; i<=100; i++)
            for(int j=0; j<=100; j++)
                a[i][j]=0;
        bool ok=true;
        forn(k,n)
        {
            string s;
            cin>>s;
            int kil=1;
            int len=1;
            a[k][len]=1;
            char ch[101];
            for(int i=1; i<s.size(); i++)
            {
                if(s[i]==s[i-1]) kil++;else
                {
                    a[k][len]=kil; kil=1;
                     if(k==0)
                        ch[len]=s[i-1];
                     if(k!=0)
                         if(ch[len]!=s[i-1]) ok=false;
                    len++;

                }
            }
            if(k==0)
                ch[len]=s[s.size()-1];
            if(k!=0)
                if(ch[len]!=s[s.size()-1]) ok=false;
            a[k][len]=kil;
            a[k][0]=len;

            //cout<<len<<endl;
        }

        for(int k=1; k<n; k++)
            if(a[k][0]!=a[k-1][0]) ok=false;

        for(int k=1; k<n; k++)
            for(int j=1; j<=a[k][0]; j++)
                if((a[0][j]==0 && a[k][j]==0) || (a[0][j]!=0 && a[k][j]!=0)) ;
                    else ok=false;

        cout<<"Case #"<<l+1<<": ";
        if(!ok){ cout<<"Fegla Won"<<'\n'; continue;}

        int d[101];
        for(int i=1; i<=a[0][0]; i++) d[i]=0;

        for(int k=0; k<n; k++)
            for(int j=1; j<=a[k][0]; j++)
                d[j]+=a[k][j];

     //  for(int i=1; i<=a[0][0]; i++)
     //       cout<<d[i]<< ' ';
     //   cout<<endl;

        for(int i=1; i<=a[0][0]; i++)
        {
            double ost =  double(d[i])/ double(n) - d[i]/n;
            d[i]=d[i]/n;
            if(ost>0.5) d[i]++;
            //cout<<d[i]<<' ';
        }



        int ans=0;

        for(int i=0; i<n; i++)
            for(int j=1; j<=a[i][0]; j++)
                ans+=abs(d[j]-a[i][j]);


        cout<<ans<<'\n';


    }

}
