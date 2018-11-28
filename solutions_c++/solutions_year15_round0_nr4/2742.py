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

//fucntion to display a vector
template <typename T>
void displayVector(T v,int size)
{
    for(typename T::iterator i=v.begin();i!=v.begin()+size;i++)
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

bool cmp(int a,int b)
{
    return a>b;
}

int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    //freopen("input.txt","r",stdin);
    freopen("output.out","w",stdout);
    LL i,j,n,t,m,sum=0,ans=0,count=0,l,k,x,d,flag=0,c,r;
    string str;
    

    vvll mat;
    cin>>t;
    for_each(k,0,t)
    {
        cin>>x>>r>>c;
        if(x==1)
        {
            str="GABRIEL";
        }
        else if(x==2)
        {   
            if((r*c)%2==0)
            {
                str="GABRIEL";       
            }
            else
            {
                str="RICHARD";
            }
        }
        else if(x==3)
        {
            if(r*c==12||r*c==6||r*c==9)
            {
                str="GABRIEL";       
            }
            else
            {
                str="RICHARD";
            }
        }
        else
        {
            if(r*c==12||r*c==16)
            {
                str="GABRIEL";          
            }
            else
            {
                str="RICHARD";  
            }
        }
        cout<<"Case #"<<k+1<<": "<<str<<endl;
    }
    return 0;

}