#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define mod 1000000007
bool arr[10];
int main()
{
    freopen("in1.txt","r",stdin);
    freopen("out1.txt","w",stdout);
    int t;
    cin>>t;
    for(int ii=0;ii<t;ii++){
        ll n,tmp;
        cin>>n;
        tmp=n;
        for(int i=0;i<10;i++)
            arr[i]=false;
        int cnt=0,prevcnt=0,flg=1,hell=0;
        while(hell<1000&&cnt!=10){
            prevcnt=cnt;
            ll a=tmp;
            //cerr<<tmp<<endl;
            while(a){
                if(arr[a%10]==false){
                    cnt++;
                    arr[a%10]=true;
                }
                a/=10;
            }
            //cerr<<"c "<<cnt<<endl;
            tmp+=n;
            hell++;
        }
        if(cnt==10)
            cout<<"Case #"<<ii+1<<": "<<tmp-n<<endl;
        else
            cout<<"Case #"<<ii+1<<": "<<"INSOMNIA"<<endl;
    }
}
