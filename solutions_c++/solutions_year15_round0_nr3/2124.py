#include <iostream>
#include <string>

#define LIM 10001
#define N_STATES 3

#define IJK_STATE 0
#define JK_STATE 1
#define K_STATE 2

#define POSI 0
#define NEGI 1
#define ONE 0
#define I 1
#define J 2
#define K 3

using namespace std;

typedef struct quat{
    int sign, value;
} Quat;

Quat lookup[4][4];
int mem[LIM][N_STATES];

void setup() {
    for (int i = 0; i < LIM; i++)
	for (int j = 0; j < N_STATES; j++)
	    mem[i][j] = -1;
    lookup[ONE][ONE] = (Quat){POSI, ONE};
    lookup[ONE][I] = (Quat){POSI, I};
    lookup[ONE][J] = (Quat){POSI, J};
    lookup[ONE][K] = (Quat){POSI, K};
    lookup[I][1] = (Quat){POSI, I};
    lookup[I][I] = (Quat){NEGI, ONE};
    lookup[I][J] = (Quat){POSI, K};
    lookup[I][K] = (Quat){NEGI, J};
    lookup[J][ONE] = (Quat){POSI, J};
    lookup[J][I] = (Quat){NEGI, K};
    lookup[J][J] = (Quat){NEGI, ONE};
    lookup[J][K] = (Quat){POSI, I};
    lookup[K][ONE] = (Quat){POSI, K};
    lookup[K][I] = (Quat){POSI, J};
    lookup[K][J] = (Quat){NEGI, I};
    lookup[K][K] = (Quat){NEGI, ONE};
}

Quat mult(Quat a, Quat b) {
    Quat r = lookup[a.value][b.value];
    r.sign = (a.sign+b.sign+r.sign) % 2;
    return r;
}

Quat from_char(char a) {
    if (a == 'i')
	return (Quat){POSI, I};
    if (a == 'j')
	return (Quat){POSI, J};
    if (a == 'k')
	return (Quat){POSI, K};
    printf("Bad Letter\n");
    exit(1);
    return (Quat){0, 0};
}

void print_quat(Quat a) {
    string v = a.sign == NEGI ? "-" : "";
    if (a.value == I) v += "i";
    if (a.value == J) v += "j";
    if (a.value == K) v += "k";
    if (a.value == ONE) v += "1";
    cout << v << endl;
}

int is_quat(Quat a, int aa) {
    return a.sign == POSI && a.value == aa;
}

int is_rest_k(int index, string &pattern) {
    Quat r = from_char(pattern[index]);
    for (int i = index+1; i < pattern.size(); i++)
	r = mult(r, from_char(pattern[i]));
    return r.sign == POSI && r.value == K;
}

int next_state(int IJK) {
    if (IJK == IJK_STATE) return JK_STATE;
    if (IJK == JK_STATE) return K_STATE;
    printf("Bad State\n");
    exit(1);
    return -1;
}

int target_value(int IJK) {
    if (IJK == IJK_STATE) return I;
    if (IJK == JK_STATE) return J;
    printf("Bad State\n");
    exit(1);
    return -1;
}

int can_solve(int index, string &pattern, int IJK) {
    if (mem[index][IJK] != -1) 	return mem[index][IJK];
    if (index >= pattern.size()) return 0;
    Quat r = from_char(pattern[index]);
    if (IJK == IJK_STATE || IJK == JK_STATE) {
	for (int i = index+1; i < pattern.size(); i++) {
	    if (is_quat(r, target_value(IJK)) && can_solve(i, pattern, next_state(IJK)) == 1) {
		mem[index][IJK] = 1;
		return 1;
	    }
	    //print_quat(r);
	    r = mult(r, from_char(pattern[i]));
	}
	mem[index][IJK] = 0;
	return 0;
    }
    else {
	mem[index][IJK] = is_rest_k(index, pattern);
	return mem[index][IJK];
    }
}

int main(void) {
    int n_cases;
    cin >> n_cases;
    for (int i = 0; i < n_cases; i++) {
	setup();
	int sz, rep;
	string pattern, tot_pattern="";
	cin >> sz >> rep;
	cin >> pattern;
	for (int i = 0; i < rep; i++)
	    tot_pattern += pattern;
	int answer = can_solve(0, tot_pattern, IJK_STATE);
	string resp = answer == 1 ? "YES" : "NO";
	cout << "Case #" << i+1 << ": " << resp << endl;
    }
}
