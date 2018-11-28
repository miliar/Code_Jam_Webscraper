#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;
    int x = 0;
    do{
        int n,c=0;
        cin>>n;
        char str[n+1];
        memset(str,'0',n+1);
        for(int i =0;i<n+1;i++){
           cin>>str[i];
        }
        int sum = 0;
        for(int i = 0;i<n+1;i++){
             if(sum<i){
                c+=i-sum;
                sum+=i-sum;
            }
            sum+=str[i]-'0';
        }
        cout<<"Case #"<<x+1<<": "<<c<<endl;
        x++;
    }while(x<t);
    cout<<"\n";

return 0;
}

