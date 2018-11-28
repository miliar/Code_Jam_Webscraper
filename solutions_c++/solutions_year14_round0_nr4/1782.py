#include<iostream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<fstream>
using namespace std;
int TC,N;
double A[1001],B[1001];
double EPS=1e-9;
double inf=1e12;
int Solve_o()
{
    int Ct=0;
    vector<int>used(N,0);
    for(int i=0;i<N;i++)
    {
        int idx=0;
        double mx=0.0;
        bool flag=true;
        for(int j=0;j<N;j++)
            if(!used[j])
        {
            if(B[j]-A[i]>=EPS)
            {
                if(flag)
                {
                    idx=j;
                    mx=B[j];
                    flag=false;
                }
                else
                {
                    if(mx-B[j]>=EPS)
                    {
                        idx=j;
                        mx=B[j];
                    }
                }
            }
        }
        if(flag==false)
        {
            used[idx]=1;
        }
        else
        {

            bool out=true;
            for(int j=0;j<N;j++)
                if(!used[j])
            {
                if(out)
                {
                    out=false;
                    idx=j;
                    mx=B[j];
                }
                else
                {
                    if(mx-B[j]>=EPS)
                    {
                        mx=B[j];
                        idx=j;
                    }
                }
            }
        used[idx]=1;
        Ct++;
        }
    }
    return Ct;
}

int Solve()
{
    sort(B,B+N);
    reverse(B,B+N);
    int Ct=0;
    vector<int>used(N,0);
    for(int i=0;i<N;i++)
    {
        bool flag=true;
        double mx=0.0;
        int idx=0;
        for(int j=0;j<N;j++)
            if(!used[j])
        {

            if(A[j]-B[i]>=EPS)
            {
                if(flag)
                {
                    idx=j;
                    mx=A[j];
                    flag=false;
                }
                else
                {
                    if(mx-A[j]>=EPS)
                    {
                        idx=j;
                        mx=A[j];
                    }
                }
            }
        }
        if(flag==false)
        {
            Ct++;
            used[idx]=1;
        }
        else
        {
            bool out=true;
            for(int j=0;j<N;j++)
                if(!used[j])
            {
                if(out)
                {
                    out=false;
                    idx=j;
                    mx=A[j];
                }
                else
                {
                    if(mx-A[j]>=EPS)
                    {
                        mx=A[j];
                        idx=j;
                    }
                }
            }
            used[idx]=1;

        }
    }
    return Ct;
}
int main()
{
    int Counter=1;
    fstream fin("D-large.in");
    fstream fout("D-large.out");
    fin>>TC;
    while(TC--)
    {
        fin>>N;
        for(int i=0;i<N;i++)
            fin>>A[i];
        for(int i=0;i<N;i++)
            fin>>B[i];
        int o=0,uo=0;
             o=Solve_o();
             uo=Solve();
        fout<<"Case #"<<Counter++<<": "<<uo<<" "<<o<<endl;
    }
return 0;
}
