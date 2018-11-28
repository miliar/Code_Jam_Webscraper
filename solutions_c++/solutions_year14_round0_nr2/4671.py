#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<iomanip>

using namespace std;

int main()
{
    int t;
    cin>>t;
    double ep = 0.0000001;
    for (int i = 0; i<t; i++){
        double C, F, X;
        double min = 0.0;
        int j=0;
        double sum,total_sum;

        cin>>C>>F>>X;
        min = X/2;
        sum = 0;
        while(1) {
           sum += C/(2+j*F);
           total_sum = sum + X/(2+(j+1)*F);

           //cout.setf(ios::fixed);
           //cout<<setprecision(7)<<min<<endl;
           //cout.setf(ios::fixed);
           //cout<<setprecision(7)<<total_sum<<endl<<endl;


           if(min - total_sum > ep )  min = total_sum;
           else break;


           j++;
        }

        cout<<"Case #"<<i+1<<": ";
        cout.setf(ios::fixed);
        cout<<setprecision(7)<<min<<endl;
    }
    return 0;
}
