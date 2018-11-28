///*********************************
///***Author: Nguyen The Thong
///***Email: nguyenthethong1996@gmail.com
///*********************************

#include <bits/stdc++.h>
using namespace std;

#define fto(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define fdw(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define read(a) scanf("%d", &a)
#define write(a) printf("%d", a)
#define read64(a) scanf("%I64d", &a);
#define write64(a) printf("%I64d", a);
#define debug(a) cout << #a << " = " << a << endl
#define ooLL 1000000000000LL
#define oo 1000000000
#define maxn 100005
#define eps 0.000000001

#define sz(a) int((a).size())
#define all(c) (c).begin(), (c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define pb push_back
#define mp make_pair

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef long long ll;

int GCD(int a, int b){return(b==0?a:GCD(b,a%b));}
int LCM(int a, int b){return a*(b/GCD(a,b));}

int numtest, times, dir;
char s[maxn];

int main() {
    freopen("B-large.in","r",stdin);
    freopen("ou.out","w",stdout);

    scanf("%d", &numtest);   getchar();
    for(int test = 1; test <= numtest; test++) {
        gets(s);


        times = 0;
        if (s[0] == '+') dir = 1; else dir = -1;
        for(int i = 0; i < strlen(s)-1; i++) {
            if (s[i] != s[i+1]) {
                times++;
                if (s[i+1] == '+') dir = 1; else dir = -1;
            }
        }
        if (dir == -    1) times++;
        printf("Case #%d: %d\n", test, times);
    }
}

///Copyright by NguyenTheThong
