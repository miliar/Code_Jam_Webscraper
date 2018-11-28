#include <iostream>
#include <cstring>

using namespace std;
int a[10]={0,0,0,0,0,0,0,0,0,0};
void put(int temp){
    if( a[temp]==0){
        a[temp]=1;
    }
}
int check(){
    for(int i=0;i<10;i++){
        if(a[i]==0){
            return 0;
        }
    }
    return 1;
}
void breakit(long int n){
    int temp;
    int b=n;
    while(b>0){
        temp=b%10;
        b=b/10;
        put(temp);
    }
}
int main()
{
    int t,te,flag=1,call;
    long int n,m;
    std::cin>>t;
    te=t;
    int i=1;
    cin.ignore();
    while(te>0){
        std::cin>>n;
        flag=1;
        i=1;
        for(int j=0;j<10;j++){
            a[j]=0;
        }
        m=n;
        while(flag<1000){
            n=i*m;
            breakit(n);
            call=check();
            if(call==1){
                break;
            }
            i++;


            flag++;
        }
        std::cout<<"Case #"<<t-te+1<<": ";
        if(flag==1000){
            std::cout<<"INSOMNIA"<<endl;
        }
        else{
            std::cout<<n<<endl;
        }
        te--;
    }
    return 0;
}
