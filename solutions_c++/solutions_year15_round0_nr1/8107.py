#include<iostream>
#include<string>
using namespace std;


int main(int arg_count, char *arg[]){

    int no_test;
    string a;
    int smax=0,i;
    cin >> no_test;
    int k=0;
    while(no_test--){

        cin >> smax;
        cin >> a;
        //length=a.length();
        int cnt=0;
        int sum=0;
        for(i=0;i<smax+1;i++){
            int c=a[i]-'0';

                if(sum>=i){
                    sum+= c;
                }
                else{
                    cnt+=i-sum;
                    sum+=i-sum;
                    sum+=c;

                }
        }
        cout <<"Case #"<<k+1<<": "<<  cnt << endl;
        k++;
    }

return 0;
}
