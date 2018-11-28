#include<iostream>
#include<string>
#include<fstream>
using namespace std;
int main()
{
    ifstream ifile("B-large.in");
    ofstream ofile("output.txt");
    int t;
    ifile>>t;
    for(int i=1;i<=t;++i)
    {
        int m,n;
        ifile>>n>>m;
        int arr[n][m];
        int flagg=0;
        for(int j=0;j<n;++j)
            for(int k=0;k<m;++k)
                ifile>>arr[j][k];
        for(int j=0;j<n;++j)
        {
            for(int k=0;k<m;++k)
            {
                int num = arr[j][k];
                int flag=0;
                for(int x=0;x<m;++x)
                {
                    if(x!=k && arr[j][x]>num)
                    {
                        flag++;
                        break;
                    }
                }
                for(int x=0;x<n;++x)
                {
                    if(x!=j && arr[x][k]>num)
                    {
                        flag++;
                        break;
                    }
                }
                if(flag>=2)
                {
                    ofile<<"Case #"<<i<<": NO\n";
                    flagg=1;
                    break;
                }
            }
            if(flagg==1)
                break;
        }
        if(flagg==0)
        ofile<<"Case #"<<i<<": YES\n";

    }
    return 0;
}
