#include <iostream>
#include <fstream>

using namespace std;
ifstream in("INPUT.TXT");
ofstream out("OUTPUT.TXT");

int FirstWay(int N,int* m)
{
    int eaten = 0;
    for (int iN = 0;iN <N - 1;iN++)
    {
        if (m[iN+1] < m[iN])
            eaten+=m[iN] - m[iN+1];
    }
    return eaten;
}

int SecondWay(int N,int* m)
{
    int eaten = 0;
    int v = 0;
    for (int iN = 0;iN<N - 1;iN++)
    {
        //cout<<"iN "<<iN<<"m[iN] - m[iN+1] "<<m[iN] - m[iN+1]<<endl;
        v = max(m[iN] - m[iN+1],v);
    }
    //cout<<"v "<<v<<endl;
    for (int iN = 0;iN<N-1;iN++)
    {
        eaten+=min(m[iN],v);
    }
    return eaten;

}

int main()
{
    int T = 0;
    int N = 0;
    int m[10002];
    in >> T;
    for (int iT = 0;iT < T;iT++)
    {
        in >> N;
        for (int iN = 0;iN < N;iN++)
        {
            in >>m[iN];
        }
        out<<"Case #"<<iT+1<<": "<<FirstWay(N,m)<<" "<<SecondWay(N,m)<<endl;

    }

    return 0;
}

