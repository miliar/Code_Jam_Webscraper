#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

unsigned long long cases, A, B;
ifstream fin("C-small-attempt0.in");
ofstream fout("C-small-attempt0.out");

int checkp(unsigned long long i)
{
    string tmp;
    int index = 0;
    while(i)
    {
        tmp.append(1,i%10+48);
        i /=10;
    }

    int start, end;
    for(start = 0, end = tmp.length()-1; start<=end; start++, end--)
    {
        if(tmp[start] != tmp[end]) break;
    }
    if(start <= end) return 0;
    else return 1;
}

int check(unsigned long long i)
{
    if(!checkp(i)) return 0;
    unsigned long long sq = sqrt(i);
    if(sq*sq != i) return 0;
    if(!checkp(sq)) return 0;
    return 1;
}

int main()
{
    fin >> cases;
    int round = 1;
    while(cases--)
    {
        int sum = 0;
        fin >> A >> B;
        for(; A<=B; A++)
        {
            //cout << "1111\n";
            if(check(A)) sum++;
        }
        fout << "Case #" << round++ << ": " << sum << endl;
    }
}
