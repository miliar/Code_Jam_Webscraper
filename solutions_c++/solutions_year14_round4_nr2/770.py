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
    int N;
    int ret = 0;
    cin >> N;
    vector<int> vals = vget<int>(N);
    vector<int> st = vals;
    vector<int> nvals = vals;
    sort(st.begin(), st.end());

    rep0(i, N)
    {
        rep0(j, N)
        {
            if(st[i] == vals[j])
                nvals[j] = i;
        }
    }
    //rep0(i, N) cout << vals[i] << ",";
    //cout << endl;
    //rep0(i, N) cout << nvals[i] << ",";
    //cout << endl;

    int la = 0;
    int ra = N-1;

    rep0(p, N)
    {
        rep0(i, N)
        {
            if(nvals[i] == p)
            {
                int dl = i - la;
                int dr = ra - i;

                if(dl < dr)
                {
                    while(i > la)
                    {
                        swap(nvals[i], nvals[i-1]);
                        i--;
                        ret++;
                    }
                    la++;
                }
                else
                {
                    while(i < ra)
                    {
                        swap(nvals[i], nvals[i+1]);
                        i++;
                        ret ++;
                    }
                    ra--;
                }

                break;
            }
        }
    }

    //rep0(i, N) cout << nvals[i] << ",";
    //cout << endl;

    char sret[10000];
    sprintf(sret, "%i", ret);
    return sret;
}

int main()
{
    char let = 'B';
	int run = 2;


    char fin[1000];
    if(run == 0) sprintf(fin, "infile.txt");
    else if(run == 1) sprintf(fin, "Z:\\Users\\John Cornwell\\Desktop\\%c-small-attempt2.in", let);
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
