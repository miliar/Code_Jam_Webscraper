#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iomanip> 
using namespace std;

char map[100][100];
int r , c , n ;
int transpose;

void work(int cnt){
    double c , f , x ;
    cin>>c>>f>>x;
    cout<<"Case #"<<cnt<<": ";
    if ( c*f <= 1e-7 ||
        x<=c || f<=-2.0*c/(c-x) ){
            cout<<std::setprecision(10)<<(x/2.0)<<endl;
            return;
        }
    double lim = (-2*c-c*f+f*x)/(c*f)  ;
    double time = 0 ;
    for ( int i = 0 ; i <= int(lim) ; ++i ){
        time += c/(2+i*f);
        //cerr<<c/(2+i*f)<<endl;
    }
    time += x/(2+f*int(lim+1));
    //cerr<<x/(2+f*int(lim+1))<<endl;
    
    cout<<std::setprecision(13)<<time<<endl;
    //cerr<<"Limit: "<<lim<<endl;
}

int main(){
    int t ;
    scanf("%d",&t);
    for ( int i = 0 ; i < t ; ++i ){
        work(i+1);
    }
}
