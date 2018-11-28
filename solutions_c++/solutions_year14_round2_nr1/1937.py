#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
using namespace std;
int main(int argc, const char * argv[])
{
   ifstream fin;
   ofstream fout;
   int t;
   fin.open("data.in",std::ofstream::in);
   fout.open("data.out",std::ofstream::out);

   fin>>t;

   for (int step=0;step<t;step++)
   {
        int ans=0,n,len=0;
        int a[100];
        int c[100][100];
        char b[100][100];
        bool pd=false;
        fin>>n;
        for (int i=0;i<n;i++)
        {
            string str;
            fin>>str;
            int k=str.length();
            a[i]=0;
            for (int j=0;j<k;j++)
                if ((j==0)||(str[j]!=str[j-1]))
                    {b[i][a[i]]=str[j];
                    c[i][a[i]]=1;
                    a[i]++;

                    }
                else c[i][a[i]-1]++;
            cout<<str<<" "<<a[i]<<endl;
            if (len==0) len=a[i];
                    else if (len!=a[i]) {
                        pd =true;
                        break;
                    }


        }
        cout<<"len"<<len<<endl;
        if (pd) {
                        fout<<"Case #"<<step+1<<": Fegla Won"<<endl;
                        continue;
        }

        for (int i=0;i<n;i++)
        {for (int j=0;j<len;j++)
            cout<<b[i][j]<<" "<<c[i][j];
        cout<<endl;
        }
        for (int i=1;i<n;i++)
        {

            for (int j=0;j<len;j++)
            if (b[i][j]!=b[i-1][j]) { pd = true;break;}
            if (pd) break;
        }
        if (pd) {
                        fout<<"Case #"<<step+1<<": Fegla Won"<<endl;
                        continue;
        }

        for (int i=0;i<len;i++)
        {
            int m=0;
            for (int j=0;j<n;j++)
                if (c[j][i]>m) m=c[j][i];

            int p=1000;
            cout<<endl<<m<<endl;
            for (int j=1;j<=m;j++)
            {
                int s=0;
                for (int k=0;k<n;k++)
                    s+=abs(c[k][i]-j);
                if (s<p) p=s;
            }
            cout<<p;
            ans+=p;




        }






        fout<<"Case #"<<step+1<<": "<<ans<<endl;
   }
   fin.close();
   fout.close();
}
