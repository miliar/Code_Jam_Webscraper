#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<map>
#include<bitset>
#include<cmath>

using namespace std;

int n;
string s;
vector<long long int> V;
vector<long long int> div;
int cpt,xx;

bool check()
{
    for(int i=2;i<=10;i++)
        if(div[i]==0)
            return false;
    return true;

}
void trans()
{
    if(cpt==xx)
        return;
    bitset<32> B(s);
    div.clear();
    div.assign(11,0);
    long long int a=1;
    for(int i=2;i<=10;i++)
    {
        V[i]=0;
        a=1;
        for(int j=0;j<s.size();j++)
        {
            //cout<<a<<" ("<<V[i]<<","<<B[j]<<") ";
            V[i]+=B[j]*a;
            a*=i;
        }

    }

    for(int i=2;i<=10;i++)
    {
        bool ver=true;
        for(long long int  j=2;j<=sqrt(V[i]);j++)
        {
            if(V[i]%j==0)
            {
                div[i]=j;
                ver=false;
                break;
            }
        }
        if(check())
        {
            cout<<s;
            for(int j=2;j<=10;j++)
            {
                cout<<" "<<div[j];
            }
            cpt++;
            cout<<endl;
        }
    }

}

void fct(int i)
{
    if(cpt==xx)
        return;
    if(i==n-1)
        {
            trans();
            return;
        }

    s[i]='0';
    fct(i+1);
    s[i]='1';
    fct(i+1);

}
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);

    int t;
    cin>>t;
    int k=1,x=0;
    V.resize(11);
   div.resize(11);
    while(t--)
    {
        cout<<"Case #"<<k<<":\n";
        k++;
        cin>>n>>xx;
        cpt=0;
        s.clear();
        s.push_back('1');
        for(int i=1;i<n-1;i++)
            s.push_back('0');
        s.push_back('1');

        fct(1);
    }

}
