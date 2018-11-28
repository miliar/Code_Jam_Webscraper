#include <iostream>
#include <fstream>

using namespace std;

ifstream in("B-large.in");
ofstream out("B-large.out");

int main()
{
    int t;
    in>>t;
    for(int i=0;i<t;i++)
    {
        int d;
        in>>d;
        int a[d];
        for(int j=0;j<d;j++)in>>a[j];
        int mini=1001;
        for(int j=1;j<=1000;j++)
        {
            int maxi=0;
            int sm=0;
            for(int k=0;k<d;k++)
            {
                if(a[k]%j==0)
                {
                    sm+=a[k]/j-1;
                    if(maxi<j)maxi=j;
                }
                else
                {
                    sm+=a[k]/j;
                    int m;
                    if(a[k]%(a[k]/j+1)==0)m=a[k]/(a[k]/j+1)+1;
                    else m=a[k]/(a[k]/j+1)+1;
                    if(maxi<m)maxi=m;
                }
            }
            if(maxi+sm<mini)mini=maxi+sm;
        }
        out<<"Case #"<<i+1<<": "<<mini<<endl;
    }
    return 0;
}
