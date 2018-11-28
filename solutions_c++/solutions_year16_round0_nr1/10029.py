#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    freopen("C:/Users/Esam/Desktop/A-small-attempt0.in","r",stdin);
    freopen("C:/Users/Esam/Desktop/output.txt","w",stdout);

    int T;
    cin>>T;

    if(T<0||T>100)
        return 0;

    for(int t=0;t<T;t++)
    {
        cout<<"Case #"<<t+1;

        long int N;
        cin>>N;

        if(N<0||N>1000000)
            break;


        long int i=0;
        long int bitflag=0x0;
        long int returnnumber;

        while (true) {
            i++;
            if(N==0)
            {
                break;
            }
            long int number=N;
            number*=i;
            returnnumber=number;
            long int checkNumber;
            while(number!=0)
            {
                checkNumber=number%10;
                number/=10;
                switch (checkNumber) {
                case 0:
                    bitflag|=0x200;
                    break;
                case 1:
                    bitflag|=0x100;
                    break;
                case 2:
                    bitflag|=0x80;
                    break;
                case 3:
                    bitflag|=0x40;
                    break;
                case 4:
                    bitflag|=0x20;
                    break;
                case 5:
                    bitflag|=0x10;
                    break;
                case 6:
                    bitflag|=0x8;
                    break;
                case 7:
                    bitflag|=0x4;
                    break;
                case 8:
                    bitflag|=0x2;
                    break;
                case 9:
                    bitflag|=0x1;
                    break;
                }
            }
            if(bitflag==1023)
                break;
        }
        if(N==0)
            cout<<": INSOMNIA"<<endl;
        else
        cout<<": "<<returnnumber<<endl;
    }
}
