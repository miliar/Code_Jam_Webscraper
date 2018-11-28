#include<iostream>
#include<cstdio>
#include<cstring>

const int MAXN = 1010;

using namespace std;

int N;
char str[MAXN];

int main(){
    
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w", stdout );
    
    int T; cin>>T;
    for(int t=1;t<=T;t++){
            
            cin>>N;
            cin>>str;
            
            int result = 0, sum = str[0]-'0';
            for(int i=1;i<=N;i++){
                    
                    int temp = str[i] - '0';
                    
                    if( (result+sum) < i )
                        result += i - sum - result;
                    
                    sum += temp;
                    }
            
            cout<<"Case #"<<t<<": "<<result<<'\n';
            }
    
    return 0;
}
