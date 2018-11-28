#include<bits/stdc++.h>

#define F first
#define S second
#define endl "\n"
#define mp make_pair
#define pb push_back
#define MOD 1000000007

using namespace std;

int testcase, end, bitch, shadow, k;
string st, jarvis;

int main(){
//freopen("input.txt", "r", stdin);
//freopen("output.txt", "w", stdout);
ios_base::sync_with_stdio(0);
cin.tie(0);

cin>>testcase;
while(testcase--)
{
    cin>>st;
    bitch = 0, ++k;
    end = st.size()-1;
    while(st[end] == '+')
        st.erase(st.begin()+end), --end;
    end = st.size();
    jarvis  = "";
    for(int i = 0; i < end; i++)
        jarvis += '+';
    while(st != jarvis)
    {
        shadow = 0;
        if(st[shadow] == '-')
        {
            while(st[shadow] == '-')
                st[shadow] = '+', ++shadow;
            ++bitch;
        }
        else
        {
            while(st[shadow] == '+')
                st[shadow] = '-', ++shadow;
            ++bitch;
        }
    }
    cout<<"Case #"<<k<<": "<<bitch<<endl;
}

return 0;}
