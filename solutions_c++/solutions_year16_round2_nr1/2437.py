//PD
#include<bits/stdc++.h>
#define pb push_back
#define SZ(a) (int)(a.size())
#define sortarr(a) sort(a.begin(),a.end()) 
#define sortrev(a) sort(a.rbegin(),a.rend())
#define mp make_pair
#define fi(i,a,b) for(i=a;i<b;i++)
#define X first
#define Y second

using namespace std;

typedef long long LL;
typedef vector<int> VI;
LL modpow(LL a, LL p, LL mod)
{LL ret = 1;while(p){if(p&1)ret = (ret*a)%mod;a=(a*a)%mod;p/=2;}return ret;}

LL power(LL a, LL p)
{LL ret = 1;while(p){if(p&1)ret = (ret*a);a=(a*a);p/=2;}return ret;}
/*int p[1000011];
VI prms;
void sieve(int n)
{int i,j;prms.pb(2);;fi(i,3,n){if(!i%2||!p[i])continue;prms.pb(i);for(j=2*i;j<n;j+=i)p[j]=1;}}*/


int main()
{
    int i,j,k,tmp;
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
   // FILE *fin = freopen("john.in","r",stdin);
   // FILE *fout = freopen("john.out","w",stdout);

    int t;
    cin>>t;
    int T=t;
    string s;
    while(t--)
    {
        cout<<"Case #"<<T-t<<": ";
        cin>>s;
        vector<int> al(26,0);
        vector<int> num(10,0);
        for(i=0;i<s.length();i++)
            al[s[i]-'A']++;

        while(al['Z'-'A'])
        {
            num[0]++;
            al['Z'-'A']--;
            al['E'-'A']--;
            al['R'-'A']--;
            al['O'-'A']--;
        }



        while(al['W'-'A'])
        {
            num[2]++;
            al['T'-'A']--;
            al['W'-'A']--;
            //al['R'-'A']--;
            al['O'-'A']--;
        }
        



        while(al['U'-'A'])
        {
            num[4]++;
            al['F'-'A']--;
            al['O'-'A']--;
            al['U'-'A']--;
            al['R'-'A']--;
        }


        while(al['R'-'A'])
        {
            num[3]++;
            al['T'-'A']--;
            al['H'-'A']--;
            al['R'-'A']--;
            al['E'-'A']--;
            al['E'-'A']--;

        }

        while(al['X'-'A'])
        {
            num[6]++;
            al['S'-'A']--;
            al['I'-'A']--;
            al['X'-'A']--;
           // al['O'-'A']--;
        }



        while(al['G'-'A'])
        {
            num[8]++;
            al['E'-'A']--;
            al['I'-'A']--;
            al['G'-'A']--;
            al['H'-'A']--;
            al['T'-'A']--;
        }




        while(al['F'-'A'])
        {
            num[5]++;
            al['F'-'A']--;
            al['I'-'A']--;
            al['V'-'A']--;
            al['E'-'A']--;
        }


        while(al['S'-'A'])
        {
            num[7]++;
            al['S'-'A']--;
            al['E'-'A']--;
            al['V'-'A']--;
            al['E'-'A']--;
            al['N'-'A']--;

        }


        while(al['O'-'A'])
        {
            num[1]++;
            al['O'-'A']--;
            al['N'-'A']--;
            al['E'-'A']--;
           // al['O'-'A']--;
        }





        while(al['N'-'A'])
        {
            num[9]++;
            al['N'-'A']--;
            al['I'-'A']--;
            al['N'-'A']--;
            al['E'-'A']--;
        }



    for(i=0;i<10;i++)
        for(j=0;j<num[i];j++)
            cout<<i;


    cout<<endl;

    num.clear();
    al.clear();
    }






    return 0;
}

