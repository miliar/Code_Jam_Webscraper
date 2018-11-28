#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int T,X=1;

    ifstream fin("B-small-attempt0.in");
    ofstream fout("B-small-attempt0.out");

    fin >> T;

    while(T-->0)
    {
        int A, B, K;

        fin >> A >> B >> K;

        int Y = 0;

        for (int i=0;i<A;i++) {
            for (int ii=0;ii<B;ii++) {
                if ((i&ii) < K)
                    Y++;
            }
        }

        fout << "Case #" << X++ << ": " << Y << "\n";
    }
    return 0;
}
