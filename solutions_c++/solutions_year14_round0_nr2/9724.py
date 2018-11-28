#include <iostream>
#include <cstdio>
using namespace std;

/*
1.输入数据 C.F.X
2.
float rate=2;
float sum=C/rate;
if buy:
    rate+=F
    sum+=X/rate;
if not
    sum+=(X-C)/rate;
*/
double minf(double a,double b){
    return a>b?b:a;
}
double minx(double C, double rate, double rx, double F){
    //cout<<rate<<endl;
    if(rx<C) return rx/rate;
    else if(rx/rate<C/rate+rx/(rate+F)) return rx/rate;
    //return minf(C/rate+minx(C,rate,rx-C,F),C/rate+minx(C,rate+F,rx,F));
    return C/rate+minx(C,rate+F,rx,F);
}

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    double C,F,X,T;
    double rate=2;
    //cout<<"Begin:"<<endl;
    cin>>T;
    for(int t=0; t<T; t++){
        //cout<<"round"<<t<<":"<<endl;
        cin>>C>>F>>X;
        rate = 2;
       // cout<<C<<" "<<F<<" "<<X<<endl;
        cout<<"Case #"<<t+1<<": ";
        printf("%.7lf\n",minx(C,rate,X,F));
    }
    return 0;
}




/*
 freopen("A-small-attempt2.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int first;
    int second;
    int arr1[4][4]={};
    int arr2[4][4]={};
    cin>>T;
    for(int i=0; i<T; i++){
        cin>>first;
        for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
                cin>>arr1[j][k];
        cin>>second;
        for(int j=0; j<4; j++)
            for(int k=0; k<4; k++)
                cin>>arr2[j][k];
        int count=0;
        int number=0;
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                if(arr1[first-1][j]==arr2[second-1][k]){
                    count++;
                    number=arr2[second-1][k];
                }
            }
        }

        if(count==1){
            cout<<"Case #"<<i+1<<": "<<number<<endl;
        }else if(count==0){
            cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
        }else{
            cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
        }
    }

*/
