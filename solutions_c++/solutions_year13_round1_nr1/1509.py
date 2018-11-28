#include<fstream>

using namespace std;

long generate(long a, long b)
{
     long count = 0;
     long sum = 0;
     long temp = 2* a + 1;
     while(b >= sum + temp)
     {
             sum += temp;
             //cout << sum << temp << endl;
             temp+= 4;
             count++;
     }
     return count;
}
int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("result.out");
    int num  = 0;
    long r,t;
    fin >> num;
    int i = 0;
    while(i < num)
    {
            fin >> r >> t;
            fout << "Case #" << (i+1) << ": " << generate(r,t) <<endl;
            i++;
    }
    system("PAUSE");
    return 0;
}
