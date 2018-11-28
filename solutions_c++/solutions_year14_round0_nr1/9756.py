#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    ifstream fin("A-small-attempt1.in");
    ofstream fout("A-small-attempt1.out");
    int t;
    fin>>t;
    for(int k=1;k<=t;++k)
    {
        int n, ta, tb, tc, td, a[4], b[4];
        fin>>n;
        for(int i=0;i<4;++i)
        {
            if(i==n-1)
                fin>>a[0]>>a[1]>>a[2]>>a[3];
            else
                fin>>ta>>tb>>tc>>td;
        }
        fin>>n;
        for(int i=0;i<4;++i)
        {
            if(i==n-1)
                fin>>b[0]>>b[1]>>b[2]>>b[3];
            else
                fin>>ta>>tb>>tc>>td;
        }
        int cnt=0;
        int ans;
        for(int i=0;i<4;++i)
        {
            for(int j=0;j<4;++j)
            {
                if(a[i]==b[j])
                {
                    cnt++;
                    ans=a[i];
                }
            }
        }
        if(cnt==1)fout<<"Case #"<<k<<": "<<ans<<endl;
        else if(cnt==0)fout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
        else fout<<"Case #"<<k<<": Bad magician!"<<endl;
    }
    return 0;
}
