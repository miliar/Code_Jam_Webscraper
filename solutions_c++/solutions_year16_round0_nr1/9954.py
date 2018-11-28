#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int t,x,i,j,k;
    long long y;
    int check[10];

    ifstream ins;
    ofstream outs;

    ins.open("q1.in",ios::in);
    outs.open("q1.out",ios::out);

    string str;
    ins>>t;
    for(i=1;i<=t;++i)
    {
        str="SLEEP";
        for(j=0;j<10;++j)
            check[j]=0;
        ins>>x;
        for(j=1;;++j)
        {
            y=j*x;
            for(k=y;k!=0;k/=10)
                check[k%10]=1;
            for(k=0;k<10;++k)
                if(check[k]==0){break;}
            if(k==10){break;}
            if(y==0){str="INSOMNIA";break;}
        }
        if(str=="SLEEP"){outs<<"Case #"<<i<<": "<<y<<endl;}
        else{outs<<"Case #"<<i<<": "<<str<<endl;}
    }
    return 0;
}
