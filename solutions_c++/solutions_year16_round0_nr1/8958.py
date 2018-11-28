#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    long long n;
    cin>>n;

    for(int i=0;i<n;i++){
        long long x;
        cin>>x;
        if(x==0)cout<<"Case #"<<i+1<<": INSOMNIA";
        else {
                vector<int> arr(10);
              long long y=x;
                long long k=1;
              while(true){
                    x=y*k;
                  bool ch=true;
                while(x!=0){
                    int reminder=x%10;
                    x/=10;
                    arr[reminder]=1;
                }
                for(int j=0;j<10;j++){
                    if(arr[j]==0){
                        ch=false;
                        break;
                    }
                }
                if(ch){
                        cout<<"Case #"<<i+1<<": "<<k*y;
                        break;
                }
               k++;
              }

        }
        if(i!=n-1)cout<<endl;
    }

    return 0;
}
