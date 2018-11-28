//gmw.sjtu@gmail.com
//list~~
#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out");
    //only for the large A.
    int N;
    fin>>N;
    for (int n=0;n<N;n++)
    {
        int count=0;
        long long int A,B;
        //longlong A,B;
        fin>>A>>B;//A>=1 & B<=1000
        if (A>1) count--;
        if (A>4) count--;
        if (A>9) count--;
        if (A>121) count--;
        if (A>484) count--;

        if(B>=1) count++;
        if(B>=4) count++;
        if(B>=9) count++;
        if (B>=121)count++;
        if (B>=484)count++;
        fout<<"Case #"<<n+1<<": ";
        fout<<count<<endl;
    }
    return 0;
}
