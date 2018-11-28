#include<iostream>

using namespace std;

int main(){
    long long int n,temp_n,tn;
    long long int t;
    cin>>t;
    for (long long int x=1;x<=t;x++){
        cin>>n;
        if (n==0){
            cout<<"Case #"<<x<<": INSOMNIA"<<"\n";
        }
        else{
            int digits[10];
            for (int i=0;i<10;i++){
                digits[i]=0;
            }
            bool cont=true;
            tn=n;
            while (cont){
                temp_n=tn;
                while (temp_n){
                    int r = temp_n%10;
                    if (digits[r]==0){
                        digits[r]=1;
                    }
                    temp_n=temp_n/10;
                }
                int count=0;
                for (int i=0;i<10;i++){
                    if(digits[i]==1){
                        count++;
                    }
                }
                if (count==10){
                    cont=false;
                }
                else{
                    tn=tn+n;
                }
                //cout<<"Case #"<<x<<": "<<tn<<"\n";
            }
            cout<<"Case #"<<x<<": "<<tn<<"\n";
        }
    }
}

