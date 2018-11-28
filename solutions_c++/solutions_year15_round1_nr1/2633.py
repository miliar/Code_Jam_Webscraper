#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    int t;
    cin>>t;
    int n=t;
    while(t--){
        int d=0;
        vector<int>v;
        int x;
        int ant;
        int m=0;
        int l;
        int p=0;

        cin>>l;
        for(int i=0;i<l;i++){
            cin>>x;
            v.push_back(x);
            if(i==0){
                ant = x;
            }
            if(ant-x>0){
                p+=(ant-x);
                m = max(m,(ant-x));
            }
            ant = x;
        }


        for(int i=0;i<l-1;i++){
            if(v[i]<m){

                    d+=v[i];
            }
            else d+=m;
        }
        cout<<"Case #"<<(n-t)<<": "<<p<<" "<<d<<endl;
    }
    return 0;
}
