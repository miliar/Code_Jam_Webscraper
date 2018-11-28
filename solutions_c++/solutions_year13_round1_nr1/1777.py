#include<iostream>
#include<cmath>
//#include<fstream>

using namespace std;
int main(){
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("A-small.txt","w",stdout);
    int t,n,r,i,first;
    double res,D;
    cin>>t;
    for (i=0;i<t;i++){
        cin>>r>>n;
        first=2*r+1;
        D=sqrt((2-first)*(2-first)+8*n);
        res=(2-first+D)/4.0;
        cout<<"Case #"<<i+1<<": "<<floor(res)<<endl;
    }
}
