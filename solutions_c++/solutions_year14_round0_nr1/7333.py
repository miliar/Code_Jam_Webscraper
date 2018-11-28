#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;
int a[17];
ifstream in("in.in");
ofstream out("out.out");
int main(){
    int t;
    in>>t;
    int l=1;
    while(t>0){
        int x,y;
        in>>x;
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                int k;
                in>>k;
                a[k]=i;
            }
        }
        in>>y;
        int index=-1,ans=0;
        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++ ){
                int k;
                in>>k;
                if(i==y){
                    if(a[k]==x){
                        ans++;
                        index=k;
                    }
                }
            }
        }
        if(ans==0){
            out<<"Case #"<<l<<": "<<"Volunteer cheated!"<<endl;
        }
        if(ans==1){
            out<<"Case #"<<l<<": "<<index<<endl;
        }
        if(ans>1){
            out<<"Case #"<<l<<": "<<"Bad magician!"<<endl;
        }
        t--;
        l++;
    }

    return 0;
}
