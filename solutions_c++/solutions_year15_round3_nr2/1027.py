#include <iostream>
#include <string>
#include <vector>

using namespace std;

int occurence(string &s, string &target)
{
    int ans=0;
    size_t start = 0;

    while ((start = s.find(target, start)) != string::npos) {
        ans++;
        start ++; // see the note
    }

    return ans;
}

int getCnt(string &keys, string &s, string &target, int n, int &mx)
{
    if (s.size()==n)
    {
        //cout<<s<<endl;
        //static int cnt=0;
        //cnt++;
        //cout<<cnt<<endl;
        int occur = occurence(s, target);
        mx = max(mx, occur);

        return occur;
    }

    int ans=0;
    for (int i=0; i<keys.size(); i++)
    {
        s.push_back(keys[i]);
        ans+=getCnt(keys, s, target, n, mx);
        s.pop_back();
    }

    return ans;
}

int mpow(int a, int b)
{
    int ans=1;
    for (int i=0; i<b; i++)
    {
        ans=ans*a;
    }

    return ans;
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    cin>>T;
    for (int cas=1; cas<=T; cas++)
    {
        int K,L,S;
        cin>>K>>L>>S;
        string keys,target;
        cin>>keys>>target;

        string temp;
        int mx=-1;
        int ans = getCnt(keys, temp, target, S, mx);
        int total = mpow(K,S);
        //cout<<ans<<" "<<total<<" "<<mx<<endl;
        printf("Case #%d: %.08lf\n",cas,mx - ( (double)ans/(double)total ));
    }
    return 0;
}
