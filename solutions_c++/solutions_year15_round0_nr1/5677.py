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
        int smax;
        string sk;
        infile>>smax>>sk;
        int i,ans=0;
        int temp=sk[0]-48;
        for (i=1;i<sk.size();i++)
        {
            if (sk[i]>48)
            {
                if (i>temp)
                {
                    ans+=i-temp;
                    temp+=i-temp+sk[i]-48;
                }
                else temp+=sk[i]-48;
            }
        }

        ffile<<"Case #"<<j<<": "<<ans<<"\n";
    }
    ffile.close();
}
