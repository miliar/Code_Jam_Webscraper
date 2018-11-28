#include<iostream>
#include<fstream>
using namespace std;
int main(){

    int T, flag = 0, N, a;
    int arr[10];
    long long ans = 0, temp, counter = 1;

    ofstream outf("output.txt");
    ifstream inf("A-large.in");

    inf>>T;


    for(int  i = 1; i <= T; ++i){

    for(int i = 0; i < 10; ++i)
        arr[i] = 0;
        flag = 0;
        counter = 1;
        ans = 0;
        inf>>N;

        if(N == 0)
            flag = 1;

        if(flag == 0){

            while(true){

                ans = N * counter;
                ++counter;
                temp = ans;
                while(temp){
                    arr[temp%10] = 1;
                    temp /= 10;
                }
                a = 1;
                for(int i = 0; i < 10; ++i)
                    if(arr[i] == 0)
                        a = 0;
                if(a == 1)
                    break;
            }
        }

        if(flag == 1)
            outf<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
            outf<<"Case #"<<i<<": "<<ans<<endl;
    }
    outf.close();


}
