#include<iostream>
#include<math.h>
#include<algorithm>
#include<cstdio>
#include<string>
#include<fstream>
using namespace std;
int arr[100][100];
int main()
{
    ifstream istr;
    ofstream ef;
    ef.open("ans.txt");
    istr.open("1.txt");
    int t,test,n,m,i,j,k;
    istr>>t;
    for(test=1;test<=t;test++){
                               ef<<"Case #"<<test<<": ";
                               istr>>n>>m;
                               for(i=0;i<n;i++){
                                                for(j=0;j<m;j++){
                                                                 istr>>arr[i][j];
                                                }
                               }
                               bool flag=1;
                               for(i=0;i<n && flag==1;i++){
                                                for(j=0;j<m;j++){
                                                                 flag=1;
                                                                 for(k=0;k<m;k++){
                                                                                  if(arr[i][k]>arr[i][j]){
                                                                                                          flag=0;
                                                                                                          break;
                                                                                  }
                                                                 }
                                                                 if(flag==0){
                                                                             flag=1;
                                                                            for(k=0;k<n;k++){
                                                                                             if(arr[k][j]>arr[i][j]){
                                                                                                                     flag=0;
                                                                                                                     break;
                                                                                             }
                                                                            } 
                                                                 }
                                                                 if(flag==0){
                                                                             ef<<"NO\n";
                                                                             break;
                                                                 }
                                                }
                               }
                               if(flag==1){
                                           ef<<"YES\n";
                               }
    }
    istr.close();
    ef.close();
   system("pause");
   return 0;
}
