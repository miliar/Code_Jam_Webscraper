/*#include <fstream>
#include <cstring>

using namespace std;
typedef long long ll;

const int MAXL = 10100;
const ll INF = 1LL<<60;

int T, l, a[MAXL];
int dpb[MAXL], dpe[MAXL];
ll mnb[MAXL], mne[MAXL];
char s[MAXL]; ll x;

int mul(int a, int b){
    static int MUL[5][5];
    MUL[1][1] = 1, MUL[1][2] = 2, MUL[1][3] = 3, MUL[1][4] = 4;
    MUL[2][1] = 2, MUL[2][2] = -1, MUL[2][3] = 4, MUL[2][4] = -3;
    MUL[3][1] = 3, MUL[3][2] = -4, MUL[3][3] = -1, MUL[3][4] = 2;
    MUL[4][1] = 4, MUL[4][2] = 3, MUL[4][3] = -2, MUL[4][4] = -1;
    int sign = 1;
    if(a < 0) sign *= -1, a = -a;
    if(b < 0) sign *= -1, b = -b;
    return sign*MUL[a][b];
}

int div(int a, int b){
    static int DIV[5][5];
    DIV[1][1] = 1, DIV[1][2] = -2, DIV[1][3] = -3, DIV[1][4] = -4;
    DIV[2][1] = 2, DIV[2][2] = 1, DIV[2][3] = 4, DIV[2][4] = -3;
    DIV[3][1] = 3, DIV[3][2] = -4, DIV[3][3] = 1, DIV[3][4] = 2;
    DIV[4][1] = 4, DIV[4][2] = 3, DIV[4][3] = -2, DIV[4][4] = 1;
    int sign = 1;
    if(a < 0) sign *= -1, a = -a;
    if(b < 0) sign *= -1, b = -b;
    return sign*DIV[a][b];
}

int div2(int a, int b){
    static int DIV[5][5];
    DIV[1][1] = 1, DIV[1][2] = -2, DIV[1][3] = -3, DIV[1][4] = -4;
    DIV[2][1] = 2, DIV[2][2] = 1, DIV[2][3] = -4, DIV[2][4] = 3;
    DIV[3][1] = 3, DIV[3][2] = 4, DIV[3][3] = 1, DIV[3][4] = -2;
    DIV[4][1] = 4, DIV[4][2] = -3, DIV[4][3] = 2, DIV[4][4] = 1;
    int sign = 1;
    if(a < 0) sign *= -1, a = -a;
    if(b < 0) sign *= -1, b = -b;
    return sign*DIV[a][b];
}

int exp(int b, int e){
    int res = 1;
    while(e){
        if(e&1) res = mul(res, b);
        e >>= 1;
        b = mul(b, b);
    }
    return res;
}

int main(){
    ifstream cin("C:\\Users\\user\\Downloads\\C-small-attempt0.in");
    ofstream cout("C:\\Users\\user\\Downloads\\ijk0_.out");
    cin >> T; for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        cin >> l >> x;
        cin >> s;
        for(int i = 0; i < l; i++)
            a[i] = (s[i] == 'i' ? 2: s[i] == 'j' ? 3: 4);
        dpb[0] = a[0]; dpe[l-1] = a[l-1];
        for(int i = 1; i < l; i++)
            dpb[i] = mul(dpb[i-1], a[i]);
        for(int i = l-2; i >= 0; i--)
            dpe[i] = mul(a[i], dpe[i+1]);
        if(exp(dpb[l-1], x) != -1){
            cout << "NO\n";
            continue;
        }
        ll mb = INF, me = INF;
        for(int i = 0; i < l; i++){
            int m = div(2, dpb[i]);
            //cout << m << '\n';
            if(m == 1) mnb[i] = 0;
            else if(m == dpb[l-1]) mnb[i] = 1;
            else if(m == exp(dpb[l-1],2)) mnb[i] = 2;
            else if(m == exp(dpb[l-1],3)) mnb[i] = 3;
            else mnb[i] = INF;
            mb = min(mb, mnb[i]*l+i+1);
        }
        for(int i = l-1; i >= 0; i--){
            int m = div2(4, dpe[i]);
            if(m == 1) mne[i] = 0;
            else if(m == dpb[l-1]) mne[i] = 1;
            else if(m == exp(dpb[l-1],2)) mne[i] = 2;
            else if(m == exp(dpb[l-1],3)) mne[i] = 3;
            else mne[i] = INF;
            me = min(me, mne[i]*l+(l-1-i)+1);
        }
        if((mb+me) < (long long)(l)*(long long)x) cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}
*/#include <fstream>
#include <string>
using namespace std;

int T, l ,x;
int a[10010], dpb[10010];
string s, s_;

int mul(int a, int b){
    static int MUL[5][5];
    MUL[1][1] = 1, MUL[1][2] = 2, MUL[1][3] = 3, MUL[1][4] = 4;
    MUL[2][1] = 2, MUL[2][2] = -1, MUL[2][3] = 4, MUL[2][4] = -3;
    MUL[3][1] = 3, MUL[3][2] = -4, MUL[3][3] = -1, MUL[3][4] = 2;
    MUL[4][1] = 4, MUL[4][2] = 3, MUL[4][3] = -2, MUL[4][4] = -1;
    int sign = 1;
    if(a < 0) sign *= -1, a = -a;
    if(b < 0) sign *= -1, b = -b;
    return sign*MUL[a][b];
}

int main() {
    ifstream cin("C:\\Users\\user\\Downloads\\C-small-attempt6.in");
    ofstream cout("C:\\Users\\user\\Downloads\\ijk.out");
	cin >> T; for(int t = 1; t <= T; t++){
		s.clear();
		bool f = 0, g = 0;
        cout << "Case #" << t << ": ";
        cin >> l >> x;
        cin >> s; l *= x;
        s_ = s;
		while(--x) s += s_;
        for(int i = 0; i < l; i++)
            a[i] = (s[i] == 'i' ? 2: s[i] == 'j' ? 3: 4);
		dpb[0] = a[0]; if(dpb[0] == 2) f = true;
        for(int i = 1; i < l; i++){
            dpb[i] = mul(dpb[i-1], a[i]);
			if(dpb[i] == 2) f = true;
			else if(dpb[i] == 4 and f) g = true;
		}
		if(dpb[l-1] == -1 and f and g) cout << "YES\n";
		else cout << "NO\n";
	}
	return 0;
}

