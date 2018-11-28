///     Raihan Ruhin
///     CSE, Jahangirnagar University.
///     Dhaka-Bangladesh.
///     id: raihanruhin (topcoder / codeforces / codechef / uva ), 3235 (lightoj)
///     mail: raihanruhin@ (yahoo / gmail / facebook)
///     blog: ruhinraihan.blogspot.com

#include<bits/stdc++.h>
using namespace std;

#define SET(a) memset(a,-1,sizeof(a))
#define CLR(a) memset(a,0,sizeof(a))
#define PI acos(-1.0)

#define MOD 1000000007
#define MX 100010

#define READ freopen("input.txt", "r", stdin)
#define WRITE freopen("output.txt", "w", stdout)

long long toDecimal(string s,int baseFrom)
{
    int cnt=0;
    long long res=0;
    for(int i=s.length()-1;i>=0;i--)
    {
        if ( s[i] > 47 && s[i] < 58 )
        res+= (pow(baseFrom,cnt)*(s[i]-'0'));
        else
        res+= (pow(baseFrom, cnt)*(s[i]-55));
        cnt++;
    }
    return res;
}

string deciamlTo(long long num, int baseTo)
{
    string s="";
    while(num)
    {
        int tmp=num%baseTo;
        if(tmp<10)
            s+=tmp+'0';
        else
            s+= char (tmp+55);
        num/=baseTo;
    }
    if(s=="")    return "0";
    reverse(s.begin(), s.end());
    return s;
}
//int to string
string tostring(int a)
{
    ostringstream os("");
    os<<a;
    return os.str();
}

//string to long long
long long tolong(string a)
{
    long long res;
    istringstream os(a);
    os>>res;
    return res;
}

vector<int>prime;
bool status[MX+2];

void PrimeGenerate(int n)
{
    int sq=sqrt(n);
    for(int i=3; i<=sq; i+=2)
    {
        if(!status[i])
            for(int j=i*i; j<=n; j+=(i<<1))
                status[j]=true;
    }

    status[0]=status[1]=true;
    for(int i=4;i<=n;i+=2) status[i]=true;

    prime.push_back(2);
    for(int i=3; i<=n; i+=2)
        if(!status[i])
            prime.push_back(i);
return;
}

int primeDiv(long long n)
{
    for(int i=0;i<prime.size();i++)
    {
        if(n % (long long) prime[i] == 0) return prime[i];
        if(n < (long long) prime[i]) break;
    }
return 0;
}


int main()
{
    //READ;
    WRITE;
    PrimeGenerate(1000);
    ios_base::sync_with_stdio(0);cin.tie(0);
    int tc,kk=1, n;
    long long num;
    string s="1000000000000001", tmp;
    cin>>tc;
    while(tc--)
    {
        int cnt=0;
        cout<<"Case #"<<kk++<<":\n";
        for(long long i=0;i<=16383;i++)
        {
            string mid=deciamlTo(i, 2);
            tmp=s;
            for(int j=mid.size()-1, k=14;j>=0;j--, k--)
                tmp[k]=mid[j];

            bool nonPrime=true;
            vector<int>v;

            for(int j=2;j<=10;j++)
            {
                num=toDecimal(tmp, j);
                int div=primeDiv(num);
                //cout<<div<<endl;
                //if(cnt==0) cout<<num<<" "<<div<<endl;
                if(div==0)
                {
                    nonPrime=false;
                    break;
                }
                v.push_back(div);
            }
            //cout<<cnt<<endl;
            if(nonPrime)
            {
                cout<<tmp;
                for(int j=0;j<v.size();j++) cout<<" "<<v[j];
                cout<<"\n";
                cnt++;
            }
            if(cnt==50) break;
        }
    }
    return 0;
}


