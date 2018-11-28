#include<bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long ull;
typedef long double ld;

#define inf 1000000007
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

using namespace std;

struct great
{
    template<class T>
    bool operator()(T const &a, T const &b) const { return a > b; }
};

struct sec {
    bool operator()(const std::pair<int,int> &left, const std::pair<int,int> &right) {
        return left.second < right.second;
    }
};

int main()
{
    ifstream infile;
    infile.open("Input.in");
    int t,j;
    infile>>t;
    ofstream ffile;
    ffile.open("Output.txt");
    for (j=1;j<=t;j++)
    {
        int x,r,c;
        string ans;
        infile>>x>>r>>c;

        if (x==1) ans="GABRIEL";

        else if (x==2)
        {
            if ((r*c)%2) ans="RICHARD";
            else ans="GABRIEL";
        }

        else if (x==3)
        {
            if (r<=2 && c<=2) ans="RICHARD";
            else if (r*c==3) ans="RICHARD";
            else if (r*c==6 || r*c==9) ans="GABRIEL";
            else if (r*c==4 || r*c==8 || r*c==16) ans="RICHARD";
            else if (r*c==12) ans="GABRIEL";
        }

        else if (x==4)
        {
            if (r<=3 && c<=3) ans="RICHARD";
            else if (r*c==4 || r*c==8) ans="RICHARD";
            else ans="GABRIEL";
        }

        ffile<<"Case #"<<j<<": "<<ans<<"\n";
    }
    ffile.close();
}
