#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream ifs("A-large.in");
    int t;
    ifs>>t;
    int q=1;
    while (t--)
    {
        ofstream ofs;
        ofs.open("test.txt", std::ios_base::app);
        int n,i=1;
        ifs>>n;
        if (n==0) {ofs<<"Case #"<<q<<": "<<"INSOMNIA"<<endl;q++;continue;}
        set<int> s;
        int nn=n;
        while (nn)
        {
            int c=nn%10;
            s.insert(c);
            nn=nn/10;
        }
        int x;
        while (s.size()<10)
        {
            x=n*i;
            int xx=x;
            while (xx)
            {
                int w=xx%10;
                s.insert(w);
                xx=xx/10;
            }
            i++;

        }
          ofs << "Case #"<<q<<": "<<x<<endl;
          q++;


       // cout<<"Case #"<<q<<": "<<x<<endl;
    }
    return 0;
}
