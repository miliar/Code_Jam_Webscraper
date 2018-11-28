//Standing Ovation

#include<iostream>
#include<fstream>
#include<string>

using namespace std;
int main()
{
    int testcases,n;
    string str;
    int ans,ep;
    ifstream fin("so_large.txt");
    ofstream fout("so_out2");
    fin>>testcases;
    for(int i=0;i<testcases;i++)
    {
        ans = 0;    ep=0;
        fin>>n>>str;
        //cout<<n<<"\t"<<str<<endl;
        for(int k=0;k<=n;k++)
        {
            if(str[k]=='0')
            {
                if(ep==0)   ans++;
                else    ep-=1;
            }
            else
            {
                ep+=str[k]-49;
            }
        }
        fout<<"Case #"<<(i+1)<<": "<<ans<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
