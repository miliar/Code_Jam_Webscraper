#include<iostream>
#include<algorithm>
using namespace std;

int T, L, X, noc=1;
const int MAX_L = 1e4+7;

struct val
{
    int sign;
    char z; // char
};

val res[MAX_L][MAX_L];

val operator*(val a, val b)
{
    val ret;
    if(a.z=='1')
    {
        ret.z=b.z; ret.sign=a.sign*b.sign;
    }
    else if(b.z=='1')
    {
        ret.z=a.z; ret.sign=a.sign*b.sign;
    }
    else if(a.z=='i')
    {
        if(b.z=='i') {ret.z='1'; ret.sign=a.sign*b.sign*(-1);}
        if(b.z=='j') {ret.z='k'; ret.sign=a.sign*b.sign;}
        if(b.z=='k') {ret.z='j'; ret.sign=a.sign*b.sign*(-1);}
    }
    else if(a.z=='j')
    {
        if(b.z=='i') {ret.z='k'; ret.sign=a.sign*b.sign*(-1);}
        if(b.z=='j') {ret.z='1'; ret.sign=a.sign*b.sign*(-1);}
        if(b.z=='k') {ret.z='i'; ret.sign=a.sign*b.sign;}
    }
    else if(a.z=='k')
    {
        if(b.z=='i') {ret.z='j'; ret.sign=a.sign*b.sign;}
        if(b.z=='j') {ret.z='i'; ret.sign=a.sign*b.sign*(-1);}
        if(b.z=='k') {ret.z='1'; ret.sign=a.sign*b.sign*(-1);}
    }
    return ret;
}

main()
{
    ios_base::sync_with_stdio(0);
    cin >> T;
    while(T--)
    {
        bool possible=false;
        cin >> L >> X;
        string S;
        cin >> S;
        // brute start
        for(int rep=1; rep<=X; ++rep)
            for(int i=0; i<L; ++i) {res[i+(rep-1)*L][i+(rep-1)*L].z=S[i]; res[i+(rep-1)*L][i+(rep-1)*L].sign=1;}
        L=L*X;
        // brute end
        for(int len=2; len<=L; ++len)
        {
            for(int i=0; i<=L-len; ++i)
            {
                res[i][i+len-1]=res[i][i]*res[i+1][i+len-1];
            }
        }
        /*for(int i=0; i<L; ++i)
        {
            cout << i << " : ";
            for(int j=i; j<L; ++j) cout << res[i][j].z << " ";
            cout << endl;
        }*/
        for(int i=0; i<L-2; ++i)
        {
            for(int j=i+1; j<L-1; ++j)
            {
                if(res[0][i].z=='i' && res[0][i].sign==1 && res[i+1][j].z=='j' && res[i+1][j].sign==1 && res[j+1][L-1].z=='k' && res[j+1][L-1].sign==1) possible=true;
            }
        }
        cout << "Case #" << noc++ << ": ";
        if(possible) cout << "YES" << endl;
        else cout << "NO" << endl;
    }
    return 0;
}
