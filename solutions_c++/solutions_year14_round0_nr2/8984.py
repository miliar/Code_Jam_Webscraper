#include <iostream>
#include<string>
#include<vector>
#include<cstring>
#include<sstream>
#include <fstream>

using namespace std;


double recurse(double C,double F,double X,double L){
    if(X/L<=((C/L)+(X/(L+F)))){
        return X/L*1.0;
    }

    return C/L*1.0+recurse(C,F,X,L+F);
}
void compute(int caseNum){
    double C,F,X;
    cin>>C>>F>>X;
    cout.precision(7);
    cout.setf( std::ios::fixed, std:: ios::floatfield ); 
    cout<<"Case #"<<caseNum<<": ";
    cout<<recurse(C,F,X,2)<<endl;
}

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;){
        compute(++i);
    };
    return 0;
}

