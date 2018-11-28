#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int n,num;
    vector <double> a(0);
    vector <double> b(0);
    double temp;
    fin>>n;
    int j,k;
    int count;
    int tem;

    for(int i=1;i<=n;i++)
    {
        fin>>num;
        for(j=0;j<num;j++)
        {
            fin>>temp;
            a.push_back(temp);
        }
        for(j=0;j<num;j++)
        {
            fin>>temp;
            b.push_back(temp);
        }
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        count=0;
        j=0;k=0;
        while(1)
        {
            if(j>=num)
                break;

            if(a[j]>b[k])
            {
                count++;
                k++;
                j++;
            }
            else
            {
                j++;
            }

        }


        fout<<"Case #"<<i<<": "<<count;
        k=0;j=0;
        count=0;

        while(1)
        {
            if(k>=num)
                break;

            if(a[j]<b[k])
            {
                count++;
                k++;
                j++;
            }
            else
            {
                k++;
            }

        }

        fout<<" "<<num-count<<endl;

        a.clear();
        b.clear();
    }


    return 0;
}
