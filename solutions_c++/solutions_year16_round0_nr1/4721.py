#include <iostream>
#include <fstream>
#include <set>

using namespace std;
int main()
{
    int inputnumber,ii,n,totalcopy;
    int total=0;
    ifstream fin("input");
    ofstream fout("output");
    bool sleep;
    fin>>inputnumber;
    set<int> flag;
    for (int ii=1;ii<=inputnumber;ii++)
    {
        sleep=false;
        total=0;
        fin>>n;
        flag.clear();
        for (int jj=0;jj<10000;jj++)
        {
            total+=n;
            totalcopy=total;
            while (totalcopy>0)
            {
                flag.insert(totalcopy % 10);
                totalcopy/=10;
            }
            if (flag.size()==10)
            {
                fout<<"Case #"<<ii<<": "<<total<<endl;
                sleep=true;
                break;
            }
        }
        if (!sleep)
        fout<<"Case #"<<ii<<": INSOMNIA"<<endl;
    }
    return 0;
}