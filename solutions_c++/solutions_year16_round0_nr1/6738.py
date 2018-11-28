#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);

    unsigned long long n,t,i,ans,c=1,num,j;
    int digits[11];
    cin>>t;
    while(t--){
        cin>>n;
        if(n==0){
            cout<<"Case #"<<c++<<": INSOMNIA\n";
        }
        else{

            for(i=0;i<10;i++)
                digits[i]=0;

            for(i=1;i<=100;i++){
                num=i*n;
                while(num>0){
                    digits[num%10]=1;
                    num=num/10;
                }
                ans=0;
                for(j=0;j<10;j++)
                    ans+=digits[j];
                if(ans==10){
                    cout<<"Case #"<<c++<<": "<<i*n<<"\n";
                    ans=-1;
                    break;
                }
            }
            if(ans!=-1){
                cout<<"Case #"<<c++<<": INSOMNIA\n";
            }
        }
    }
    return 0;
}
