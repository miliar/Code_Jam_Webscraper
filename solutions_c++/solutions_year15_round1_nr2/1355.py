#include <iostream>
#include <queue>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <set>
#include <sstream>
#include <ctime>
#include <map>
using namespace std;

int pgcd(int A,int B)
{
    return A==0?B:pgcd(B%A,A);
}

int ppcm(int A,int B)
{
    return (A*B)/pgcd(A,B);
}

int main()
{
    ios_base::sync_with_stdio(false);
    ifstream in("input.txt");
    ofstream out("output.txt");
    #define cin in
    #define cout out
    int nb_cas;
    cin>>nb_cas;
    for(int cas=1;cas<=nb_cas;cas++)
    {
        cout<<"Case #"<<cas<<": ";
        int N,B;
        cin>>B>>N;
        vector<int> M(B);
        int pp=1;
        for(int c=0;c<B;c++){cin>>M[c];pp=ppcm(pp,M[c]);}
        int reduction = 0;
        for(int c=0;c<B;c++) {reduction+=pp/M[c];}
        N%=reduction;
        vector<int> state(B,0);
        if(N==0)
            N+=reduction;
        for(int c=0;c<N;c++)
        {
            int best = 0;
            for(int c2=0;c2<B;c2++)
            {
                if(state[best] > state[c2])
                {
                    best=c2;
                }
            }
            int toReduce = state[best];
            for(int c2=0;c2<B;c2++)
            {
                state[c2]-=toReduce;
                state[c2]=max(state[c2],0);
            }
            state[best]=M[best];
            if(c==N-1)
            {
                cout<<best+1<<endl;
            }
        }
    }
}
