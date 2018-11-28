#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int gprod[8][8] = {
{0,1,2,3,4,5,6,7},
{1,4,3,6,5,0,7,2},
{2,7,4,1,6,3,0,5},
{3,2,5,4,7,6,1,0},
{4,5,6,7,0,1,2,3},
{5,0,7,2,1,4,3,6},
{6,3,0,5,2,7,4,1},
{7,6,1,0,3,2,5,4}};

const long glog[8][8] = {
{0,-1,-1,-1,-1,-1,-1,-1},
{0,1,-1,-1,2,3,-1,-1},
{0,-1,1,-1,2,-1,3,-1},
{0,-1,-1,1,2,-1,-1,3},
{0,-1,-1,-1,1,-1,-1,-1},
{0,3,-1,-1,2,1,-1,-1},
{0,-1,3,-1,2,-1,1,-1},
{0,-1,-1,3,2,-1,-1,1}};

const int ginv[8] = {0,5,6,7,4,1,2,3};

int gexp(int x, long n)
{
    n %= 8;
    int p = 0;
    for(int i=0; i<n; i++)
        p = gprod[p][x];
    return p;
}

int main()
{
    int T;
    cin >> T;
    for(int k=1; k<=T; k++)
    {
        int L; long X;
        cin >> L >> X;
        string s;
        cin >> s;
        vector<int> sn(L);
        for(int i=0; i<L; i++)
            sn[i] = s[i] - 'h';
        int ptot = 0;
        for(int i=0; i<L; i++)
            ptot = gprod[ptot][sn[i]];
        if(gexp(ptot,X) != 4)
        {
            cout << "Case #" << k << ": NO" << endl;
            continue;
        }
        int p = 0; long indx = -1;
        for(int i=0; i<L; i++)
        {
            p = gprod[p][sn[i]];
            long expn = glog[ptot][gprod[1][ginv[p]]];
            if(expn >= 0)
            {
                if(indx==-1 || expn*L+i<indx)
                    indx = expn*L+i;
            }
        }
        if(indx == -1)
        {
            cout << "Case #" << k << ": NO" << endl;
            continue;
        }
        p = 0; long kndx = -1;
        for(int i=L-1; i>=0; i--)
        {
            p = gprod[sn[i]][p];
            long expn = glog[ptot][gprod[ginv[p]][3]];
            if(expn >= 0)
            {
                if(kndx==-1 || L*(X-expn-1)+i>kndx)
                    kndx = L*(X-expn-1)+i;
            }
        }
        if(kndx == -1)
        {
            cout << "Case #" << k << ": NO" << endl;
            continue;
        }
        if(indx>=X*L || kndx<0 || indx>=kndx)
        {
            cout << "Case #" << k << ": NO" << endl;
            continue;
        }
        cout << "Case #" << k << ": YES" << endl;
    }
    return 0;
}
