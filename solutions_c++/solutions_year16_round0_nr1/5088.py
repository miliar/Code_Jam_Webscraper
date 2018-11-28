#include <iostream>
#include <fstream>
using namespace std;
long long n, T;
bool a[10];
int main()
{   freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>T;
    int l = 1;
    while(T){
            bool flag = true;
        T--;

        cin>>n;
        cout<<"Case #"<<l<<": ";
        l++;
        if(n==0){
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        for(int i=0; i<10; i++){
            a[i] = false;
        }
        long long m;
        long long t;
        for(int i=1; i<=1000; i++){
            flag = true;
            t = i*n;
            m = t;
            while(t>0){
                a[t%10] = true;
                t /= 10;
            }
            for(int l1=0; l1<10; l1++){
                if(!a[l1])   flag = false;
            }
            if(flag==true)  break;
        }
        if(flag)    cout<<m<<endl;
    }

    return 0;
}
