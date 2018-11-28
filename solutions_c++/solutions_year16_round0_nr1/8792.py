#include <bits/stdc++.h>
using namespace std;
int main()
{
    int i,n,j,f,s,d,x,m,t;
    ifstream read("A-large.in");
    read>>t;
    ofstream outfile;
    outfile.open("ofile2.txt");
    //cin>>t;
    for(i=1;i<=t;i++)
    {
        read>>n;
        if(n==0)
            outfile<<"Case #"<<i<<": INSOMNIA\n";
        else
        {
            f=1;
            vector<int> a(10,0);
            j=1;
            s=0;
            while(f)
            {
                m=n*j;
                x=m;
                while(m)
                {
                    d=m%10;
                    if(a[d]==0)
                    {
                        a[d]=1;
                        s+=1;
                    }
                    m/=10;
                }
                if(s==10)
                    f=0;
                j++;
            }
            //outfile << data << endl;
            outfile<<"Case #"<<i<<": "<<x<<endl;
        }
    }
    outfile.close();
    read.close();
    return 0;
}
