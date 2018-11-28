#include <iostream>
using namespace std;

int main()
{
    int t,p=0;
    cin>>t;
    while(t--){++p;
        int n,i;
        cin>>n;
        int a[10]={0};
        if(n>0){
        for(i=1;;i++){
            long int k;
            k=i*n;
            do{
                int d=k%10;
                k=k/10;
                a[d]++;
            }while(k>0);
            for(int j=0;j<10;j++){
                if(a[j]==0)
                break;
                if(j==9){
                    i=i*n;
                    k=1;break;
                }
            }
            if(k==1)
            break;
        }
        cout<<"Case #"<<p<<": "<<i<<endl;
        }
        else
        cout<<"Case #"<<p<<": INSOMNIA"<<endl;
    }
    return 0;
}
