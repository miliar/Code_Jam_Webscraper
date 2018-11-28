
#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <math.h>
#include <map>
using namespace std;
typedef long long ll;

#define MAX 1000001

int r_n[MAX];
int times[MAX];
int jump_size[MAX];

int A[MAX], B[MAX];

struct Info {
    int start;
    int end;
    int jump_size;
}info[MAX];

bool cmp (Info const& i1, Info const& i2) {
    return i1.jump_size > i2.jump_size;
}

int reverse_num(int n) {
    int l = log10(n)+1;
    int sum = 0;
    for (int i = 0; i < l; i++) {
        int x = n % 10;
        sum += x * pow(10, l-i);
        n /= 10;
    }
    return sum/10;
}

int main() {
    
    ofstream fout ("ans.txt");
    ifstream fin ("input.txt");
    
    for (int i = 1; i < MAX; i++) {
        r_n[i] = reverse_num(i);
        info[i].start = i;
        info[i].end = r_n[i];
        info[i].jump_size = r_n[i] - i;
    }
    sort (info, info+MAX, cmp);

    
    int T;
    fin >> T;
    // TEST CASES
    for (int t = 0; t < T; t++) {
        
        memset(A, 0, sizeof(A));
        memset(B, 0, sizeof(B));
        
        int N, ans=0;
        fin >> N;
        
        int jumps = 0;
        for (int i = 0; i < MAX; i++) {
            if (info[i].jump_size <= 1) break;
            
            if (info[i].end <= N && info[i].start < N) {
                int k = 0;
                for (k = 0; k < jumps; k++) {
                    if (!(info[i].start >= B[k] || info[i].end < A[k]))
                        break;
                }
                if (k == jumps) {
                    A[jumps] = info[i].start;
                    B[jumps] = info[i].end;
                    jumps++;
                    ans += info[i].jump_size - 1;
                }
            }
        }
        
        
        fout << "Case #" << t+1 << ": " << N - ans << "\n";
    }
    
    return 0;
}

