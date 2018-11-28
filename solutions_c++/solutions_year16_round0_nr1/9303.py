#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int t,n,i,j,k,a[10];
    bool flag;
    freopen("A2.txt","r",stdin);
    freopen("out_A2.txt","w",stdout);
    cin>>t;
    for(int c=1;c<=t;c++){
        cin>>n;
        for(i=0;i<10;i++)
            a[i]=0;
        flag = false;
        k=n;
        if(n==0)
            cout<<"case #"<<c<<": INSOMNIA"<<endl;
        while(n!=0 && !flag){
            j=n;
            while(j){
                i=j%10;
                ++a[i];
                j=j/10;
            }
            flag=true;
            for(i=0;i<10;i++)
                if(a[i]==0){
                flag=false;
            }
            if(flag)
                    cout<<"case #"<<c<<": "<<n<<endl;
            else
                n=k+n;
        }
    }
return 0;
}
