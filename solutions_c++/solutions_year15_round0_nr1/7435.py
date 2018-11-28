#include <fstream>
#include <cstring>

using namespace std;

ifstream in("ProbA.in");
ofstream out("ProbA.out");

const int NMAX = 2000;

string s;
int N, Ans;

void Rezolva() {
    in >> N;
    in >> s;
    Ans = 0;
    int Om = (int)(s[0] - '0');
    for( int i = 1;  i <= N;  ++i ) {
        if( Om < i )  {
            Ans += i - Om;
            Om += ( i - Om );
        }
        Om += (s[i] - '0');
    }
    out << Ans;
}

int main() {
    int T;
    in >> T;
    for( int t = 0;  t < T;  ++t ) {
        out << "Case #" << t+1 << ": ";
        Rezolva();
        out << '\n';
    }
    return 0;
}
