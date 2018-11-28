#include<bits/stdc++.h>
#define INF 0x7fffffff
#define forstl(i, n) for(__typeof(n.begin())i = n.begin(); i!= n.end(); i++)

using namespace std;



typedef long long ull;

typedef pair<ull, ull> ii;
typedef pair<ull, ii> iii;

set<iii> numbers;

ull toInt(string s)
{
    stringstream ss;
    ss << s;
    ull x;
    ss >> x;

    //cout << "desamprendi: " << x << endl;
    return x;
}

vector<ull> getNumbers(string c, vector<ull> v)
{
    if(count(c.begin(), c.end(), '?')==0)
    {
        v.push_back(toInt(c));
        return v;
    }

    for(int i=0; i<c.size(); i++)
    {
        if(c[i]=='?')
        {
            for(int j=0; j<10; j++)
            {
               c[i] = '0' + j;
               v = getNumbers(c, v);
            }
            break;
        }
    }

    return v;

}

void solve(string c, string x)
{

    vector<ull> c1; c1=  getNumbers(c, c1);
    vector<ull> x1; x1= getNumbers(x, x1);

    for(int i=0; i<c1.size(); i++)
    {
        for(int j=0; j<x1.size(); j++)
        {
            numbers.insert(make_pair(fabs(c1[i]-x1[j]), make_pair(c1[i], x1[j])));
        }
    }
    /*if(count(c.begin(), c.end(), '?') == 0 && count(j.begin(), j.end(), '?') == 0)
    {
        ull a = toInt(c), b = toInt(j);
        numbers.insert(make_pair(abs(a-b), make_pair(a,b)));
        return;;
    }


    for(int i=0; i<c.size(); i++)
    {
        string x = c;
        if(c[i]=='?')
        {
            for(int s =0; s<c.size(); s++)
            {
                x[s] = '0' + s;
                solve(x, j);
            }

            break;
        }
    }

    for(int i=0; i<j.size(); i++)
    {
        string x = j;
        if(j[i]=='?')
        {
            for(int s =0; s<j.size(); s++)
            {
                x[s] = '0' + s;
                solve(c, x);
            }

            break;
        }
    }*/
}


int main()
{
    int t;
    int cases =1;
    while(scanf("%d", &t)!=EOF)
    {
        cin.ignore();
        while(t--)
        {
            numbers.clear();
            printf("Case #%d: ", cases++);
            string c,j;

            cin >> c >> j;

            solve(c,j);

            /*forstl(it, numbers)
            {
                printf("%lld %lld %lld \n", *it);
            }*/
            printf("%0*lld ", c.size(), numbers.begin()->second.first);
            printf("%0*lld\n", c.size(), numbers.begin()->second.second);
        }
    }
    return 0;
}
