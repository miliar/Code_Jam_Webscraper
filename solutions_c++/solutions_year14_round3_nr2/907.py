#include <iostream>
#include <string>
using namespace std;
long long array[10] = {0,1,2,3,4,5,6,7,8,9};
long long count=0;
void swap(long long x, long long y){
    long long temp = array[x];
    array[x]=array[y];
    array[y]=temp;

    return;
}

string printArray(long long size, string * str_arr){
    long long i;
    string per="";
    for (i=0;i<size;i++)
        per+=str_arr[(array[i])];
    //cout<<per<<endl;
    return per;
}
void check(string str){
    long long ch[26];
    for(long long i=0; i<26; i++){
        ch[i]=0;
    }
    char old;
    bool thro=false;
    for(long long i=0; i<str.length(); i++){
        char chr=str[i];
        if(i==0){
            ch[chr-97]++;
            old=chr;
        }
        else if(chr==old){
            ch[chr-97]++;
        }
        else if(ch[chr-97]!=0){
            thro=true;
            break;
        }
            
        else {
            ch[chr-97]++;
            old=chr;
        }
    }
    if(!thro)
    count++;
}

void permute(long long k,long long size, string * str_arr){
    long long i;

    if (k==0){
        check(printArray(size, str_arr));
    }
    else{
        for (i=k-1;i>=0;i--){
            swap(i,k-1);
            permute(k-1,size, str_arr);
            swap(i,k-1);
        }
    }

    return;
}

int main(){
    long long ntest;
    cin>>ntest;
    for(long long test=0; test<ntest; test++){
        long long n;
        cin>>n;
        string str_arr[n];
        count=0;
        for(long long i=0; i<n; i++){
            cin>>str_arr[i];
        }
        permute(n,n,str_arr);
        cout<<"Case #"<<test+1<<": "<<count%1000000007<<endl;
    }
}