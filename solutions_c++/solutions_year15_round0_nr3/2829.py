#include <fstream>
using namespace std;
#define dim 10005

int l[dim],r[dim];

int Tot;

int abs(int a){
    return a < 0 ? -a : a;
}

int Mul(int a,int b)
{
    int semn = 1;
    if(a*b < 0) semn = -1;

    a = abs(a);
    b = abs(b);

    if(a == 1)
        return b*semn;
    if(b == 1)
        return a*semn;
    if(a == b)
        return -semn;
    if(a == int('i')){
        if(b == int('j'))
            return semn*int('k');

        if(b == int('k'))
            return -semn*int('j');
    }

    if(a == int('j')){
        if(b == int('i'))
            return -semn*int('k');

        if(b == int('k'))
            return semn*int('i');
    }

    if(a == int('k')){
        if(b == int('j'))
            return -semn*int('i');

        if(b == int('i'))
            return semn*int('j');
    }
}

int main()
{
    ifstream fin("C-small-attempt2.in");
    ofstream fout("file.out");

    int T;
    fin >> T;

    string Y = "YES";
    string N = "NO";
    string Ans;
    string s,w;

    int L,X;

    for(int t = 1; t <= T; t++){
        fin >> L >> X >> w;

        L *= X;
        s = "";

        for(int i = 1; i <= X; i++)
            s += w;

        //fout << s << "\n";

        l[0] = int(s[0]);
        for(int i = 1; i < L; i++)
            l[i] = Mul(l[i-1],int(s[i]));

        r[L-1] = int(s[L-1]);
        for(int i = L-2; i >= 0; i--)
            r[i] = Mul(int(s[i]),r[i+1]);

        Ans = N;

        for(int i = 0; i < L-2; i++){
            if(l[i] == int('i')){
                int B = 1;
                for(int j = i + 2; j < L; j++){
                    B = Mul(B,int(s[j-1]));
                    if(B == int('j') && r[j] == int('k')){
                        Ans = Y;
                        break;
                    }
                }
            }
            if(Ans == Y) break;
        }

        fout << "Case #" << t << ": " << Ans << "\n";
    }

}
