#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int n;
    fin>>n;

    int A,B,K;
    int count=0;
    //n=1;
    for(int i=0;i<n;i++)
    {
        fin>>A>>B>>K;
        count=0;
        for(int j=0;j<A;j++)
        {
            for(int l=0;l<B;l++)
            {
                //cout<<j<<"\t"<<l<<"\t"<<(j&l)<<endl;
                if((j&l)<K)
                {
                    count++;
                }
            }
        }
        fout<<"Case #"<<i+1<<": "<<count<<endl;
    }



    return 0;
}
