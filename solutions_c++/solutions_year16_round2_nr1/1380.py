#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define ll long long
using namespace std;
vector<int>v;
int main(){
    freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t,k=1;
	cin>>t;
	while(t--)
    {
        v.clear();
	string s;
	cin>>s;
	int cnt=10000;
	while(cnt--&&s.size())
    {
        for(int i=0 ; i<s.size() ; i++)
        {
            if(s[i]=='Z')
            {
                s.erase(i,1);
                s.erase(s.find("E"),1);
                s.erase(s.find("R"),1);
                s.erase(s.find("O"),1);
                i=-1;
                v.pb(0);
                continue;
            }
            else if(s[i]=='U')
            {
                s.erase(i,1);
                s.erase(s.find("F"),1);
                s.erase(s.find("O"),1);
                s.erase(s.find("R"),1);
                i=-1;
                v.pb(4);
                continue;
            }
            else if(s[i]=='W')
            {
                s.erase(i,1);
                s.erase(s.find("T"),1);
                s.erase(s.find("O"),1);
                i=-1;
                v.pb(2);
                continue;
            }
            else if(s[i]=='G')
            {
                s.erase(i,1);
                s.erase(s.find("E"),1);
                s.erase(s.find("I"),1);
                s.erase(s.find("T"),1);
                s.erase(s.find("H"),1);
                i=-1;
                v.pb(8);
                continue;
            }
            else if(s[i]=='X')
            {
                s.erase(i,1);
                s.erase(s.find("I"),1);
                s.erase(s.find("S"),1);
                i=-1;
                v.pb(6);
                continue;
            }
        }
    }
    cnt=1000;
    while(s.size()&&cnt--)
    {
        for(int i=0 ; i<s.size() ; i++)
        {
            if(s[i]=='V')
            {
                if(s.find("I")!=-1&&s.find("F")!=-1)
                {
                    s.erase(i,1);
                    s.erase(s.find("I"),1);
                    s.erase(s.find("F"),1);
                    s.erase(s.find("E"),1);
                    v.pb(5);
                    i=-1;
                    continue;
                }
                else
                {
                    s.erase(i,1);
                    s.erase(s.find("S"),1);
                    s.erase(s.find("E"),1);
                    s.erase(s.find("N"),1);
                    s.erase(s.find("E"),1);
                    v.pb(7);
                    i=-1;
                    continue;
                }
            }
            if(s[i]=='O')
            {
                s.erase(i,1);
                s.erase(s.find("N"),1);
                s.erase(s.find("E"),1);
                v.pb(1);
                i=-1;
                continue;
            }
            if(s[i]=='T')
            {
                s.erase(i,1);
                s.erase(s.find("R"),1);
                s.erase(s.find("E"),1);
                s.erase(s.find("H"),1);
                s.erase(s.find("E"),1);
                v.pb(3);
                i=-1;
                continue;
            }
        }

    }
    cnt=s.size()/4;
    while(cnt--)    v.pb(9);
    sort(v.begin(),v.end());
    cout<<"Case #"<<k++<<": ";
    for(int i=0 ; i<v.size() ; i++) cout<<v[i];
    cout<<endl;
    }

}
