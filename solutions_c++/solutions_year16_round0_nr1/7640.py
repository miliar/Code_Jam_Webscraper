#include <iostream>

using namespace std;

int main()
{
    int test,t,cnt,i,j;
    long long int num,n;
    bool a[11],flag;
    //cout << "Hello world!" << endl;
    cin>>test;
    for(j=1;j<=test;j++){
        cin>>num;
        if(num==0){
            cout<<"Case #"<<j<<": INSOMNIA"<<endl;
        }
        else{
            for(i=0;i<10;i++){
                a[i]=0;
            }
            flag=1;
            i=1;
            cnt=0;
            while(flag){
                n=i*num;
                while (n) { // loop till there's nothing left
                    t = n % 10; // assign the last digit
                    n /= 10; // "right shift" the number
                    if(!a[t]){
                        a[t]=1;
                        cnt++;
                    }
                }
                if(cnt==10){
                    flag=0;
                    cout<<"Case #"<<j<<": "<<i*num<<endl;
                }
                i++;
            }
        }
    }
    return 0;
}

