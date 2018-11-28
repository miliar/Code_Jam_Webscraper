
/*
 *Aditya Gourav @ adi.pearl
 */
#include<bits/stdc++.h>
using namespace std;

///debugging
struct debugger{template<typename T> debugger& operator,(const T& v){cerr<<v<<" ";return *this;}}dbg;
#define db(args...) do {dbg,args; cerr << endl;} while(0)

#define R(f) freopen(f,"r",stdin);
#define W(f) freopen(f,"w",stdout);
#define TEST int num_cases; cin>>num_cases;for(int case_id=1;case_id <= num_cases;++case_id)

typedef unsigned long long ull;

/** Main Code starts here :) **/
int cnt[26] = {0};

int getNoDigits(int digit){
    int a,b,c,d,e,f;
    switch(digit){
    case 0:
        a = cnt['Z'-'A'];
        b = cnt['E'-'A'];
        c = cnt['R'-'A'];
        d = cnt['O'-'A'];
        return min(a,min(b,min(c,d)));
    case 1:
        a = cnt['O'-'A'];
        b = cnt['N'-'A'];
        c = cnt['E'-'A'];
        return min(a, min(b,c));
    case 2:
        a = cnt['T'-'A'];
        b = cnt['W'-'A'];
        c = cnt['O'-'A'];
        return min(a, min(b,c));
    case 3:
        a = cnt['T'-'A'];
        b = cnt['H'-'A'];
        c = cnt['R'-'A'];
        d = cnt['E'-'A'];
        return min(a,min(b,min(c,d/2)));
    case 4:
        a = cnt['F'-'A'];
        b = cnt['O'-'A'];
        c = cnt['U'-'A'];
        d = cnt['R'-'A'];
        return min(a,min(b,min(c,d)));
    case 5:
        a = cnt['F'-'A'];
        b = cnt['I'-'A'];
        c = cnt['V'-'A'];
        d = cnt['E'-'A'];
        return min(a,min(b,min(c,d)));
    case 6:
        a = cnt['S'-'A'];
        b = cnt['I'-'A'];
        c = cnt['X'-'A'];
        return min(a,min(b,c));
    case 7:
        a = cnt['S'-'A'];
        b = cnt['E'-'A'];
        c = cnt['V'-'A'];
        d = cnt['N'-'A'];
        return min(a,min(b/2,min(c,d)));
    case 8:
        a = cnt['E'-'A'];
        b = cnt['I'-'A'];
        c = cnt['G'-'A'];
        d = cnt['H'-'A'];
        e = cnt['T'-'A'];
        return min(a,min(b,min(c,min(d,e))));
    case 9:
        a = cnt['N'-'A'];
        b = cnt['I'-'A'];
        c = cnt['E'-'A'];
        return min(a/2,min(b,c));
    }
}

void decrement(int i, int c){
    switch(i){
    case 0:
        cnt['Z'-'A'] -= c;
        cnt['E'-'A'] -= c;
        cnt['R'-'A'] -= c;
        cnt['O'-'A'] -= c;
        break;
    case 1:
        cnt['O'-'A'] -= c;
        cnt['N'-'A'] -= c;
        cnt['E'-'A'] -= c;
        break;
    case 2:
        cnt['T'-'A'] -= c;
        cnt['W'-'A'] -= c;
        cnt['O'-'A'] -= c;
        break;
    case 3:
        cnt['T'-'A'] -= c;
        cnt['H'-'A'] -= c;
        cnt['R'-'A'] -= c;
        cnt['E'-'A'] -= 2*c;
        break;
    case 4:
        cnt['F'-'A'] -= c;
        cnt['O'-'A'] -= c;
        cnt['U'-'A'] -= c;
        cnt['R'-'A'] -= c;
        break;
    case 5:
        cnt['F'-'A'] -= c;
        cnt['I'-'A'] -= c;
        cnt['V'-'A'] -= c;
        cnt['E'-'A'] -= c;
        break;
    case 6:
        cnt['S'-'A'] -= c;
        cnt['I'-'A'] -= c;
        cnt['X'-'A'] -= c;
        break;
    case 7:
        cnt['S'-'A'] -= c;
        cnt['E'-'A'] -= 2*c;
        cnt['V'-'A'] -= c;
        cnt['N'-'A'] -= c;
        break;
    case 8:
        cnt['E'-'A'] -= c;
        cnt['I'-'A'] -= c;
        cnt['G'-'A'] -= c;
        cnt['H'-'A'] -= c;
        cnt['T'-'A'] -= c;
        break;
    case 9:
        cnt['N'-'A'] -= 2*c;
        cnt['I'-'A'] -= c;
        cnt['E'-'A'] -= c;
        break;
    }
}

#define SUBMIT

int main(){

    #ifdef SUBMIT
    R("A-large.in");
    W("A-l.txt");
    #endif

    #ifdef SAMPLE
    R("example_input.txt");
    #endif



    TEST{
        string s;
        cin >> s;

        for(int i = 0; i < 26; ++i)
            cnt[i] = 0;
        for(int i = 0; i < s.length(); ++i){
            cnt[s[i] - 'A']++;
        }

        vector<pair<int, int>> res;
        if(cnt['Z'-'A'] > 0){
            int c = getNoDigits(0);
            res.push_back(make_pair(0,c));
            decrement(0, c);
        }
        if(cnt['W'-'A'] > 0){
            int c = getNoDigits(2);
            res.push_back(make_pair(2,c));
            decrement(2, c);
        }
        if(cnt['U'-'A'] > 0){
            int c = getNoDigits(4);
            res.push_back(make_pair(4,c));
            decrement(4, c);
        }
        if(cnt['X'-'A'] > 0){
            int c = getNoDigits(6);
            res.push_back(make_pair(6,c));
            decrement(6, c);
        }
        if(cnt['G'-'A'] > 0){
            int c = getNoDigits(8);
            res.push_back(make_pair(8,c));
            decrement(8, c);
        }

        for(int i = 0; i < 10; ++i){
            int c = getNoDigits(i);
            if(c > 0){
                res.push_back(make_pair(i,c));
                decrement(i, c);
            }
        }

        sort(res.begin(), res.end());

        for(int i = 0; i < 26; ++i){
            if(cnt[i] != 0)
                db(case_id, " ", i, " ", cnt[i]);
        }


        printf("Case #%d: ",case_id);

        for(int i = 0; i < res.size(); ++i){
            for(int j = 0; j < res[i].second; ++j)
                cout << res[i].first;
        }
        cout << endl;
	}


    return 0;
}
