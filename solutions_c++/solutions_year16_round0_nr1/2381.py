#include<iostream>
#include<cstdio>
#include<cstring>
#define MAX 1000001
#define FULL ((1<<10) - 1)
using namespace std;
short a[MAX];
int main()
{
    long long x;
    int cas;
   // freopen("A-large.in","r",stdin);
  //  freopen("Aout.txt","w",stdout);
    for(int i = 1 ;i < MAX ;i++){
        int t =i;
        while(t){
            int t1 = t%10;
            a[i]|= (1<<t1);
            t/=10;
        }
    }
    cin>>cas;
    for(int q=1;q<=cas;q++){
        cin>>x;

        short o = 0;
        int i = 1;
        cout<<"Case #"<<q<<": ";
        if(x==0){
            cout<<"INSOMNIA"<<endl;
            continue;
        }
        while(true){
            long long t = i*x;
            if(t < MAX){
                o|=a[t];
            }
            else{
                while(t){
                    o|=(1<<(t%10));
                    t/=10;
                }
            }
            if(o == FULL){
                cout<<i*x<<endl;
                    break;
            }
            i++;
        }

    }
    return 0;
}
