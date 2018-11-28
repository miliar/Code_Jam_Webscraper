#include <iostream>
#include <set>
#include <fstream>
using namespace std;
set<int> numbers;
void addset(long long x)
{
    while(x!=0)
    {
        numbers.insert(x%10);
        x/=10;
    }
}
int main()
{
      ifstream fin("input.in");
    ofstream fout("output.out");

    //-- check if the files were opened successfully
    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int t;
    fin>>t;
    for(int i=0 ; i<t ; i++)
    {
        int n;
        fin>>n;

        if(n==0)
            fout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        else
        {
            long long j;
            for(j=n ; numbers.size()!=10 ; j+=n)
            {
                addset(j);
            }
            fout<<"Case #"<<i+1<<": "<<j-n<<endl;
        }
        numbers.clear();
    }
    fin.close();
    fout.close();
    return 0;
}
