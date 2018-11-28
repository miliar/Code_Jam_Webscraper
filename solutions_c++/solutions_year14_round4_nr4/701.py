#include <bits/stdc++.h>

#define rep(i,a,b) for(int i = a; i < (int)b; i++)
#define rep0(i,b) rep(i,0,b)
#define repn(i,a,b) for(int i = b-1; i >= (int)a; i--)
#define repn0(i,b) repn(i,0,b)
#define clr(arr, set) rep0(j, sizeof(arr) / sizeof(arr[0])) arr[j] = set
#define inf (int)0x7FFFFFFF
typedef long long LL;
using namespace std;


template<typename T>
vector<T> vget(int n)
{
    int pb;
    vector<T> ret;
    rep0(i, n)
    {
        cin >> pb;
        ret.push_back(pb);
    }
    return ret;
}


void init()
{

}


string solve()
{
    int N, M;
    cin >> M >> N;
    vector<string> vals;
    rep0(i, M)
    {
        string s;
        cin >> s;
        vals.push_back(s);
    }

    rep0(i, N) cout << vals[i] << ",";
    cout << endl;

    cout << N << "," << M << endl << endl;

    int bits = M * 2;
    vector<int> serv(M, 0);

    cout << bits << " " << (1 << (bits-1)) << endl;
    cout << endl;

    set<int> seen;

    int cnt = 0;
    int ret = 0;
    rep0(bm, 1 << (bits))
    {
        int bad = 0;
        int hsh = 0;
        rep0(i, M)
        {
            int s = (bm >> (i*2)) & 3;
            if(s >= N)
            {
                bad == 1;
                break;
            }
            serv[i] = s;
            hsh += s << (i*2);
        }
        if(bad)
            continue;
        if(seen.count(hsh))
            continue;
        seen.insert(hsh);

/*
        cout << endl << endl;
        rep0(i, M)
            cout << serv[i] << ",";
        cout << endl;
*/
        int tot = 0;
        rep0(i, N)
        {
            set<string> pref;

            rep0(j, M)
            {
                if(serv[j] != i) continue;
                string s = vals[j];
                rep0(k, s.size())
                {
                    pref.insert(s.substr(0, k+1));
                    //cout << "server" << i << " " << s.substr(0, k+1) << endl;
                }
            }

            tot += pref.size();
            if(pref.size() != 0)
                tot++;
            //cout << "server" << i << " total:" << pref.size() + 1 << endl;

        }
        //cout << "for all" << tot << endl;
        if(tot > ret)
        {
            ret = tot;
            cnt = 1;
        }
        else if(tot == ret)
            cnt ++;



    }


    char sret[10000];
    sprintf(sret, "%i %i", ret, cnt);
    return sret;
}

int main()
{
    char let = 'D';
	int run = 1;


    char fin[1000];
    if(run == 0) sprintf(fin, "infile.txt");
    else if(run == 1) sprintf(fin, "Z:\\Users\\John Cornwell\\Desktop\\%c-small-attempt0.in", let);
    else if(run == 2) sprintf(fin, "Z:\\Users\\John Cornwell\\Desktop\\%c-large.in", let);

    freopen(fin, "r", stdin);


    ofstream outf;
    outf.open("out.txt");

    init();

    string line;
    int num;
    cin >> num;

    cout << num << " Test Cases" << endl;
    rep0(i, num)
    {
        string ret = solve();
        outf << "Case #" << (i+1) << ": " << ret << endl;
        cout << "Case #" << (i+1) << ": " << ret << endl;
    }
    outf.close();

}
