#include <iostream>
#include <fstream>
#include <iomanip>
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
        int ans=0;
        int a,b,k;
        fin>>a>>b>>k;
        for (int i=0;i<a;i++)
            for (int j=0;j<b;j++)
                {
                    int s1=i,s2=j,s=0,p=1;

                    while ((s1+s2)!=0)
                    {
                        if ((s1%2==1)and(s2%2==1)) s+=p;
                        p*=2;
                        s1=s1/2;
                        s2=s2/2;

                    }
                  //  cout<<s<<endl;
                    if (s<k)
                    {ans++;
                      //  cout<<i<<" "<<j<<endl;
                    }
                }
        fout<<"Case #"<<step+1<<": "<<ans<<endl;
   }
   fin.close();
   fout.close();
}
