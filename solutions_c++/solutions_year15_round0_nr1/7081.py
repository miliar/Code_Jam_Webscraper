#include<iostream>
#include<algorithm>
#include<cstdio>
using namespace std;

int main()
{
    int i,j,t,smax,standed = 0,cnt = 0,addition = 0;
    char str[1005] = {0};
    freopen("A-large.in","r",stdin);
    freopen("large.out","w",stdout);
    cin>>t;
    while(t--){
        cin>>smax>>str;
        standed = 0;
        addition = 0;
        for(int i = 0; i <= smax; i++){
            if(standed < i&&str[i]-'0' > 0){
                addition += i - standed;
                standed += i - standed;
            }
            standed += str[i]-'0';
            //cout<<standed<<' '<<addition<<endl;
        }
        cout<<"Case #"<<++cnt<<": "<<addition<<endl;
    }
    return 0;
}
