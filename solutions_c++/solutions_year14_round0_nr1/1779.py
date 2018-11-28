#include<fstream>
#include<iostream>
#include<vector>
using namespace std;
int main()
{
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int t;
    fin>>t;
    for(int i=1;i<=t;i++)
    {
        int r1,r2;
        fin>>r1;
        int arr[17] = {0};
        for(int kk=1;kk<=4;kk++)
        {
            for(int jj = 1;jj<=4;jj++)
            {
                int x;
                fin>>x;
                if(kk==r1)
                    arr[x] = 1;
            }
        }
        fin>>r2;
        int matches = 0;
        int ans = 0;
        for(int kk=1;kk<=4;kk++)
        {
            for(int jj = 1;jj<=4;jj++)
            {
                int x;
                fin>>x;
                if(kk==r2 && arr[x])
                {
                    matches++;
                    ans = x;
                }
            }
        }
        fout<<"Case #"<<i<<": ";
        if(matches<=0)
            fout<<"Volunteer cheated!";
        else if(matches>1)
            fout<<"Bad magician!";
        else
            fout<<ans;
        fout<<endl;
    }

    fin.close();
    fout.close();
    return 0;
}
