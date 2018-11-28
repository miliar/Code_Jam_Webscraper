#include<fstream>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("B-small-attempt0.in");
    fout.open("output.txt");
    int T,A,B,K,l,i,j,count;
    fin>>T;
    for(l=1;l<=T;l++)
    {
        fin>>A>>B>>K;
        count=0;
        for(i=0;i<A;i++)
        {
            for(j=0;j<B;j++)
            {
                if((i&j)<K)
                count++;
            }
        }
        fout<<"Case #"<<l<<": "<<count<<endl;
    }
    return 0;
}
