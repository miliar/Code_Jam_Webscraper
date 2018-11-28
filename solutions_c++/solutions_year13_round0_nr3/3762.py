#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<math.h>

using namespace std;

bool pal(long long int x)
{
        stringstream ss;
        ss<<x;
        string s=ss.str();
        int i,j;
        for(i=0,j=s.length()-1;i<j;i++,j--)
            if(s[i]!=s[j])
                return false;
        return true;
}
int main()
 {
     fstream fin,fout;
     fin.open("c.in");
     fout.open("c.txt");
     int t;
     fin>>t;

     for(int z=1;z<=t &&!fin.eof();z++)
        {
            long long int a,b,ans;
            fin>>a>>b;
            a=ceil(sqrt(a));
            cout<<a;
            ans=0;
            for(long long int i=a*a;i<=b;i=(++a)*a)
                if(pal(i) && pal(a))
                    ans++;

        string ns;
        ns="Case #";
        stringstream ss;
        ss<<z;
        ns+=ss.str();
        ns+=": ";

        fout<<ns;
        fout<<ans;
        fout<<endl;
        }
     fin.close();
     fout.close();
     return 0;
 }
