#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstring>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;


ofstream outFile("../GoogleJam/output.txt");
int c[102][102];
int maxL[102];
int maxC[102];

void eval(){
    int N;
    int M;
    cin>>N;
    cin>>M;

    for(int j=0; j<102; j++)
    {
        maxL[j]=1;
        maxC[j]=1;
    }
    for(int i=0; i<N; i++)
    {
        for(int j=0; j<M; j++)
        {
            cin>>c[i][j];
            if(c[i][j]>maxL[i]) maxL[i] = c[i][j];
            if(c[i][j]>maxC[j]) maxC[j] = c[i][j];
        }
    }

    for(int i=0; i<N; i++)
    {
        for(int j=0; j<M; j++)
        {
            if(c[i][j]<maxL[i] && c[i][j]<maxC[j])
            {
                outFile<<"NO";
                cout<<"NO";
                return;
            }
        }
    }

    outFile<<"YES";
    cout<<"YES";
}

int main(){
    int cases;
    string line;
    getline(cin, line);
    istringstream(line)>>cases;
    for(int i=1; i<=cases; i++){
        cout<<"Case #"<<i<<": ";
        outFile<<"Case #"<<i<<": ";
        eval();
        outFile<<endl;
        cout<<endl;
    }
    return 0;
}
