//google code jam

//#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;
int n;
int *x;
int solve(int,int );
int main()
{
    ifstream cin; cin.open("input.txt");
    ofstream cout; cout.open("output.txt");
    int s,t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>s>>n;
        x=new int[n];
        int res=0;
        for(int j=0;j<n;j++) cin>>x[j];
        sort(&x[0],&x[n-1]+1);
       // for(int j=0;j<n;j++)  cout<<x[j]<<' ';
        //cout<<endl;
        if(s==1) res=n;
        else res=solve(s,0);
        cout<<"Case #"<<i+1<<": "<<res<<endl;
    }

    return 0;
}


int solve(int s, int p)
{
        int t1,t2;
        int res=0;
        for(int j=p;j<n;j++)
        {
            if(x[j]<s) {s+=x[j]; }
            else if(x[j]<(s+s-1)){res++; s+=s-1+x[j];}
            else if(x[j]>=(s+s-1))
            {
               if(s!=(s+s-1)) t1=solve(s+s-1,j); else t1=1000000000;
                t2=solve(s,j+1);
                res++;
                if(t1>t2) res+=t2; else res+=t1;
                break;
            }
        }
        return res;
}
