#include<iostream>
#include<set>
#include<vector>
using namespace std;

typedef set<string> SS;

SS sset;

string recs;

#define dbg(x) cerr << #x << " = " << x << " "

int count_sum( int n, bool is_odd)
{
    int res = 0;
    for(int i=0;i<(int)recs.size()-1;++i)
    {
        res += (recs[i]-'0')*(recs[i]-'0')*2;
    }

    if ( recs.size()>0)
    {
        if ( n>0 || !is_odd)
        {
            res += (recs[recs.size()-1]-'0')*(recs[recs.size()-1]-'0')*2;
        } else 
        {
            res += (recs[recs.size()-1]-'0')*(recs[recs.size()-1]-'0');
        }
    }
    return res;
}

string rotate(string str, bool is_odd)
{
    string res = recs;
    
    if ( !is_odd) res += recs[recs.size()-1];
    for (int i=recs.size()-2;i>=0;--i)
    {
        res += recs[i];
    }
    return res;
}

string square( string str)
{
    string res(2*str.size()-1,'0');

    for (int i=0;i<str.size();++i)
    {
        for (int j=0;j<str.size();++j)
        {
            res[i+j] += (str[i]-'0')*(str[j]-'0');
        }
    }

    return res;
}

void addsq(string s)
{
    sset.insert( string(110-s.size(),'0')+s);
}

void rec( int n, bool is_odd)
{
    int sum = count_sum(n,is_odd);
    if ( sum >=10)
        return;

    if ( n==0)
    {
        string str = rotate(recs,is_odd);
        string sq = square(str);
        addsq(sq);
        return;
    }

    for (int i=(sum==0 ? 1 : 0);i<=3;++i)
    {
        recs += ('0'+i);
        rec(n-1,is_odd);
        recs.erase(recs.size()-1);
    }
}

void gen(int n, bool is_odd)
{
    recs="";
    rec(n,is_odd);
}

typedef vector<string> VS;

VS vs;

string add_1( string s)
{
    int i=s.size()-1;

    while ( i>=0 && s[i]=='9') { s[i]='0';i--;}
    if ( i>=0)
    {
        s[i]++;
    } else
    {
        s = '1'+s;
    }
    return s;
}

int search_i( string s)
{
    s = string(110-s.size(),'0')+s;

    int _min = 0;
    int _max = vs.size()-1;

    while (_min < _max)
    {
        int mid = (_min+_max)>>1;
        if ( vs[mid] < s)
        {
            _min = mid+1;
        } else
        {
            _max = mid;
        }
    }
    return _min;
}

void print(int t, int x)
{
    cout << "Case #" << t << ": " << x << endl;
}

int main()
{
    for (int i=1;i<=26;++i)
    {
        gen(i,true);
        gen(i,false);
    }
    
    sset.insert(string(110,'1'));

    vs.assign(sset.begin(),sset.end());

    int T;
    cin >> T;
    for (int t=0;t<T;++t)
    {
        string A,B;
        cin >> A >> B;
        print(t+1, search_i(add_1(B))-search_i(A));
    }
}
