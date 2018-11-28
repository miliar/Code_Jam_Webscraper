#include <bits/stdc++.h>
#define INF 1000000000
#define mod 1000000007
#define vi vector<int>
#define vit vector<int>::iterator
#define ll long long
#define ii pair<int, int>
#define vii vector<ii>
#define pb push_back
#define mp make_pair
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for(int ctr=1; ctr<=T; ctr++)
    {
        string str;
        cin>>str;
        string res, tmp;
        res += str[0];
        for(int i=1; i<str.size(); i++)
        {
            if(res[0]>str[i])
                res += str[i];
            else
            {
                tmp = res;
                res = str[i] + tmp;
            }
        }
        cout<<"Case #"<<ctr<<": "<<res<<endl;
    }
    return 0;
}
