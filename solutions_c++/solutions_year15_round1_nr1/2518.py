#include <iostream>
using namespace std;

int m[1001];

int main(int argc, const char * argv[]) {
    
    FILE *fin = freopen("in.txt", "r", stdin);
    //FILE *fout =
    freopen("out.txt", "w", stdout);
    
    int TCount = 0;
    int T;
    cin >> T;
    while (T--)
    {
        
        int N;
        cin >> N;
        int m1 = 0, m2 = 0;
        int Gap, GapMax = 0;
        
        for (int i = 0; i < N; i++)
        {
            cin >> m[i];
            if (i == 0) continue;
            Gap = m[i-1] - m[i];
            m1 += Gap > 0 ? Gap : 0;
            GapMax = Gap > GapMax ? Gap : GapMax;
        }
        
        for (int i = 0; i < N-1; i++)
        {
            m2 += m[i] >= GapMax ? GapMax : m[i];
        }
        
        cout << "Case #" << ++TCount << ": " << m1 << " " << m2 << endl;
        
    }
    return 0;
}
