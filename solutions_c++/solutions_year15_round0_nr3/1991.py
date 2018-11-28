#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

const int SGN[4][4] = { {0, 0, 0, 0},
                        {0, 1, 0, 1},
                        {0, 1, 1, 0},
                        {0, 0, 1, 1} };

const int LETTER[4][4] = { {0, 1, 2, 3},
                           {1, 0, 3, 2},
                           {2, 3, 0, 1},
                           {3, 2, 1, 0} };

const int M = 8 * 4;

struct Matrix {
    int a[M][M];

    Matrix() {
        memset(a, 0, sizeof(a) );
    }

    Matrix identity() {
        Matrix matrix = Matrix();
        for (int i = 0; i < M; i++) {
            matrix.a[i][i] = 1;
        }
        return matrix;
    }

    void print() {
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                cerr << a[i][j] << " ";
            }
            cerr << "\n";
        }
        cerr << "--------------------\n";
    }
};

Matrix operator*(Matrix a, Matrix b) {
    Matrix c;
    for (int i = 0; i < M; i++)
        for (int j = 0; j < M; j++) {
            for (int k = 0; k < M; k++) {
                c.a[i][j] += a.a[i][k] * b.a[k][j];
            }
            // c.a[i][j] = min(1, c.a[i][j] );
        }
    return c;
}

map< vector<int>, int > state_to_int;
map< int, vector<int> > int_to_state;

Matrix matrix[4];

void preprocess() {
    for (int phase = 0; phase < 4; phase++)
        for (int sgn = 0; sgn < 2; sgn++)
            for (int letter = 0; letter < 4; letter++) {
                vector<int> state(3);
                state[0] = phase;
                state[1] = sgn;
                state[2] = letter;
                int id = state_to_int.size();

                state_to_int[state] = id;
                int_to_state[id] = state;

                // cerr << phase << " " << sgn << " " << letter << " " << id << "\n";
            }


    for (int letter2 = 1; letter2 < 4; letter2++)
        for (int sgn1 = 0; sgn1 < 2; sgn1++)
            for (int letter1 = 0; letter1 < 4; letter1++) {
                int sgn3 = sgn1 ^ SGN[letter1][letter2];
                int letter3 = LETTER[letter1][letter2];

                for (int phase = 0; phase < 3; phase++) {
                    vector<int> state(3);
                    state[0] = phase;
                    state[1] = sgn1;
                    state[2] = letter1;
                    int id = state_to_int[state];

                    vector<int> next_state(3);
                    int next_id;

                    next_state[0] = phase;
                    next_state[1] = sgn3;
                    next_state[2] = letter3;
                    next_id = state_to_int[next_state];
                    matrix[letter2].a[next_id][id] += 1;

                    if (sgn3 == 0 && letter3 == phase + 1) {
                        next_state[0] = phase + 1;
                        next_state[1] = 0;
                        next_state[2] = 0;
                        next_id = state_to_int[next_state];
                        matrix[letter2].a[next_id][id] += 1;
                    }
                }
            }

    // for (int i = 1; i < 4; i++) {
    //     matrix[i].print();
    // }
}

string solve() {
	Matrix current = Matrix().identity();
    int l;
    long long x;
    string s;
    cin >> l >> x >> s;
    for (int i = 0; i < l; i++) {
        current = matrix[s[i] - 'i' + 1] * current;
    }
    
    Matrix result = Matrix().identity();

    while (x) {
        if (x % 2 == 1) {
            result = result * current;
        }
        current = current * current;
        x /= 2;
    }

    vector<int> state(3);
    state[0] = 3;
    state[1] = 0;
    state[2] = 0;
    int id = state_to_int[state];

    string answer = (result.a[id][0] ? "YES" : "NO");
    return answer;
}

int main() {
    preprocess();
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": " << solve() << "\n";
    }
    return 0;
}