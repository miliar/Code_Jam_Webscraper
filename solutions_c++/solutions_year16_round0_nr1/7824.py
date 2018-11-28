#include<iostream>
#include<cstring>
using namespace std;
#define SIZE 2000000
int digit=0,digittmp=0;
void mul(short a[],int b,short c[]){
    int carry=0;
    int col=0;
    while(b!=0){
        int num = b%10;
        if(num !=0){
            for(int i=col;i<digit;i++){
                c[i] += a[i-col]*num;
            }
        }
        b/=10;
        col++;
        if(col>=1 && b!=0){
            digit++;
        }
    }
    // shift
    for(int i=0;i<digit;i++){
        if(c[i] >=0){
            c[i]+=carry;
            carry = c[i]/10;
            c[i] = c[i]%10;
            if(i == digit-1 && carry>0){
                digit++;
            }
        }
    }
}

int main(){
    int t;
    long long num;
    cin>>t;
    short arr[SIZE];
    short c[SIZE];
    short l[10];
    for(int a=1;a<=t;a++){
        int cnt = 10,multi=1;
        digit =0;
        memset(l,0,sizeof(l));
        memset(arr,0,sizeof(arr));
        cin>>num;
        if(num == 0) {
            cout<<"Case #"<< a <<": INSOMNIA";
            cout<<endl;
            continue;
        } else {
            int z=0;
            // num to arr
            while(num){
                arr[z++] = num%10;
                digit++;
                num/=10;
            }
            // compute
            digittmp = digit;
            while( cnt != 0){
                digit = digittmp;
                memset(c,0,sizeof(c));
                mul(arr,multi++,c);

                for(int i=0;i<digit;i++){
                    if(l[c[i]] == 0){
                        l[c[i]]++;
                        cnt--;
                    }
                }
                if(multi >= 1000) {
                    cout<<"Case #"<< a <<": INSOMNIA";
                    cout<<endl;
                    break;
                }
            }

        }
        if(multi >=1000){
            continue;
        }
        cout<<"Case #"<< a <<": ";
        for(int i=digit-1;i>=0;i--){
            cout<<c[i];
        }
        cout<<endl;
    }
}
