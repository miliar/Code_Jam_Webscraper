#include<bits/stdc++.h>
using namespace std;
int t;
const int maxn=1009;
double na[maxn],ke[maxn];
int n;
bool icanbeathim(int stna,int eke)
{
    int pos1=n,pos2=eke;
    while(pos1>=stna)
    {
        //cout<<"pos1="<<pos1<<" "<<"pos2="<<pos2<<" na[pos1]="<<na[pos1]<<" ke[pos2]="<<ke[pos2]<<endl;
        if(na[pos1]<ke[pos2])return false;
        pos1--;pos2--;
    }
    return true;
}
int actwar()
{
    int pos1=1,pos2=n,lke=n;
    int re=0;
    while(pos2>=1)
    {
        if(na[pos2]>ke[lke])
        {
            re++;
            pos1++;pos2--;
        }
        else
        {
            lke--;
            pos2--;
        }
    }
    return re;
}
void solve(int tc)
{

    cin>>n;
    for(int i=1;i<=n;i++)cin>>na[i];
    for(int j=1;j<=n;j++)cin>>ke[j];
    sort(na+1,na+n+1);
    sort(ke+1,ke+n+1);
    int uk1=1,uk2=n;
    while(!icanbeathim(uk1,uk2))
    {
        uk1++;uk2--;
    }
    cout<<"Case #"<<tc<<": "<<n-uk1+1<<" ";
    cout<<actwar()<<"\n";
    /*cerr<<uk1<<" "<<uk2<<endl;
    for(int i=1;i<=n;i++)cerr<<na[i]<<" ";
    cerr<<endl;
    for(int j=1;j<=n;j++)cerr<<ke[j]<<" ";
    cerr<<endl;*/
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        solve(i);
    }
}
