#include <iostream>
#include <string>
using namespace std;
int main() {
    ios::sync_with_stdio(false);
    int number;
    int output[100];
     int Smax;
    cin>>number;
    string s;
    for (int j=0;j<number;j++){

    cin>>Smax;
    cin>>s;
    int out=0;
    int temp=0;
    for (int i=0;i<Smax+1;i++)
    {
        if((temp<i)&&(s[i]-'0')){
            out=out+i-temp;
            temp=i;
        }

            temp=temp+s[i]-'0';
    }
    output[j]=out;

    }
    for (int i=0;i<number;i++){
    cout<<" Case #"<<(i+1)<<": "<<output[i]<<endl;
    }
    return 0;
    }
