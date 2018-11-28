#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;


int main(){

    int T;
    cin>>T;
    int k=0;

    while(T--){
        k++;

        char str[105];
        cin>>str;

        int l = strlen(str);

        long long int count =0;

        for(int i=0;i<l;){

            if(str[i]=='+'){
                while(str[i]=='+'){
                    i++;
                }
                if(i<l){
                    count++;
                }
            }
            if(str[i]=='-'){
                while(str[i]=='-') {
                    i++;
                }

                count++;
            }
        }
        cout <<"Case #"<<k<<": "<<count<<endl;
    }


    return 0;
}