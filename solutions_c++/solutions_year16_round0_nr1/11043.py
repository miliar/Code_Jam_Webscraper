#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <fstream>
using namespace std;
void seperating(std::vector <int>& s,unsigned long long num)
{
    int r;
    unsigned long long t=num;
    while(t!=0)
    {
        r=t%10;
        s.push_back(r);
        t/=10;
    }
}
int main()
{
    int t;
    long n,i,j;
    set <int> digits;
    vector <int> seperate;
    ifstream input;
    ofstream output;
    unsigned long long number;
    input.open("A-large.in");
    output.open("Outputl.txt");
    input >>t;
    for(j=1;j<=t;j++)
    {
        digits.clear();
        input>>n;
        if(n==0)
        {
            output<<"Case #"<<j<<": INSOMNIA"<<endl;
            continue;
        }
        i=1;
        do
        {
            seperate.clear();
            number=i*n;
            seperating(seperate,number);
            digits.insert(seperate.begin(),seperate.end());
            i++;
        }while(digits.size()<10);
        output<<"Case #"<<j<<": ";
        output<<number<<endl;
    }
    input.close();
    output.close();
    return 0;
}
