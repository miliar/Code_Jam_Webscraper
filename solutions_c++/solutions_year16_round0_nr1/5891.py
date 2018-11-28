#include <iostream>
#include <stdio.h>
#include <map>
#define MAX (int)1e4
using namespace std;
int main(){
freopen("A-large.in","r",stdin);
  freopen("out_large.out","w",stdout);
    int T,cs = 1;
    cin >> T;
    while(T--){
        int N,count = 0,A[10] = {0},j = -1;
        long long temp;
        cin >> N;
        for(int i = 1;i < MAX;i++){
            temp = N*i;
         //   cout<<temp<<endl;
            while(temp){
            int x = temp%10;
                count+=(!A[x]);
                A[x]++;
                temp/=10;
                if(count == 10)
                break;
            }
            if(count == 10){
            j = i;
                break;
           }
        }
        cout<<"Case #"<<cs++<<": ";
        if(j == -1)
        cout<<"INSOMNIA\n";
        else cout<<N*j<<'\n';
    }

    return 0;
}
