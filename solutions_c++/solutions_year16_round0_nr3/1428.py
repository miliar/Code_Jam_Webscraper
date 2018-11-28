#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define mod 1000000007
bool prime[1000006];
char arr[100];
int n,j,cnt;
ll tmp[20];
vector<vector<ll> > vc;
int prim(ll n){
    int i;

    if (n==2)
        return 1;

    if (n%2==0)
        return 0;

    for (i=3;i<=sqrt(n);i+=2)
        if (n%i==0)
            return 0;

    return 1;
}

void rec(int ind)
{
    if(ind==n-1){
        if(cnt==j)
            return;
        ///check in all bases
        string tm(arr);
        //cout<<tm<<endl;
        for(int i=2;i<=10;i++)
        {
            tmp[i]=stol (tm,nullptr,i);
            //cout<<tmp[i]<<" ";
            if(prim(tmp[i]))
                return;
        }
        //cout<<"ASD";
        vector<ll> vv;
        vc.push_back(vv);
        vc[cnt].push_back(tmp[10]);
        for(int i=2;i<=10;i++){
            for(int j=2;;j++){
                if(tmp[i]%j==0){
                    //cout<<j<<endl;
                    vc[cnt].push_back(j);
                    break;
                }
            }
        }
        cnt++;
        return;
    }
    arr[ind]='0';
    rec(ind+1);
    arr[ind]='1';
    rec(ind+1);
}
int main()
{
    //SieveOfEratosthenes(1000006);
    freopen("in3.txt","r",stdin);
    freopen("out3.txt","w",stdout);
    int t;
    cin>>t;
    cin>>n>>j;
    arr[0]='1',arr[n-1]='1';arr[n]='\0';
    vc.resize(j);
    rec(1);
    cout<<"Case #1:"<<endl;
    for(int i=0;i<j;i++)
    {
        for(int jj=0;jj<vc[i].size();jj++){
            cout<<vc[i][jj]<<" ";
        }
        cout<<endl;
    }
}
