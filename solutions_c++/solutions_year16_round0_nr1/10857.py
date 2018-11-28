#include <iostream>
using namespace std;

int main()
{
    int rem=0,t,j,k=0;
    cin >> t;
    k=t;
    while(t--){
        long long int n,i=1,sum=0;
        cin >> n;
        int count[10]={0};
        count[0]=99;
        int m=n;
        int f=10000;
        while(f--){
            int p=m;
            while(m>0){
                rem=m%10;
                m=m/10;
                count[rem]=rem;
            }
            sum=0;
            for(j=0; j<10; j++){
                sum+=count[j];
            }
            if(sum==45 && count[0]==0){
                cout << "Case #" << k-t << ": " << p << endl; 
                break;
            }
            m=n*i;
            i++;
        }
        if(f==-1){
            cout << "Case #" << k-t << ": " << "INSOMNIA" << endl;
        }
    }
}
