#include <cstdio>
#include <cstring>

void Bsqrt(char* X, int lenA, char *QA, int& lenQA) {
    char Y[105], Z[55], A[55];
    int X_right_end = lenA;
    int X_pivot_left = 0;
    int X_pivot_right = 2;
    if(X_right_end % 2 != 0) {
        X_pivot_right = 1;
    }
    int Z_pivot_right = 2;
    int Z_pivot_left = 1;
    int Y_pivot_left = -1;
    int Y_pivot_right = -1;
    int A_right_end = 1;

    for(int i = 0; i < X_right_end; ++i) {
        X[i] -= '0';
    }
    for(int i = 0; i < 55; ++i) {
        Z[i] = 0;
    }

    do {
        for(int k = 9; k >= 0; --k) {
            Z[Z_pivot_right - 1] = k;
            int carry_num = 0, i, j;
            Y_pivot_right = X_pivot_right;
            for(i = Z_pivot_right - 1, j = Y_pivot_right - 1; i >= Z_pivot_left; --i, --j) {
                int mul = Z[i] * k + carry_num;
                carry_num = mul / 10;
                Y[j] = mul % 10;
            }
            if(carry_num != 0) {
                if(j < 0 || j < X_pivot_left) {
                    continue;
                } else if(j >= X_pivot_left) {
                    Y[j] = carry_num;
                    Y_pivot_left = j;
                    for(int zero = X_pivot_left; zero < Y_pivot_left; ++zero) {
                        Y[zero] = 0;
                    }
                }
            } else if(carry_num == 0) {
                if(j < X_pivot_left - 1) {
                    continue;
                } else if(j >= X_pivot_left - 1) {
                    Y_pivot_left = j + 1;
                    for(int zero = X_pivot_left; zero < Y_pivot_left; ++zero) {
                        Y[zero] = 0;
                    }
                }
            }
            bool X_bigger_than_Y = true;
            for(int i = X_pivot_left, j = X_pivot_left; i < X_pivot_right; ++i, ++j) {
                if(X[i] < Y[j]) {
                    X_bigger_than_Y = false;
                    break;
                } else if(X[i] > Y[j]) {
                    break;
                }
            }
            if(X_bigger_than_Y) {
                for(int i = X_pivot_right - 1; i >= X_pivot_left; --i) {
                    X[i] -= Y[i];
                    if(X[i] < 0) {
                        X[i] += 10;
                        X[i - 1] -= 1;
                    }
                }
                X_pivot_right += 2;
                Z[Z_pivot_right - 1] += k;
                int i, carry_num = 0;
                for(i = Z_pivot_right - 1; i >= Z_pivot_left; --i) {
                    if(Z[i] >= 10) {
                        Z[i] -= 10;
                        Z[i - 1] += 1;
                        carry_num = 1;
                    } else {
                        carry_num = 0;
                    }
                }
                if(carry_num != 0) {
                    Z_pivot_left -= 1;
                }
                Z[Z_pivot_right] = 0;
                Z_pivot_right += 1;
                while(X_pivot_left < X_pivot_right &&
                    (X_pivot_right - X_pivot_left) > (Z_pivot_right - Z_pivot_left)) {
                    if(X[X_pivot_left] == 0) {
                        ++X_pivot_left;
                    } else {
                        break;
                    }
                }
                A[A_right_end - 1] = (char)(k + '0');
                A_right_end += 1;
                break;
            } else {
                if(k == 0) {
                    X_pivot_right += 2;
                    Z[Z_pivot_right - 1] += k;
                    int i, carry_num = 0;
                    for(i = Z_pivot_right - 1; i >= Z_pivot_left; --i) {
                        if(Z[i] >= 10) {
                            Z[i] -= 10;
                            Z[i - 1] += 1;
                            carry_num = 1;
                        } else {
                            carry_num = 0;
                        }
                    }
                    if(carry_num != 0) {
                        Z_pivot_left -= 1;
                    }
                    Z[Z_pivot_right] = 0;
                    Z_pivot_right += 1;
                    while(X_pivot_left < X_pivot_right &&
                        (X_pivot_right - X_pivot_left) > (Z_pivot_right - Z_pivot_left)) {
                        if(X[X_pivot_left] == 0) {
                            ++X_pivot_left;
                        } else {
                            break;
                        }
                    }
                    A[A_right_end - 1] = (char)(k + '0');
                    A_right_end += 1;
                    break;
                }
            }
        }
    } while(X_pivot_right <= X_right_end);

    A[A_right_end - 1] = 0;
    for(int i = 0; i < A_right_end - 1; ++i) {
        QA[i] = A[i] - '0';
    }
    lenQA = A_right_end - 1;
}

bool less_than(char* MA, int beginMA, char* A, int lenA) {
    if(105 - beginMA < lenA) {
        return true;
    }
    if(105 - beginMA > lenA) {
        return false;
    }
    for(int i = beginMA, j = 0; j < lenA; ++i, ++j) {
        if(MA[i] < A[j]) {
            return true;
        } else if(MA[i] > A[j]) {
            return false;
        }
    }
    return false;
}

bool less_or_equal(char* MA, int beginMA, char* A, int beginA) {
    if(105 - beginMA < 105 - beginA) {
        return true;
    }
    if(105 - beginMA > 105 - beginA) {
        return false;
    }
    for(int i = beginMA, j = beginA; j < 105; ++i, ++j) {
        if(MA[i] < A[j]) {
            return true;
        } else if(MA[i] > A[j]) {
            return false;
        }
    }
    return true;
}

void Bsquare(char* A, int beginA, char* MA, int& beginMA) {
    int tmp[105] = {0};
    int b = (105 - beginA);
    b = 105 - (b * 2);
    for(int i = 104, k = 104; i >= beginA; --i, --k) {
        for(int j = 104, l = k; j >= beginA; --j, --l) {
            tmp[l] += (int)A[i] * (int)A[j];
        }
    }
    for(int i = 104; i >= b; --i) {
        if(tmp[i] >= 10) {
            tmp[i - 1] += tmp[i] / 10;
            tmp[i] = tmp[i] % 10;
        }

    }
    beginMA = 0;
    while(beginMA < 104 && tmp[beginMA] == 0) {
        ++beginMA;
    }
    for(int i = beginMA; i < 105; ++i) {
        MA[i] = (char)tmp[i];
    }
}

void Badd1(char* A, int& beginA) {
    A[104] += 1;
    for(int i = 104; i >= beginA; --i) {
        if(A[i] >= 10) {
            A[i - 1] += 1;
            A[i] -= 10;
        }
    }
    if(A[beginA - 1] != 0) {
        --beginA;
    }
}

bool isPalindrome(char* MA, int beginMA) {
    for(int i = beginMA, j = 104; i <= j; ++i, --j) {
        if(MA[i] != MA[j]) {
            return false;
        }
    }
    return true;
}

int main() {
    int T, cases = 0;
    scanf("%d", &T);
    while(T-- > 0) {
        printf("Case #%d: ", (++cases));
        char A[105], B[105], QA[105] = {0}, QB[105] = {0}, TMP_A[105], TMP_B[105];
        int lenA, lenB, lenQA, lenQB;
        scanf("%s%s", A, B);
        strcpy(TMP_A, A);
        strcpy(TMP_B, B);
        lenA = strlen(A);
        lenB = strlen(B);
        Bsqrt(TMP_A, lenA, QA, lenQA);
        Bsqrt(TMP_B, lenB, QB, lenQB);
        for(int i = 0; i < lenA; ++i) {
            A[i] -= '0';
        }
        for(int i = 0; i < lenB; ++i) {
            B[i] -= '0';
        }
        int beginQA = 104, beginQB = 104, beginMA = 104, beginMB = 104;
        for(int i = lenQA - 1; i >= 0 && beginQA >= 0; --i, --beginQA) {
            QA[beginQA] = QA[i];
            QA[i] = 0;
        }
        ++beginQA;
        for(int i = lenQB - 1; i >= 0 && beginQB >= 0; --i, --beginQB) {
            QB[beginQB] = QB[i];
            QB[i] = 0;
        }
        ++beginQB;
        char MA[105] = {0};
        Bsquare(QA, beginQA, MA, beginMA);
        if(less_than(MA, beginMA, A, lenA)) {
            Badd1(QA, beginQA);
        }
        int counter = 0;
        char MB[105] = {0};
        Bsquare(QB, beginQB, MB, beginMB);
        Bsquare(QA, beginQA, MA, beginMA);
        while(less_or_equal(MA, beginMA, MB, beginMB)) {
            if(isPalindrome(MA, beginMA) && isPalindrome(QA, beginQA)) {
                counter += 1;
            }
            Badd1(QA, beginQA);
            Bsquare(QA, beginQA, MA, beginMA);
        }
        printf("%d\n", counter);
    }
}
