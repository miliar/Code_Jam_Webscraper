#include <cstdlib>
#include <iostream>
#define N 4 // square
using namespace std;

int main(int argc, char *argv[])
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t=0; // testcases;
    int ans1=0,ans2=0;
    cin>>t;
    //cout<<"t="<<t<<endl;
    int a[N]={0};
    int cnt=0; // 0: cheated 1: ret 1<=: bad
    int ret=0; 
    for(int i=0; i<t; i++){
             cnt=0;
             ret=0;
             cin>>ans1;
             //cout<<"ans1="<<ans1<<endl;
             for(int j=0;j<N*(ans1-1);j++){
                     int x;
                     cin>>x;
             }
             for(int j=0;j<N;j++){
                     cin>>a[j];
             }
             for(int j=0;j<N*(N-ans1);j++){
                     int x;
                     cin>>x;
             }
             
             cin>>ans2;
             //cout<<"ans2="<<ans2<<endl;
             for(int j=0;j<N*(ans2-1);j++){
                     int x;
                     cin>>x;
             }
             for(int j=0;j<N;j++){
                     int x=0;
                     cin>>x;
                     for(int k=0;k<N;k++){
                             if(a[k]==x){
                                         if(ret!=x){
                                                   ret=x;
                                                   cnt++;
                                         }
                             }
                     }
             }
             for(int j=0;j<N*(N-ans2);j++){
                     int x;
                     cin>>x;
             }
             //ret
             if(cnt==0){
                        cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
             }
             else if(cnt==1){
                  cout<<"Case #"<<i+1<<": "<<ret<<endl;
             }
             else{
                  cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
             }
             
    }
    //system("PAUSE");
    return EXIT_SUCCESS;
}
