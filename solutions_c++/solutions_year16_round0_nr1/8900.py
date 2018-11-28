#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<fstream>
#include<cstring>
#include<stack>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<queue>
#include<iomanip>
#define ll long long int
#define eps 1e-9

using namespace std;

int main(){
    int t,cases = 1;
    cin>>t;
    while(t--){
        cout<<"Case #"<<cases++<<": ";
        int num[10] = {0};
        int n;
        cin>>n;
        if(n==0){
            cout<<"INSOMNIA"<<endl;
        }
        else{
            int times = 1;
            while(1){
                int temp = times*n;
                while(temp){
                   num[temp%10] = 1;
                   temp/=10;
                }
                bool flag = 0;
                for(int i=0;i<10;i++){
                    if(num[i] == 0)
                        flag = 1;
                }
                if(!flag){
                    cout<<times*n<<endl;
                    break;
                }
                else
                    times++;
            }
        }
    }
    return 0;
}
