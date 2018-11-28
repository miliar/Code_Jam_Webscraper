#include<fstream>
using namespace std;

#define IN_FILE "a.in"
#define OUT_FILE "output.txt"

int main()
{
    ifstream in;
    ofstream out;
    in.open(IN_FILE);
    out.open(OUT_FILE);
    int t,choice,arr[4][4],i,j,x;
    in>>t;
    for(x=1;x<=t;++x)
    {
        int ans1[17] = {},ans2[17] = {};
        in>>choice;
        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
        {
            in>>arr[i][j];
        }
        for(j=0;j<4;++j)
        ans1[arr[choice-1][j]] = 1;
        in>>choice;
        for(i=0;i<4;++i)
            for(j=0;j<4;++j)
        {
            in>>arr[i][j];
        }
        for(j=0;j<4;++j)
        {
            ans2[arr[choice-1][j]] = 1;
        }
        int counter = 0,value = 0;
        for(j=1;j<=16;++j)
        {
            if(ans1[j] && ans2[j])
            {
                ++counter;
                value = j;
            }
        }
        if(counter == 1)
        {
           out<<"Case #"<<x<<": "<<value<<'\n';
        }
        else if(counter == 0)
        {
            out<<"Case #"<<x<<": Volunteer cheated!\n";
        }
        else
        {
            out<<"Case #"<<x<<": Bad magician!\n";
        }
    }
    in.close();
    out.close();
    return 0;
}
