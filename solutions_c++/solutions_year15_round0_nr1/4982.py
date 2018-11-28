#include <bits/stdc++.h>

using namespace std;

int main(int argc, char* argv[])
{
    vector<string> ovat;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.out","w",stdout);
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int no;
        string mia;
        cin>>no;
        cin>>mia;
        ovat.push_back(mia);
    }

    for(int i=0;i<n;i++)
    {
        int person=0;
        int in_piedi=((int)ovat[i][0]-48);
        for(int j=1;j<ovat[i].size();j++)
        {
            if(ovat[i][j]!='0')
            {
                if(in_piedi>=j)
                    in_piedi+=((int)ovat[i][j]-48);
                else
                {
                    person+=(j-in_piedi);
                    in_piedi+=person+((int)ovat[i][j]-48);
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<person<<endl;
    }
    return 0;
}
