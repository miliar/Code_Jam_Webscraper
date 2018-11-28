#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("out.txt");
    int t,n,**h,*miss,r,*hghts,*cnt,diff,c,mi;
    fin>>t;
    for(int tc=0;tc<t;tc++)
    {
        diff=-1;
        fin>>n;
        r=2*n-1;
        hghts=new int[n*n];
        cnt=new int[n*n];
        for(int i=0;i<(n*n);i++)
            cnt[i]=0;
        cout<<r;
        //getch();
        h=new int *[r];
        for(int row=0;row<r;row++)
            h[row]=new int[n];
        miss=new int[n];
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<n;j++)
            {
                fin>>h[i][j];
                cout<<h[i][j];
                c=0;
                for(int df=0;df<diff+1;df++)
                {
                    if(hghts[df]==h[i][j])
                    {
                        c=1;
                        cnt[df]++;
                        break;
                    }
                }
                if(c==0)
                {
                    diff++;
                    hghts[diff]=h[i][j];
                    cnt[diff]++;
                }
            }
        }
        cout<<endl<<"diff hghts:"<<diff+1;
        mi=0;
        for(int i=0;i<diff+1;i++)
        {
            if(cnt[i]%2==1)
            {
                miss[mi]=hghts[i];
                mi++;
            }
        }
        for(int i=0;i<n;i++)
        {
            for(int j=i+1;j<n;j++)
            {
                if(miss[j]<miss[i])
                {
                    miss[i]=miss[i]+miss[j];
                    miss[j]=miss[i]-miss[j];
                    miss[i]=miss[i]-miss[j];
                }
            }
        }
        fout<<"Case #"<<tc+1<<": ";
        for(int i=0;i<n;i++)
            fout<<miss[i]<<" ";
        fout<<endl;
        delete miss;
        delete h;
        delete hghts;
        delete cnt;
    }
}
