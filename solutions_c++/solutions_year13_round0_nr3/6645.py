#include<fstream>
#include<cmath>
using namespace std;
static int _case = 1;
short __pal[10000] = {0};
int __sqrt[10000] = {0};
ifstream fin("input.txt");
ofstream fout("output.txt");
void result(int _r) {
    fout << "Case #" << _case << ": " << _r << endl;
}
int _pal(int n)
{
    if(n == -1) return 2;
    if(__pal[n] == 0) {
        int rev = 0, num, dig;
        num = n;
        while (num > 0)
        {
            dig = num % 10;
            rev = rev * 10 + dig;
            num = num / 10;
        }
        if(n == rev) __pal[n] = 1;
        else __pal[n] = 2;
    }

    return __pal[n];
}
int _sqrt(int n)
{
    if(__sqrt[n] == 0) {
        __sqrt[n] = (pow(sqrt(n), 2) == n) ? sqrt(n) : -1;
    }
    return __sqrt[n];
}

void solve()
{
    int A, B;
    int _r = 0;
    fin >> A >> B;
    for(int i = A; i <= B; i++) {
        if(_pal(i) == 1 && _pal(_sqrt(i)) == 1) {
                _r++;
        }
    }


    result(_r);

}

int main() {
    int total;
    fin >> total;
    while(total --) {
        solve();
        _case++;
    }
    return 0;
}
