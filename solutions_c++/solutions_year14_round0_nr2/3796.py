#include<iomanip>
#include<iostream>
#include<stdio.h>
#define max 100
using namespace std;
int main(){
    cout<<fixed<<setprecision(7);
    int testcases;
    int finish = 0,cnt = 0;
    double result[max];
    double Time,C,F,X,rate= 0.0,gtime = 0.0,cookies= 0.0;
    freopen("B-large.in","r",stdin);
    freopen("cookieout.txt","w",stdout);
    cin>>testcases;
    int testcasesran = 0;
    while(testcasesran < testcases){
        cin>>C;
        cin>>F;
        cin>>X;
        cookies = C;
        rate = 2.0;
        finish = 0;
        gtime = 0.0;
        result[cnt] = 0.0;
            while(finish == 0){
                    if((X-cookies)/rate > ((X-cookies)+C)/(rate+F)){
                        Time = double(cookies)/rate;
                        gtime = gtime + Time;
                        //cout << "gtime1 = " << Time<<endl;
                        rate = rate+F;
                    }
                    else{
                        Time = double(X)/rate;
                        //cout << Time;
                        gtime = gtime + double(Time);
                        result[cnt] = gtime;
                        //cout << "gtime2 = " << gtime<<endl;
                        finish = 1;

                    }
            cookies = C;
            }
    cnt++;
    testcasesran++;
    }


    for(int i=0;i<testcases;i++){
        //std::cout.precision(7);
        cout<<"Case #"<<i+1<<": "<<result[i]<<endl;
    }
    return 0;
}
