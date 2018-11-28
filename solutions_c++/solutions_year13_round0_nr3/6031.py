#include<iostream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;

int palindrome[1001];
int squares[1001];

bool isPalin(int n)
{
    vector<int> pal;
    bool flag=true;
    while(n!=0)
    {
        int x = n%10;
        n = n/10;
        pal.push_back(x);
    }
    for(int i=0,j=pal.size()-1;i<pal.size()/2;i++,j--)
    {
        if(pal[i]!=pal[j])
            flag=false;
    }
    return flag;
}
void sss()
{
    int i=1;
int    n=0;
    while(n<1001)
    {
        squares[n]=-1;
        n++;
    }
    n=0;
    while(n<1001)
    {
        n=i*i;
        if(n<1001)
            squares[n]=i;
        i++;
    }
}
int main()
{
    for(int i=0;i<1001;i++)
    {
        if(isPalin(i))
        palindrome[i]=1;
        else
        palindrome[i]=0;
    }
  sss();
    int t;
    cin>>t;
    int i=0;
    while(t--)
    {
        i++;
        int a,b;
        cin>>a>>b;
        int count =0;
        while(a<=b)
        {
            if(isPalin(a))
            {
                //cout<<a<<" ";
                if(squares[a]!=-1)
                    if(isPalin(squares[a]))
                        count++;
            }
            a++;
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
      //  cout<<count<<endl;
    }
    return 0;
}
