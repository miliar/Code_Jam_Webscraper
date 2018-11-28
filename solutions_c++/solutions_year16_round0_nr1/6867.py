#include <iostream>

using namespace std;

int main()
{
    long long int t,i,j,ans;
    cin>>t;
    long long int n;
    for(int k=1;k<=t;k++){
        int count1=0;
        int a[10]={0},c;
        cin>>n;
        if(n==0){
            cout<<"Case #"<<k<<": INSOMNIA"<<endl;
        }
        else{
        for(i=1;;i++){
            j=i*n;
            ans=j;
            while(j){
                c=j%10;
                if(a[c]==0){
                    a[c]++;
                    count1++;
                }
                j=j/10;
            }
            if(count1==10){
                cout<<"Case #"<<k<<": "<<ans<<endl;
                break;
            }
        }
        }
    }
    return 0;
}
