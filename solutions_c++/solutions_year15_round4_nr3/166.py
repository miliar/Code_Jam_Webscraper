#define TASKNAME "text"

#include <bits/stdc++.h>

#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define sz(a) (int)a.size()
#define fst first
#define snd second
#define y1 osrughosduvgarligybakrybrogvba
#define y0 aosfigdalrowgyalsouvgrlvygalri                               
#define mp make_pair
#define pb push_back
#define eprintf(...) fprintf(stderr, __VA_ARGS__)
 
using namespace std;
 
typedef int ll;
typedef long double ld;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef vector <bool> vb;
typedef vector <ll> vll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <int, ll> pil;
typedef vector <pii> vpii;

template <typename T>
T sqr(T x) {
    return x * x;
}

template <typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

const double EPS = 1e-9;
const int INF = 1e9;
const ll INFLONG = (ll)1e18;

const ll p = 239017;

void parseWords(string const& s, vector<ll> &words) {
    int i = 0;
    //string word = "";
    ll h = 0;
    while (i < sz(s)) {
        while (i < sz(s) && isalpha(s[i])) {
            h = h * p + s[i++];
            //word += s[i++];
        }
        //words.pb(word);
        //word = "";
        words.pb(h);
        h = 0;
        i++;
    }
}

ll hash(string const& s) {
    ll h = 0;
    for (int i = 0; i < sz(s); i++) {
        h = h * p + s[i];
    }
    return h;
}

int main()
{
    freopen(TASKNAME".in", "r", stdin);
    freopen(TASKNAME".out", "w", stdout);
    int testsCount;
    scanf("%d", &testsCount);
    for (int testNumber = 1; testNumber <= testsCount; ++testNumber) {
        printf("Case #%d: ", testNumber);
        fprintf(stderr, "Running %d\n", testNumber);
        int n;
        scanf("%d ", &n);
        string s;
        vector<ll> english, french;
        multiset<ll> englishWords, frenchWords;
        getline(cin, s);
        parseWords(s, english);
        getline(cin, s);
        parseWords(s, french);

        vector<vector<ll>> sentences;
        for (int i = 0; i < n - 2; i++) {
            getline(cin, s);
            sentences.push_back(vector<ll>());
            parseWords(s, sentences.back());
        }
        int minAns = INF;

        englishWords.clear();
        frenchWords.clear();
        for (int it = 0; it < sz(english); it++) {
            englishWords.insert(english[it]);
        }
        for (int it = 0; it < sz(french); it++) {
            frenchWords.insert(french[it]);
        }
        set<ll> both;
        for (ll s : englishWords) {
            if (frenchWords.find(s) != frenchWords.end()) {
                both.insert(s);
            }
        }

        set<ll> ans = both;
        for (int msk = 0; msk < (1 << (n - 2)); msk++) {
            set<ll> newEnglish, newFrench;
            for (int i = 0; i < n - 2; i++) {
                if (msk & (1 << i)) {
                    for (int it = 0; it < sz(sentences[i]); it++) {
                        newEnglish.insert(sentences[i][it]);  
                    }
                } else {
                    for (int it = 0; it < sz(sentences[i]); it++) {
                        newFrench.insert(sentences[i][it]);
                    }
                }
            }
            vector<ll> inserted;
            for (set<ll>::iterator it = newEnglish.begin(); it != newEnglish.end(); ++it) {
                ll s = *it;
                if ((frenchWords.find(s) != frenchWords.end() || newFrench.find(s) != newFrench.end()) && ans.find(s) == ans.end()) {
                    ans.insert(s);
                    inserted.pb(s);
                    if (sz(ans) >= minAns) {
                        break;
                    }
                }
            }
            for (set<ll>::iterator it = newFrench.begin(); it != newFrench.end(); ++it) {
                ll s = *it;
                if ((englishWords.find(s) != englishWords.end() || newEnglish.find(s) != newEnglish.end()) && ans.find(s) == ans.end()) {
                    ans.insert(s);
                    inserted.pb(s);
                    if (sz(ans) >= minAns) {
                        break;
                    }
                }
            }
            minAns = min(minAns, sz(ans));
            for (int i = 0; i < sz(inserted); i++) {
                ans.erase(inserted[i]);
            }
        }
        printf("%d\n", minAns);
    }          
    return 0;
}