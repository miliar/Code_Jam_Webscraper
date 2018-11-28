#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>


using namespace std;

int main()
{
    ofstream fout;
    ifstream fin;
    fin.open("D-large.in");
    fout.open ("answers.txt");
    int t;
    fin>>t;
    for(int ctr1=0;ctr1<t;ctr1++)
    {
        int n;
        fin>>n;
        double firstNiza[n];
        double secondNiza[n];
        for(int ctr2=0;ctr2<n;ctr2++)
        {
            fin>>firstNiza[ctr2];
        }
        for(int ctr2=0;ctr2<n;ctr2++)
        {
            fin>>secondNiza[ctr2];
        }
        stable_sort(firstNiza,firstNiza+n);
        stable_sort(secondNiza,secondNiza+n);
        int ctrTemp=0;
        int rez1=0;
        for(int ctr2=0;ctr2<n;ctr2++)
        {
            if (firstNiza[ctr2]>secondNiza[ctrTemp])
            {
                rez1++;
                ctrTemp++;
            }
        }
        int rez2=0;
        int ctr3=n-1;
        for(int ctr2=n-1;ctr2>=0;ctr2--)
        {
            if (firstNiza[ctr2]>secondNiza[ctr3])
            {
                rez2++;
            }
            else {
                ctr3--;
            }
        }
        fout<<"CASE #"<<ctr1+1<<": "<<rez1<<" "<<rez2<<endl;
    }

    fout.close();
    fin.close();
    return 0;
}
