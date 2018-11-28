#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define ll long long
using namespace std;
vector<string>v;
string s,ans,tmp;
int main(){
    freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t,k=1;
	cin>>t;
	while(t--)
    {
        cin>>s;
        ans="";
        int sz=s.size();
        ans+=s[0];
        char c;
        for(int i=1 ; i<s.size() ; i++)
        {
            c=s[i];
            tmp="";
            if(c>=ans[0])
                {tmp+=c;ans.insert(0,tmp);}
            else    ans+=c;
        }
        cout<<"Case #"<<k++<<": "<<ans<<endl;
	}

}
