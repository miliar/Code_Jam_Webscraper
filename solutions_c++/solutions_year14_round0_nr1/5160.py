#include<iostream>
using namespace std;

int main() {
    freopen( "A-small-attempt0.in", "r", stdin );
    freopen( "A-small-attempt0.out", "w", stdout );
    int T,a[4][4],b[4][4],ans1,ans2,i,j,found,chosen,k=1;
    cin>>T;
    while(T--) {
               found=0;
               cin>>ans1;
               for(i=0;i<4;i++) {
                               for(j=0;j<4;j++)
                                               cin>>a[i][j];
               }
               cin>>ans2;
               for(i=0;i<4;i++) {
                               for(j=0;j<4;j++)
                                               cin>>b[i][j];
               }
               for(i=0;i<4;i++) {
                                for(j=0;j<4;j++) {
                                                 if(a[ans1-1][i]==b[ans2-1][j]) {
                                                       found++;
                                                       chosen=a[ans1-1][i];
                                                 }
                                }
               }
               if(found==0)   cout<<"Case #"<<k<<": Volunteer cheated!\n";  
               else if(found==1)            cout<<"Case #"<<k<<": "<<chosen<<"\n";
               else            cout<<"Case #"<<k<<": Bad magician!\n";
               k++;
    }
    return 0;
}
