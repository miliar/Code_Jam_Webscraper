#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <stack>
using namespace std;

bool safe(const int* pv, int N, int total)
{
    int m = total/2;
    if(m<=0 && total>0) return false;
    for(int i=0; i<N; ++i)
    {
        if(pv[i]>m) return false;
    }
    return true;
}

string findOut2(int* pv, int N, int total)
{
    string result = "";
    for(int i=0; i<N; ++i)
    {
        if(pv[i]<=0)
        {
            continue;
        }
        --pv[i];
        for(int j=0; j<N; ++j)
        {
            if(pv[j]<=0)
            {
                continue;
            }
            --pv[j];
            if(safe(pv, N, total-2))
            {
                result.push_back('A'+i);
                result.push_back('A'+j);
                return result;
            }
            ++pv[j];
        }
        ++pv[i];
    }
}

string findOut1(int* pv, int N, int total)
{
    string result = "";
    for(int i=0; i<N; ++i)
    {
        if(pv[i]<=0)
        {
            continue;
        }
        --pv[i];
        if(safe(pv, N, total-1))
        {
            result.push_back('A'+i);
            return result;
        }
    }
    return result;
}

int main(int argc, char* argv[])
{
    int Pi[26]={0};
    int T = 0;
    cin >> T;
    for(int i=1; i<=T ;++i)
    {
        int N=0;
        cin >> N;
        int total = 0;
        for(int p=0; p<N; ++p)
        {
            cin >> Pi[p];
            total+=Pi[p];
        }
        string result = "";
        while(total>0)
        {
            string tmp = findOut2(Pi, N, total);
            if(tmp.length()>0)
            {
                total -= 2;
                result = result + " " + tmp;
                continue;
            }
            tmp = findOut1(Pi, N, total);
            if(tmp.length()>0)
            {
                total -= 1;
                result = result + " " + tmp;
                continue;
            }
            cout << "ERROR" << endl;
        }
        cout << "Case #" << i << ": " << result << endl;
    }
}