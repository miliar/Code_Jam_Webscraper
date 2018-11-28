#include <bits/stdc++.h>
using namespace std;
vector<string> s;
int main()
{
    s.push_back("A");
    s.push_back("B");
    s.push_back("C");
    s.push_back("D");
    s.push_back("E");
    s.push_back("F");
    s.push_back("G");
    s.push_back("H");
    s.push_back("I");
    s.push_back("J");
    s.push_back("K");
    s.push_back("L");
    s.push_back("M");
    s.push_back("N");
    s.push_back("O");
    s.push_back("P");
    s.push_back("Q");
    s.push_back("R");
    s.push_back("S");
    s.push_back("T");
    s.push_back("U");
    s.push_back("V");
    s.push_back("W");
    s.push_back("X");
    s.push_back("Y");
    s.push_back("Z");

    int test, t, n, ans, a, sum = 0;
    multimap<int, int> ma;
    multimap<int, int>::iterator it1, it2;
    vector<string> v;
    cin>>t;
    for(int test = 1; test <= t; test++){
        sum = 0;
        ma.clear();
        v.clear();
        cin>>n;
        for(int i = 0; i < n; i++){
            cin>>a;
            sum+=a;
            ma.insert(make_pair(a, i));
        }
        while(1){
            it1 = ma.end();
            it2 = ma.end();
            it1--;
            it2--;
            it2--;
            if(it1->first == 0)
                break;
            if(max((it1->first-1), it2->first) <= (sum-1)/2){
                sum-=1;
                int x = it1->first-1;
                int y = it1->second;
                v.push_back(s[y]);
                ma.erase(it1);
                ma.insert(make_pair(x, y));
            }
            else{
                sum-=2;
                int l = it1->first-1;
                int m = it1->second;
                int n = it2->first-1;
                int o = it2->second;
                string p = s[m]+s[o];
                v.push_back(p);
                ma.erase(it1);
                ma.erase(it2);
                ma.insert(make_pair(l, m));
                ma.insert(make_pair(n, o));
            }
        }
        cout<<"Case #"<<test<<": ";
        for(int i = 0; i < v.size(); i++){
            cout<<v[i]<<" ";
        }
        cout<<endl;
    }
}