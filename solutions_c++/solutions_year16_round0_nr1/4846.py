#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main(){
    long t,c_n;
    cin>>t; c_n = 1;
    int n;
    while(t--){
        cout<<"Case #"<<c_n<<":";
        c_n++;
        cin>>n;
        if(n == 0)
            cout<<" INSOMNIA"<<endl;
        else{
            vector<bool> sat(10,false);
            long  full=0;
            long i=1;
            while(full < 10){
                long temp = i*n;
                while(temp){
                    long x = temp%10;
                    if(sat[x] == false){
                        full++;
                        sat[x] = true;
                    }
                    temp /= 10;
                }
                if(full == 10)
                    cout<<" "<<i*n<<endl;
                i++;
            }
        }

    }
}
