#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>
#include <fstream>

using namespace std;

int A1[20][20],A2[20][20];
int a1[20], a2[20];
int main()
{
    ofstream ofile;
    ifstream ifile;
    ofile.open("output.txt");
    ifile.open("input.txt");
    int T;
    ifile>>T;
    for(int zz = 0; zz<T; zz++)
    {
        int N1, N2;
        ifile>>N1;
        for(int i = 0; i<4; i++)
            for(int j = 0; j<4; j++)
                ifile>>A1[i][j];
        ifile>>N2;
        for(int i = 0; i<4; i++)
            for(int j = 0; j<4; j++)
                ifile>>A2[i][j];
        
        for(int i = 0; i<4; i++)
        {
            a1[i] = A1[N1-1][i];
            a2[i] = A2[N2-1][i];
        }
        int cnt = 0, num = 0;
        for(int i = 0; i<4; i++)
        {
            for(int j = 0; j<4; j++)
            {
                if(a1[i] == a2[j])
                {
                    cnt++;
                    num = a1[i];
                }
            }
        }
        if(cnt==1)
            ofile<<"Case #"<<(zz+1)<<": "<<num<<endl; 
        else if(cnt == 0)
            ofile<<"Case #"<<(zz+1)<<": "<<"Volunteer cheated!"<<endl;
        else ofile<<"Case #"<<(zz+1)<<": "<<"Bad magician!"<<endl;
    }
    ofile.close();
    ifile.close();
    return 0;
}
