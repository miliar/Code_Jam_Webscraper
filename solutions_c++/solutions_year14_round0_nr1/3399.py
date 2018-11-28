#include <cstdio>
#include <vector>
#include <algorithm>
#define infile "a.in"
#define outfile "a.out"
#define moves 4

using namespace std;

int first[moves][moves];
int second[moves][moves];
int firstRow, secondRow;

void read(int m[moves][moves], int &row) {

    scanf("%d\n", &row);

    for (size_t i = 0; i < moves; ++i) {
        for (size_t j = 0; j < moves; ++j) {
            scanf("%d", &m[i][j]);
        }
    }

}

void read() {
    read(first, firstRow);
    read(second, secondRow);
}

vector <int> getRow(int m[moves][moves], int row) {
    vector <int> v;

    for (size_t i = 0; i < moves; ++i) {
        v.push_back(m[row-1][i]);
    }

    return v;
}

void solve(int t) {

    vector <int> a = getRow(first, firstRow);
    vector <int> b = getRow(second, secondRow);
    vector <int> ::iterator it;
    vector <int> c(moves);

    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    it = set_intersection(a.begin(), a.end(), b.begin(), b.end(), c.begin());
    c.resize(it - c.begin());

    printf("Case #%d: ", t);

    if (c.size() == 1) {
        printf("%d\n", c[0]);
    } else if (c.size() == 0) {
        printf("Volunteer cheated!\n");
    } else {
        printf("Bad magician!\n");
    }
}

int main() {
    freopen(infile, "r", stdin);
    freopen(outfile, "w", stdout);

    int t;
    scanf("%d\n", &t);

    for (int i = 0; i < t; ++i) {
        read();
        solve(i+1);
    }

    fclose(stdin);
    fclose(stdout);
    return 0;
}
