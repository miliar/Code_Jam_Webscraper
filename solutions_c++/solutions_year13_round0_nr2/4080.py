#include<iostream>
#include<fstream>
#include<sstream>

using namespace std;
int main()
{
    fstream fin,fout;
    fin.open("b.in");
    fout.open("b.txt");
    int t;
    fin>>t;
    for(int z=1;z<=t &&!fin.eof();z++)
    {
        int n,m,tmp;
        fin>>n>>m;
        int lwn[n][m];
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            {
                fin>>tmp;
                lwn[i][j]=tmp;
            }

        }

        bool ans=true;
        for(int i=0;i<n && ans;i++)
            for(int j=0;j<m && ans;j++)
                {
                    bool f1,f2;
                    f1=f2=1;
                    for(int k=0;k<n &&f1;k++)
                        if(lwn[k][j]>lwn[i][j])
                                    f1=false;
                    for(int k=0;k<m &&f2;k++)
                        if(lwn[i][k]>lwn[i][j])
                                    f2=false;
                    if(!f1 && !f2)
                        ans=false;
                }
        string ns;
        ns="Case #";
        stringstream ss;
        ss<<z;
        ns+=ss.str();
        ns+=": ";
        if(ans)
            ns+="YES";
        else
            ns+="NO";
        fout<<ns;
        fout<<endl;
    }
    fout.close();
    fin.close();
return 0;
}
