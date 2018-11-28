#include <iostream>

using namespace std;
int A[10];
void init(){
    for(int j=0;j<=9;j++){
        A[j]=0;
    }
}
int check(){
    if(A[0]==1&&A[1]==1&&A[2]==1&&A[3]==1&&A[4]==1&&A[5]==1&&A[6]==1&&A[7]==1&&A[8]==1&&A[9]==1){
        return 1;
    }
    return 0;
}
int main()
{
    int T;
    cin>>T;
    for(int i=1;i<=T;i++){
        int pass=0;
        long long N;
        init();
        cin>>N;
        int r;
        r=1000000;

        for(int k=1;k<=r;k++){
            int temp = k*N;
            //cout<<temp<<endl;
            A[temp %10]=1;
            if((temp/10)!=0)
            A[(temp/10)%10]=1;
            if((temp/100)!=0)
            A[(temp/100)%10]=1;
            if((temp/1000)!=0)
            A[(temp/1000)%10]=1;
            if((temp/10000)!=0)
            A[(temp/10000)%10]=1;
            if((temp/100000)!=0)
            A[(temp/100000)%10]=1;
            if((temp/1000000)!=0)
            A[(temp/1000000)%10]=1;
            //cout<<temp<<"->"<<temp %10<<" "<<(temp/10)%10<<" "<<(temp/100)%10<<endl;
            if(check()){
                cout<<"Case #"<<i<<": "<<temp<<endl;
                pass=1;
                break;
            }
        }
        if(pass==0)
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
    }

    return 0;
}
