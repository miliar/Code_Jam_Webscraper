#include<bits/stdc++.h>
using namespace std;
string a;
int main()
{
    freopen("1.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int m,i,j,n,count,temp ;
    cin>>n;

    for(i=0;i<n;i++)
    {
        cin>>m>>a;
             count=0;
        temp=0;
        for(j=0;j<=m;j++)
        {
            if(j<=temp)
            {
                temp+=a[j]-'0';
            }
            else{
                count+=j-temp;
                temp+=j-temp + a[j]-'0';
            }
        }
        cout<<"Case #"<<i+1<<": "<<count<<"\n";
    }
    return 0;
}
