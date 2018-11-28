#include<bits/stdc++.h>
#define s(x) scanf("%d",&x)
#define ll long long
#define l(x) scanf("%I64d",&x)
#define cst int t; s(t); while(t--)
#define fr freopen("B-large.in", "r", stdin)
#define finp ios_base::sync_with_stdio(false)
#define pb push_back
#define pf printf
using namespace std;


class pancake
{
    string s;
public:
    int solve(void);
    void flip(int i, int j);
};

void pancake::flip(int i,int j)
{
    for(int k=i; k<=j; k++)
        if(s[k]=='+')
            s[k]='-';
        else
            s[k]='+';

}

int pancake::solve(void)
{
    cin>>s;
    int count = 0;
    int len=s.length();
    while(len--){
        if(s[len]=='-'){
            count++;
            flip(0, len);
        }
    }
    return count;
}

int main()
{
    fr;
    freopen("out.txt", "w", stdout);
    int ct=0;
    cst{
       pancake ob;
       cout<<"Case #"<<++ct<<": "<<ob.solve()<<endl;
    }
    return 0;
}
