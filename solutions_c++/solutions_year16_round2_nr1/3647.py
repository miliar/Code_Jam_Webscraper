#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>
#include <utility>
#include <map>
#define FOR(i, a, b) for(int i = (a); i < (b); ++i)
typedef long long ll;
#define ALL(a) (a).begin(),(a).end()
using namespace std;

string num[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

bool makeNumber(int prev, vector<int>& cnt, string& made)
{
    bool allZero = true;
    FOR(i,0,26)
    {
        if (cnt[i] != 0)
        {
            allZero = false;
            break;
        }
    }

    if (allZero)
        return true;

    FOR(i,prev, 10)
    {
        string numStr = num[i];
        bool finded = true;
//        vector<int> v;

        vector<int> cntCp = cnt;

        FOR(j,0,numStr.length())
        {
            int idx = numStr[j] - 'A';
            
            if (cntCp[idx] == 0)
            {
                finded = false;
                break;
            }
            else
                cntCp[idx]--;
        }

        if (finded)
        {
            made.push_back(i + '0');
            if (makeNumber(i, cntCp, made))
                return true;
            made.pop_back();
        }

    }
    return false;
}

int main()
{

	FILE* fin = freopen("in.txt","rt", stdin);
    FILE* fout = freopen("out.txt","wt", stdout);
	int c;
	scanf("%d",&c);

    //char cnt[26];
    //memset(cnt, 0, sizeof(cnt));
    //FOR(i,0,10)
    //{
    //    FOR(j,0,num[i].length())
    //    {
    //        cnt[num[i][j]-'A']++;
    //    }
    //}

    //FOR(i,0,26)
    //{
    //    if (cnt[i] == 1)
    //        printf("%c : %d\n", i+'A',cnt[i]);
    //}

    

	FOR(xx,0,c)
	{
        char t[2100];
        vector<int> cnt(26, 0);
        memset(t, 0, sizeof(t));
        scanf("%s", t);
        string s = t;
        string ret;

        FOR(i,0,s.length())
            cnt[s[i]-'A']++;

        if (makeNumber(0, cnt, ret))
            printf("Case #%d: %s\n", xx+1, ret.c_str());
    }

    fclose(fout);
	fclose(fin);

	return 0;
}