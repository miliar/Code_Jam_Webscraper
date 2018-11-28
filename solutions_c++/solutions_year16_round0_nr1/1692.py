#include<iostream>
#include<stdio.h>
#include<string.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<set>
#include<math.h>
#include<map>
#include<string.h>
using namespace std;

#define mp make_pair
#define pb push_back

int t,n;

int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("op1-2.out","w",stdout);
    cin>>t;
    for(int cas=1;cas<=t;cas++) {
        bool arr[10];
        memset(arr,false,sizeof(arr));
        cin>>n;
        if(n==0)
            cout<<"Case #"<<cas<<": INSOMNIA\n";
        else {
            for(int i=1;;i++) {
                int temp=n*i;
                while(temp!=0) {
                    arr[temp%10]=true;
                    temp=temp/10;
                }
                bool flag=true;
                for(int j=0;j<10;j++) {
                    if(arr[j]==false)
                        flag=false;
                }
                if(flag) {
                    cout<<"Case #"<<cas<<": "<<n*i<<"\n";
                    break;
                }
            }
        }
    }
}
