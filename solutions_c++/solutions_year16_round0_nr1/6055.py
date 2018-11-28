//this is for proble a
#include <iostream>
using namespace std;
int main() {
    int T;
    cin>>T;
    int Thold=T;
    while(T>0){
        int temp=0;
        int rec=0;
        bool got0=false;
        bool got1=false;
        bool got2=false;
        bool got3=false;
        bool got4=false;
        bool got5=false;
        bool got6=false;
        bool got7=false;
        bool got8=false;
        bool got9=false;
        bool done=false;
        int n;
        cin>>n;
        if(n==0){
            cout<<"Case #"<<Thold-T+1<<": "<<"INSOMNIA"<<endl;
        }
        else{
            for(int i=1;i<91;i++){
                int product=n*i;
                while(product!=0){
                    temp=product%10;
                    product/=10;
                    switch(temp){
                    case 0:
                        got0=true;
                        break;
                    case 1:
                        got1=true;
                        break;
                    case 2:
                        got2=true;
                        break;
                    case 3:
                        got3=true;
                        break;
                    case 4:
                        got4=true;
                        break;
                    case 5:
                        got5=true;
                        break;
                    case 6:
                        got6=true;
                        break;
                    case 7:
                        got7=true;
                        break;
                    case 8:
                        got8=true;
                        break;
                    case 9:
                        got9=true;
                        break;
                }
                    done=got0&&got1&&got2&&got3&&got4&&got5&&got6&&got7&&got8&&got9;
                    if(done)
                        break;
                }
                if(done){
                    rec=n*i;
                    break;
                }
            }
            cout<<"Case #"<<Thold-T+1<<": "<<rec<<endl;
        }
        
        T--;
    }
    return 0;
}
