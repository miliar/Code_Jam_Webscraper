#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

string alg(int M, int N, int design[100][100])
{
    int lawn[100][100];
    for (int i=0; i<M; ++i)
    {
        int greatest=design[i][0];
        for (int j=0; j<N; ++j)
            if (design[i][j]>greatest)
                greatest=design[i][j];
        for (int j=0; j<N; ++j)
            lawn[i][j]=greatest;
    }
    for (int i=0; i<N; ++i)
    {
        int greatest=design[0][i];
        for (int j=0; j<M; ++j)
            if (design[j][i]>greatest)
                greatest=design[j][i];
        for (int j=0; j<M; ++j)
            if (lawn[j][i]>greatest)
                lawn[j][i]=greatest;
    }
    /*for (int i=0; i<M; ++i)
    {
        for (int j=0; j<N; ++j)
            cout << lawn[i][j];
        cout << endl;
    }*/
    for (int i=0; i<M; ++i)
        for (int j=0; j<N; ++j)
            if (lawn[i][j]!=design[i][j])
                return "NO";
    return "YES";
}

int main()
{
    /*int M, N, design[100][100]={{2,2,2,2,2},
                                {2,1,1,1,2},
                                {2,1,2,1,2},
                                {2,1,1,1,2},
                                {2,2,2,2,2}};*/
    /*int design[100][100]={{2,1,2},
                          {1,1,1},
                          {2,1,2}};
    int design[100][100]={{1,2,1}};*/
    int T, M, N, design[100][100];
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    in >> T;
    for (int i=1; i<=T; ++i)
    {
        in >> M >> N;
        for (int j=0; j<M; ++j)
            for (int k=0; k<N; ++k)
                in >> design[j][k];
        out << "Case #" << i << ": " << alg(M, N, design) << endl;
    }
    return 0;
}
