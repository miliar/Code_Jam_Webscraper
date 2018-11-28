#include <iostream>
#include <algorithm>
using namespace std;

typedef pair<int,int> pii;      //first- number     second-alphabet

int compare(pii t1,pii t2)
{
    return t1.first>t2.first;
}

int main()
{
    int T;
    cin>>T;
    
    for(int t=1;t<=T;++t)
    {
        int n;
        cin>>n;
        
        pii p[n];
        for(int i=0;i<n;++i)
        {
            cin>>p[i].first;
            p[i].second=i;
        }
        
        sort(p,p+n,compare);
        
        cout<<"Case #"<<t<<": ";
        
        for(int i=0;i<n;i+=2)
        {
            int temp=p[i].first-p[i+1].first;
            if(temp%2 == 1)
                cout<<(char)('A' + p[i].second)<<' ';
            
            temp--;
            
            for(int j=0;j<temp;j+=2)
                cout<<(char)('A' + p[i].second)<<(char)('A' + p[i].second)<<' ';
        }
        
        if(n%2 == 1)
        {
            int temp=p[n-1].first;
            if(temp%2 == 1)
                cout<<(char)('A' + p[n-1].second)<<' ';
            
            temp--;
            
            for(int i=0;i<temp;i+=2)
                cout<<(char)('A' + p[n-1].second)<<(char)('A' + p[n-1].second)<<' ';
        }
        n--;    //decrease after removing odd
        
        for(int i=0;i<n;i+=2)
        {
            int temp=p[i+1].first;
            
            for(int j=0;j<temp;++j)
                cout<<(char)('A' + p[i].second)<<(char)('A' + p[i+1].second)<<' ';
        }
        cout<<'\n';
    }
    
    return 0;
}