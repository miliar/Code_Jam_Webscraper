#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

//cout.precision(6);
//cout.setf( std::ios::fixed, std:: ios::floatfield ); // floatfield set to fixed

typedef unsigned long long int ulli;
struct oe
{
    int o;
    int e;
};

int main()
{
    ifstream inFile( "a.in" );
    int caseCount;
    inFile >> caseCount;
    
    for (int csIx = 1; csIx <= caseCount; ++csIx)
    {
        cout << "Case #" << csIx << ": ";
        ulli N;
        int M;
        ulli o[1000], e[1000], p[1000];
        
        inFile >> N >> M;
        vector<oe> oes;
        for (int i = 0; i < M; ++i)
        {
            inFile >> o[i] >> e[i] >> p[i];
            for (int k = 0; k < p[i]; ++k)
            {
                oe a;
                a.o = o[i]; a.e = e[i];
                oes.push_back(a);
            }
        }

        int res = 0;
        while (1) {
        bool found = false;
        for (int i = 0; i < oes.size(); ++i)
        {
            for (int j = i + 1; j < oes.size(); ++j)
            {
                int s1 = oes[i].o;
                int e1 = oes[i].e;
                int s2 = oes[j].o;
                int e2 = oes[j].e;
                
                if (s2 > e1) continue;
                if (s1 > e2) continue;
                if (s1 < s2 && e1 < e2)
                {
                    res += (s2 - s1) * (e2 - e1);
                    oe n1; n1.o = s1; n1.e = e2;
                    oe n2; n2.o = s2; n2.e = e1;
                    
                    oes.erase(oes.begin() + max(i, j));
                    oes.erase(oes.begin() + min(i, j));
                    oes.push_back(n1);
                    oes.push_back(n2);
                    found = true;
                }
                if (s1 > s2 && e1 > e2)
                {
                    res += (s2 - s1) * (e2 - e1);
                    oe n1; n1.o = s1; n1.e = e2;
                    oe n2; n2.o = s2; n2.e = e1;
                    
                    oes.erase(oes.begin() + max(i, j));
                    oes.erase(oes.begin() + min(i, j));
                    oes.push_back(n1);
                    oes.push_back(n2);
                    found = true;
                }
            }
        }
            if (!found) break;
        }
        cout << res << endl;
/*
        ulli data[1000][1000];
        for (int i = 0; i < 1000; ++i)
        {
            for (int j = 0; j < 1000; ++j)
            {
                data[i][j] = 0;
            }
        }
        for (int i = 0; i < M; ++i)
        {
            data[o[i]][e[i]] = p[i];
        }
/*
        cout << endl;
        for (int i = 1; i <= N; ++i)
        {
            for (int j = 1; j <= N; ++j)
            {
                cout << data[i][j] << " ";
            }
            cout << endl;
        }
        
/*
        for (int i = 0; i < M; ++i)
        {
            int oCurr = o[i];
            int eCurr = e[i];
            int oPos = find(oS.begin(), oS.end(), oCurr) - oS.begin();
            int ePos = find(eS.begin(), eS.end(), eCurr) - eS.begin();

            cout << "From " << oCurr << " to " << eCurr << ": " << data[oPos][ePos] << endl;
            
        }
*/
        /*
        ulli res = 0;
        for (int start = 1; start <= N; ++start)
        {
            for (int end = start; end <= N; end++)
            {
                if (data[start][end] == 0)
                    continue;
                
                for (int s2 = end; s2 > start + 1; --s2)
                {
                    for (int e2 = N; e2 >= end; --e2)
                    {
                        if (data[s2][e2] == 0) continue;
                        if (s2 == e2) continue;
                        
                        int common = min(data[start][end], data[s2][e2]);
                        res += (s2 - start) * (e2 - end) * common;
                        data[start][end] -= common;
                        data[s2][e2] -= common;
                        data[start][e2] += common;
                        data[s2][end] += common;
                    }
                }
            }
        }
/*
        cout << endl;
        for (int i = 1; i <= N; ++i)
        {
            for (int j = 1; j <= N; ++j)
            {
                cout << data[i][j] << " ";
            }
            cout << endl;
        }
*/ 
//        cout << res << endl;
    }
    
    inFile.close();
    return 0;
}
