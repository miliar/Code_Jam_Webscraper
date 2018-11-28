#include <bits/stdc++.h>
using namespace std;

int main() {

    std::ios::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    long long p,n,pn;
    cin>>t;
    for(int j=1;j<=t;j++)
    {
        cin>>n;
        if(n==0)
        cout<<"Case #"<<j<<": INSOMNIA"<<endl;
        else{
            int d[10]={0};
            int count=0,i=1;
            pn=n;
            while(count<10){
                n=pn*i;
                //cout<<n<<"-";
                p=n;
                while(p>0&&count<10){
                    if(d[p%10]==0){
                        count++;
                        d[p%10]=1;
                    }
                    p=p/10;
                }
                i++;
            }
            cout<<"Case #"<<j<<": "<<n<<endl;
        }
    }
    
	return 0;
}
