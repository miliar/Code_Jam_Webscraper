//IN THE NAME OF GOD
//BENYAM1N

#include <iostream>
#include <set>
#include <iomanip>
#include <cstring>
#include <algorithm>
#include <string>
#include <fstream>
#include <cmath>
#include <deque>
#include <queue>
#include <vector>
#include <map>
#include <set>

using namespace std;

const long long MAX_N = 100000+100;

#define lc(x) 2*x
#define rc(x) 2*x+1
#define inf 1<<30

typedef pair<int,int> pii;
typedef long long ll;
typedef unsigned long long ull;

ifstream fin("a.in");
ofstream fout("out.txt");

int main()
{
    int t;
    fin>>t;
    int w = 1;
    while(t--)
    {
        int a,b,arr1[10][10],arr2[10][10];
        fin>>a;
        for(int i = 1 ; i <= 4 ; i++)
            for(int j = 1 ; j <= 4 ; j++) fin>>arr1[i][j];
        fin>>b;
        for(int i = 1 ; i <= 4 ; i++)
            for(int j = 1 ; j <= 4 ; j++) fin>>arr2[i][j];
        int ans = 0;
        int p;
        //cout<<arr1[2][3]<<" "<<arr2[3][3]<<endl;
        for(int i = 1 ; i <= 4 ; i++)
            for(int j = 1 ; j <= 4 ; j++) if(arr1[a][i] == arr2[b][j]) ans++,p = arr1[a][i];
        if(ans == 1) fout<<"Case #"<<w<<": "<<p<<endl;
        if(ans == 0) fout<<"Case #"<<w<<": "<<"Volunteer cheated!"<<endl;
        if(ans >1) fout<<"Case #"<<w<<": "<<"Bad magician!"<<endl;
        w++;
    }
}
