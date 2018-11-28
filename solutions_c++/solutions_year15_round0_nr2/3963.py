#include<iostream>
#include<fstream>
#include<map>
#include<cmath>
using namespace std;
ifstream fin("in.in");
ofstream fout("out.out");
#define cin fin
#define cout fout
map<int,int> s;
void input()
{
    s.clear();
    int d;
    cin>>d;
    while(d--)
    {
        int a;
        cin>>a;
        s[a]++;
    }
}
int solve()
{
    if(s.empty())
        return 0;
    pair<int,int> maxi=*s.rbegin();
    if(maxi.first<=3)
        return maxi.first;
    int ret=maxi.first;
    pair<int,int> a=maxi;
    pair<int,int> b=maxi;
    for(a.first=2,b.first=maxi.first-2;a.first<=b.first;a.first++,b.first--)
    {
        s.erase(maxi.first);
        s[a.first]+=a.second;
        s[b.first]+=b.second;
//        int temp=maxi.second;
//        for(int i=a.first+1;i<maxi.first;i++)
//            if(s.count(i))
//                temp+=s[i];
//        if(temp<=maxi.first-a.first)
            ret=min(ret,maxi.second+solve());
        s[a.first]-=a.second;
        s[b.first]-=b.second;
        if(!s[a.first])
            s.erase(a.first);
        if(!s[b.first])
            s.erase(b.first);
        s.insert(maxi);
    }
    return ret;
}
int main()
{
    int t;
    cin>>t;
    for(int v=1;v<=t;v++)
    {
        input();
        cout<<"Case #"<<v<<": "<<solve()<<endl;
    }
    return 0;
}


