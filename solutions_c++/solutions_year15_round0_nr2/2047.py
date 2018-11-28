#include<bits/stdc++.h>
#define For(i,i1,i2) for(int i=i1;i<i2;i++)
#define ll long long
#define pii pair<int,int>
#define F first
#define S second
#define V vector<int>
#define MP make_pair
#define PB push_back
#define MAX 1000000000000
#define CLR(x) memset(x,0,sizeof(x));
using namespace std;
int arr[10000],ans[10000];
int main(){
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    For(x,1,t+1){
        int n,Ans=0,mx=-1,mi=-1,Mx,sum=0,sq;
        CLR(arr);
        cin>>n;
        For(i,0,n){
            cin>>arr[i];
            sum+=arr[i];
            if(mx<arr[i]){
                mx=arr[i];
                mi=i;
            }
        }
        Mx=mx;
        sq=sqrt(sum);
        For(j,2,mx){
            Ans=0;
            For(i,0,n){
                Ans+=ceil((double)arr[i]/j)-1;
            }
            ans[j]=Ans+j;
            Mx=min(Mx,ans[j]);
        }
        /*int siz=n;
        ans[0]=mx;
        Mx=mx;
        For(i,1,Mx+1){
            int tmp=mx-mx/2;
            arr[mi]/=2;
            arr[siz]=tmp;
            siz++;mx=-1;mi=-1;
            For(j,0,siz){
                if(mx<arr[j]){
                    mx=arr[j];
                    mi=j;
                }
            }
            ans[i]=i+mx;
        }
        int Ans=100000000;
        For(i,0,Mx){
            Ans=min(ans[i],Ans);
        }
        Ans=min(Ans,Mx);*/
        cout<<"Case #"<<x<<": "<<Mx<<endl;
    }
}

