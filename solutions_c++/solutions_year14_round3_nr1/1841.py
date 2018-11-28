#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int f(int x, int y, int k)
{  // cout<<x<<" "<<y<<endl;
    if (k>40) return -1;

    if (x==y) return 0;

    if ((x<y)&&(y%2==0))
    {
    int s= f(x,y/2 ,k+1);
    if (s==-1) return -1;
    else return f(x,y/2,k+1)+1;
    }

    if ((x>y)&&(f(x-y,y, k+1)!=-1)) return 0;

    return -1;
}
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
        int p=0,q=0;
        int ans=0;
        string str;
        fin>>str;
      //  cout<<str;
        int i=0,n=str.length();
        while (str[i]!='/')
        {
            p=p*10+str[i]-'0';
            i++;
        }
        i++;
        while (i<n)
        {
            q=q*10+str[i]-'0';
            i++;
        }
        ans = f(p,q,0);

        if (ans!=-1) fout<<"Case #"<<step+1<<": "<<ans<<endl;
                else fout<<"Case #"<<step+1<<": impossible"<<endl;
   }
   fin.close();
   fout.close();
}
