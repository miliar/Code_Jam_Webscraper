#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
    int num[100];
    pair <char, int> A[100][100];
    ifstream in("A.in");
    ofstream out("A.out");
    int t,n,average,sum;
    char temp;
    bool f;
    string temp2;
    in>>t;
    for (int z=0;z<t;z++)
    {
        f=false;
        in>>n;
        for (int i=0;i<n;i++)
        {
           in>>temp2;
           A[i][0].first=temp2[0];A[i][0].second=1;
           num[i]=1;
           for (int j=1;j<temp2.length();j++)
           {
                if (temp2[j]==A[i][num[i]-1].first) A[i][num[i]-1].second++;
                else
                {
                    num[i]++;
                    A[i][num[i]-1].first=temp2[j];
                    A[i][num[i]-1].second=1;
                }
           }
        }
        for (int i=1;i<n;i++)
        {
            if (num[i]!=num[0]) f=true; else
            for (int j=0;j<num[i];j++)
            {
                if (A[i][j].first!=A[0][j].first) f=true;
            }
        }
        sum=0;
        for (int i=0;i<num[0];i++)
        {
            average=0;
            for (int j=0;j<n;j++)
            {
                average+=A[j][i].second;
            }
            average/=n;
            for (int j=0;j<n;j++)
            {
                sum+=abs(average-A[j][i].second);
            }

        }
        if (f) out<<"Case #"<<z+1<<": Fegla won"<<endl;
        else out<<"Case #"<<z+1<<": "<<sum<<endl;
    }
    return 0;
}
