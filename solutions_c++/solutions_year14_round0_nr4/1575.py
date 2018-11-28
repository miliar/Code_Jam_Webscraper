#include<fstream>
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

ifstream fin("D-large.in");
ofstream fout("out.txt");

int main()
{
    int t;
    fin>>t;
    for(int test=1;test<=t;test++)
    {
        vector<double> w1,w2;
        int n;
        fin>>n;
        for(int i=0;i<n;i++)
        {
            double p;
            fin>>p;
            w1.push_back(p);
        }
        for(int i=0;i<n;i++)
        {
            double p;
            fin>>p;
            w2.push_back(p);
        }
        sort(w1.begin(),w1.end());
        sort(w2.begin(),w2.end());
        int ans1 = 0, ans2 = 0;

        int bb=n-1;
        for(int i=n-1;i>=0;i--)
        {
            while(bb>=0 && w2[bb]>w1[i])
                bb--;
            if(bb>=0)
            {
                ans2++;
                bb--;
            }
        }

        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(w2[j]>w1[i])
                {
                    w2[j]=0;
                    break;
                }
            }
        }
        for(int i=0;i<n;i++)
        {
            if(w2[i] > 0)
                ans1++;
        }
        fout<<"Case #"<<test<<": ";
        fout<<ans2<<" "<<ans1<<endl;
    }
}
