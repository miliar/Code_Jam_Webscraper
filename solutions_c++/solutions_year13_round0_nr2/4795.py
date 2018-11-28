#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
long long n,m,k,l,t;
int  a[101][101];
int red[101],stu[101],che;
bool tru;
bool check (int x)
{
    for (int i=0; i<n; i++) red[i]=0;
    for(int j=0; j<m; j++) stu[j]=0;
    for (int i=0; i<n; i++)
        for(int j=0; j<m; j++)
        if (a[i][j]==x) {red[i]=1; stu[j]=1;}
    for (int i=0; i<n; i++)
        if (red[i]==1)
        {
            che=1;
            for (int j=0; j<m; j++)
                if (a[i][j]>x) che=0;
            red[i]+=che;
        }
    for (int j=0; j<m; j++)
        if (stu[j]==1)
        {
            che=1;
            for (int i=0; i<n; i++)
                if (a[i][j]>x) che=0;
            stu[j]+=che;
        }
    for (int i=0; i<n; i++)
        for(int j=0; j<m; j++)
        if (a[i][j]==x)
            if (red[i]==1 && stu[j]==1) return 0;
    return 1;
}
int main()
{
    ofstream fout ("test.out");
    ifstream fin ("test.in");
    fin>>t;
    for (int o=0; o<t; o++)
    {
        fin>>n>>m;

        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                fin>>a[i][j];
        if (n==1 || m==1) {fout<<"Case #"<<o+1<<": YES"<<endl; continue;}
        tru=1;
        for (int i=1; i<101; i++)
            if (check(i)==0) {tru=0; break;}

        if (tru) fout<<"Case #"<<o+1<<": YES"<<endl;
        else fout<<"Case #"<<o+1<<": NO"<<endl;
    }
    return 0;
}
