#include <bits/stdc++.h>
using namespace std;

#define READ(in)      freopen(in,"r",stdin)
#define WRITE(out)    freopen(out,"w",stdout)

#define FOR(i, s, e)  for(int i=s; i<=e; i++)
#define FOREACH(i,n)  for(__typeof(n.begin()) i=n.begin();i!=n.end();i++)
#define SCI(x) scanf("%d", &x)
#define SCII(x, y) scanf("%d %d", &x, &y)
#define SCIII(x, y, z) scanf("%d %d %d", &x, &y, &z)

#define SET(x, y) memset(x, y, sizeof(x))

#define pb            push_back
#define mp            make_pair
#define ff            first
#define ss            second

#define DB(x)         cerr << #x << " = " << x << endl;

#define MOD(x) x%10000007
#define MAX (long long unsigned) (1e18) + 7

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int multiply(int x, int y){
    int ret, neg = 1;
    if(x*y<0) neg = -1;

    x = fabs(x);
    y = fabs(y);
    if(x==1){
        ret = y;
    }
    else if(x=='i'){
        if(y=='1') ret = x;
        else if(y=='i') ret = -1;
        else if(y=='j') ret = 'k';
        else if(y=='k') ret = -1 * 'j';
    }
    else if(x=='j'){
        if(y=='1') ret = x;
        else if(y=='i') ret = -1*'k';
        else if(y=='j') ret = -1;
        else if(y=='k') ret = 'i';
    }
    else if(x=='k'){
        if(y=='1') ret = x;
        else if(y=='i') ret = 'j';
        else if(y=='j') ret = -1*'i';
        else if(y=='k') ret = -1;
    }

    return neg*ret;
}

int power(int x, int n){
    if(x==1) return 1;
    else if(x==-1){
        if(n%2) return -1;
        else return 1;
    }
    else{
        n %= 4;
        if(n==0) return 1;
        else if(n==1) return x;
        else if(n==2) return -1;
        else return -x;
    }
}

int main()
{
    READ("in.txt");
    WRITE("out.txt");
    ios_base::sync_with_stdio(false);

    int t, l, x, kase=1;
    string str;
    cin >> t;
    while(t--){
        cin >> l >> x >> str;

        map<char, bool> instr;
        int fir=1, cnt=0;

        for(int i=0; i<str.size(); i++){
            if(!instr[str[i]]){
                cnt++;
                instr[str[i]] = true;
            }
            fir = multiply(fir, str[i]);
        }

        if(cnt > 1 && multiply(fir, power(fir, x-1)) == -1){
            bool foundi = false, foundj = false;
            //cout << "endtered\n";
            fir = 1;
            //DB(x);
            while(x--){
                for(int i=0; i<str.size(); i++){
                    fir = multiply(fir, str[i]);
                    //cout << (char) fir << endl;
                    if(!foundi){
                        if(fir == 'i'){
                            foundi = true;
                            fir = 1;
                        }
                    }
                    else if(!foundj){
                        if(fir == 'j'){
                            foundj = true;
                            break;
                        }
                    }
                }
                if(foundi && foundj) break;
            }
            if(foundi && foundj) printf("Case #%d: YES\n", kase++);
            else printf("Case #%d: NO\n", kase++);
        }

        else{
            printf("Case #%d: NO\n", kase++);
        }

    }

    fclose(stdin);
    fclose (stdout);
    return 0;
}
