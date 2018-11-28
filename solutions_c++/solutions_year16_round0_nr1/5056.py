
#include<iostream>
#include<algorithm>
#include <cstdio>
using namespace std;

bool isAllAppeared(bool filter[10]){
    for (int i=0 ; i<10 ; i++)
        if (!filter[i])return false;
    return true;
}

int addDigits(int N,bool* filter)
{
    int changes = 0;
    if(N >= 10)
       changes += addDigits(N / 10,filter);

    int digit = N % 10;
    if (!filter[digit]){
            filter[digit]=1;
            return changes+1;
    }
    return changes;
}

int main(){
    freopen("output.txt","w",stdout);
    //freopen("in.txt","r",cin);
    int testcases,N,cnt,j,changes;
    bool filter[10];
    cin>>testcases;
    for (int i=0 ; i<testcases ; i++){
        cnt = 0,j=0;
        //memset(filter, 0, sizeof(filter));
        fill_n(filter, 10, 0);
        cin>>N;
        while (!isAllAppeared(filter) && cnt <= 100){
            j++;
           changes = addDigits(N*j,filter);
            if (changes == 0) cnt ++;
        }
        if(i)cout<<endl;
        cout<<"Case #"<<(i+1)<<": ";
        if (isAllAppeared(filter)){
            cout<<j*N;
        }else{
            cout<<"INSOMNIA";
        }
    }
    return 0;
}
