#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <stdio.h>

using namespace std;
int T, t;
int N, n;
fstream fin, fout;
long long result;
unsigned long long P, Q;
//char car[110][3]={0};
string car[110];
char str[105];
long long fact(long long n)
{
    if (n<=1) return 1;
    else return (n*fact(n-1)%1000000007);
}
long long solve()
{
    int qCnt=0, pCnt=0;
    scanf("%llu/%llu", &P, &Q);
//    cout << P << " " << Q << endl;
    if((Q%P)==0)
    {
        Q=Q/P; P=1;
    }
    if((Q&(Q-1))!=0)
        return -1;
    
    while(Q!=1){qCnt++; Q=Q>>1;}
    while(P!=1){pCnt++; P=P>>1;}
//    cout << qCnt << " " << pCnt << endl; 
    return qCnt-pCnt;
}
int main()
{
    fin.open("input.txt", ios::in);
    fout.open("output.txt", ios::out);
    scanf("%d", &T);
    for(t=1;t<=T;t++){
        result = solve();
        if(result==-1)
        {
            cout << "Case #" << t << ": impossible" << endl;
            fout << "Case #" << t << ": impossible" << endl;
        }
        else
        {
            cout << "Case #" << t << ": " << result << endl;
            fout << "Case #" << t << ": " << result << endl;
        }
    }
    fout.close(); fin.close(); return 0;
}
