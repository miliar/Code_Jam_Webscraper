#include <iostream>
#include <vector>
#include <string>

//#include <gmpxx.h>

using namespace std;

static vector< vector<int> > cols, acols;
static vector<bool> srows, scols;
static vector<int> unknownFill;

template <typename T> inline bool isInSortedVector(T el, const vector<T> &vec) {
    return *lower_bound(vec.cbegin(), vec.cend(), el) == el;
}

template <typename T> inline int positionInSortedVector(T el, const vector<T> &vec) {
    return (int) (lower_bound(vec.cbegin(), vec.cend(), el) - vec.cbegin());
}

template <typename T> inline bool isInVector(T el, const vector<T> &vec) {
    for (const T &el2 : vec) {
        if (el2 == el)
            return true;
    }
    return false;
}

template <typename T> inline int positionInVector(T el, const vector<T> &vec) {
    for (int i = vec.size(); i-- > 0;) {
        if (vec[i] == el)
            return i;
    }
    return -1;
}

bool addList(const vector< vector<int> > &input, int N, int index, bool hasRow) {
    if (index >= input.size())
        return true;
    /* Try row */
    if (hasRow) {
        for (int k, i = 0; i < N; ++i) {
            if (srows[i])
                continue;
            for (k = N; k-- > 0;) {
                if (!acols[k][i])
                    continue;
                if (acols[k][i] > input[index][k])
                    goto tryCol;
                if (acols[k][i] < input[index][k])
                    break;
            }
            if (k < 0) {
                vector<int> backup;
                backup.reserve(N);
                for (k = 0; k < N; ++k) {
                    backup.push_back(acols[k][i]);
                    acols[k][i] = input[index][k];
                }
                srows[i] = true;
                if (addList(input, N, index + 1, true))
                    return true;
                srows[i] = false;
                for (k = N; k-- > 0;)
                    acols[k][i] = backup[k];
                goto tryCol;
            }
        }
    } else {
        for (int k, i = 0; i < N; ++i) {
            if (srows[i])
                continue;
            for (k = cols.size(); k-- > 0;) {
                if (!isInSortedVector(cols[k][i], input[index]))
                    break;
            }
            if (k < 0) {
                for (k = N; k-- > 0;) {
                    acols[k] = unknownFill;
                    acols[k][i] = input[index][k];
                }
                for (k = cols.size(); k-- > 0;) {
                    int pos = positionInSortedVector(cols[k][i], input[index]);
                    acols[pos] = cols[k];
                    scols[pos] = true;
                }
                srows[i] = true;
                if (addList(input, N, index + 1, true))
                    return true;
                srows[i] = false;
                scols.clear();
                scols.resize(N, false);
            }
        }
    }
tryCol:
    /* Try column */
    if (hasRow) {
        for (int i, k = 0; k < N; ++k) {
            if (scols[k])
                continue;
            for (i = N; i-- > 0;) {
                if (acols[k][i]) {
                    if (acols[k][i] < input[index][i])
                        break;
                    if (acols[k][i] > input[index][i])
                        return false;
                } else {
                    int j = k + 1;
                    while ((j < N) && (!acols[j][i]))
                        ++j;
                    if ((j < N) && (acols[j][i] - (j - k) < input[index][i]))
                        break;
                }
            }
            if (i < 0) {
                vector<int> backup;
                backup.reserve(N);
                for (i = 0; i < N; ++i) {
                    backup.push_back(acols[k][i]);
                    acols[k][i] = input[index][i];
                }
                scols[k] = true;
                if (addList(input, N, index + 1, true))
                    return true;
                scols[k] = false;
                for (i = N; i-- > 0;)
                    acols[k][i] = backup[i];
                break;
            }
        }
    } else {
        for (int i, k = 0; k < cols.size(); ++k) {
            int fg = 0;
            for (i = N; i-- > 0;) {
                if (cols[k][i] < input[index][i])
                    fg |= 1;
                if (cols[k][i] > input[index][i])
                    fg |= 2;
            }
            switch (fg)
            {
            case 0:
            case 3:
                return false;
            case 2:
            {
                auto pos = cols.begin() + k;
                cols.insert(pos, input[index]);
                if (addList(input, N, index + 1, false))
                    return true;
                cols.erase(pos);
                return false;
            }
            case 1:
            default:
                break;
            }
        }
        auto pos = cols.end();
        cols.insert(pos, input[index]);
        if (addList(input, N, index + 1, false))
            return true;
        cols.erase(pos);
    }
    return false;
}

int main() {
    int T;
    cin >> T;
    vector< vector<int> > input;
    vector<int> lst;
    for (int i = 0; i < T;) {
        int N, tmp;
        cin >> N;
        cols.clear();
        srows.resize(0);
        srows.resize(N, false);
        scols.resize(0);
        scols.resize(N, false);
        acols.clear();
        acols.resize(N);
        input.clear();
        unknownFill.resize(N, 0);
        for (int j = (N << 1); --j > 0;) {
            for (int k = N; k-- > 0;) {
                cin >> tmp;
                lst.push_back(tmp);
            }
            input.push_back(lst);
            lst.clear();
        }
        cols.push_back(input[input.size() - 1]);
        input.pop_back();
        if (!addList(input, N, 0, false)) {
            cerr << "Error: No solution." << endl;
            return 0;
        }
        if (isInVector(false, scols)) {
            lst = acols[positionInVector(false, scols)];
        } else {
            int pos = positionInVector(false, srows);
            lst.reserve(N);
            for (int j = 0; j < N; ++j)
                lst.push_back(acols[j][pos]);
        }
        cout << "Case #" << (++i) << ":";
        for (int j = 0; j < N; ++j)
            cout << " " << lst[j];
        lst.clear();
        cout << endl;
    }
    return 0;
}
