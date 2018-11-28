#include <bits/stdc++.h>
using namespace std;

int main() {
    long long i,t;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        long long n;
        cin>>n;
        vector<vector<long long> > p;
        p.resize(n,vector<long long> (2,0));
        for(long long j=0;j<n;j++)
        {
            cin>>p[j][0];
            p[j][1]=j;
        }
        cout<<"Case #"<<i<<": ";
        long long flag=0;
        while(1)
        {
            sort(p.begin(),p.begin()+n);
            if(p[n-1][0]==0)
            break;
            if(n-4>=0)
            if(p[n-3][0]==1&&p[n-2][0]==1&&p[n-1][0]==1&&p[n-4][0]==0)
            {
                cout<<(char)(p[n-1][1]+65)<<" "<<(char)(p[n-2][1]+65)<<(char)(p[n-3][1]+65);
                flag=1;
                break;
            }
            if(n-4==-1)
            if(p[n-3][0]==1&&p[n-2][0]==1&&p[n-1][0]==1)
            {
                cout<<(char)(p[n-1][1]+65)<<" "<<(char)(p[n-2][1]+65)<<(char)(p[n-3][1]+65);
                flag=1;
                break;
            }
            if(flag==0)
            cout<<(char)(p[n-1][1]+65)<<(char)(p[n-2][1]+65)<<" ";
            p[n-1][0]--;
            p[n-2][0]--;
            
        }
        
        
        cout<<"\n";
    }
	return 0;
}