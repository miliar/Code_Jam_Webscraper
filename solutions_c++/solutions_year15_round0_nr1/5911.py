#include <bits/stdc++.h>
#define MAX 1000
#define MOD 1000000007
#define for_each(i,x,n) for(i=x;i<n;++i)
#define for_each_dec(i,n,x) for(i=n-1;i>=x;--i)
#define SIZE(v) LL len=v.size();
typedef long long int LL;

using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<LL> vll;
typedef vector<vll> vvll;


//fucntion to display a vector
template <typename T>
void displayVector(T v)
{
    for(typename T::iterator i=v.begin();i!=v.end();i++)
    {
        cout<<*i<<" ";
    }
    cout<<endl;
}

//function to display a matrix
template <typename T>
void displayMatrix(T mat)
{
    for(typename T::iterator i=mat.begin();i!=mat.end();i++)
    {
            displayVector(*i);       
    }
    cout<<endl; 
}


//fucntion to input a vector
template <typename T>
void inputVector(T &v)
{
    for(typename T::iterator i=v.begin();i!=v.end();i++)
    {
        cin>>*i;
    }
}

//function to input a matrix
template <typename T>
void inputMatrix(T &mat)
{
    for(typename T::iterator i=mat.begin();i!=mat.end();i++)
    {
            inputVector(*i);
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    LL i,j,n,t,m,sum=0,ans=0,count=0,l,k,x;
    string str;
    vll arr;

    vvll mat;
    cin>>t;
    for_each(k,0,t)
    {

        int smax;
        cin>>smax;
        cin>>str;
        int peopleStanding=0;
        int count=0;
        for_each(i,0,smax+1)
        {
            if(peopleStanding<i)
            {
                count+=i-peopleStanding;
                peopleStanding=i;
            }
            peopleStanding+=str[i]-'0';
        }
        cout<<"Case #"<<k+1<<": "<<count<<endl;
    }
    return 0;

}