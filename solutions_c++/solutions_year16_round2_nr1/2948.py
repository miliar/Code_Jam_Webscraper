#include<bits/stdc++.h>
using namespace std;
#define ll long long
vector <ll> v;
ll done[300];

int main()
{
freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
ll l,t,k,i;
bool flag;
string s;
cin>>t;
for(k=1;k<=t;k++)
{
    v.clear();
    flag=true;
    cin>>s;
    memset(done,0,sizeof(done));
    l=s.length();
    for(i=0;i<l;i++)
        done[s[i]]++;

    while(done['Z']>=1&&done['E']>=1&&done['R']>=1&&done['O']>=1)
    {

        v.push_back(0);
        done['Z']--;
        done['E']--;
        done['R']--;
        done['O']--;
    }
    while(done['T']>=1&&done['W']>=1&&done['O']>=1)
    {
        flag=true;
        v.push_back(2);
        done['T']--;
        done['W']--;
        done['O']--;
    }
 while(done['F']>=1&&done['O']>=1&&done['U']>=1&&done['R']>=1)
    {
        flag=true;
        v.push_back(4);
        done['F']--;
        done['O']--;
        done['U']--;
        done['R']--;

    }

        while(done['S']>=1&&done['I']>=1&&done['X']>=1)
    {
        flag=true;
        v.push_back(6);
        done['S']--;
        done['I']--;
        done['X']--;

    }
while(done['E']>=1&&done['I']>=1&&done['G']>=1&&done['H']>=1&&done['T']>=1)
    {
        flag=true;
        v.push_back(8);
        done['E']--;
        done['I']--;
        done['G']--;
        done['H']--;
        done['T']--;

    }
     while(done['T']>=1&&done['H']>=1&&done['R']>=1&&done['E']>=2)
    {
        flag=true;
        v.push_back(3);
        done['T']--;
        done['H']--;
        done['E']-=2;
        done['R']--;
    }




    while(done['O']>=1&&done['N']>=1&&done['E']>=1)
    {
        flag=true;
        v.push_back(1);
        done['O']--;
        done['N']--;
        done['E']--;

    }





    while(done['F']>=1&&done['I']>=1&&done['V']>=1&&done['E']>=1)
    {
        flag=true;
        v.push_back(5);
        done['F']--;
        done['I']--;
        done['V']--;
        done['E']--;
    }


    while(done['S']>=1&&done['N']>=1&&done['E']>=2&&done['V']>=1)
    {
        flag=true;
        v.push_back(7);
        done['S']--;
        done['N']--;
        done['E']-=2;
        done['V']--;
    }



    while(done['N']>=2&&done['I']>=1&&done['E']>=1)
    {
        flag=true;
        v.push_back(9);
        done['N']-=2;
        done['I']--;
        done['E']--;

    }

    sort(v.begin(),v.end());
    cout<<"Case #"<<k<<": ";
    string temp="";
    for(i=0;i<v.size();i++)
        temp+=(v[i]+'0');
        cout<<temp<<"\n";

    v.clear();
}
return 0;
}
