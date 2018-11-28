#include<iostream>
#include<fstream>
using namespace std;

int max_rvp(int *a,int n)
{
    int ans=0;

    for(int i=0;i<n;i++)
        if(a[ans]<a[i])
            ans=i;
    return ans;

}

int total(int *a,int n)
{
    int ans=0;

    for(int i=0;i<n;i++)
        ans+=a[i];
    return ans;
}

int main()
{
    int T;
    ifstream infile("A-small-attempt0.in");
    ofstream outfile("ans.txt");
    infile>>T;
    for(int i=0;i<T;i++)
    {
        outfile<<"Case #"<<(i+1)<<": ";
        int N;
        infile>>N;
        int p[1500];
        for(int j=0;j<N;j++)
            infile>>p[j];
        int t;

        if(N%2==0)
            t=total(p,N);
        else
            t=total(p,N)-N;
        for(int k=0;k<t;k++)
        {
            int ans=max_rvp(p,N);
            p[ans]--;
            char w='A'+ans;
            outfile<<w;
            if((k+1)%2==0)
                outfile<<" ";
        }
        if(N%2!=0)
        {

            outfile<<"A ";
            for(int i=1;i<N;i++)
            {
                char s='A'+i;
                outfile<<s;
                if(i%2==0)
                    outfile<<" ";
            }

        }
        outfile<<endl;
    }

    return 0;
}
