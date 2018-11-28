#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <fstream>

using namespace std;


int num_f(char* str){
    //cout<<"str:"<<str<<endl;
    int count = 0;
    //char ch;
    int sum = 0;
    int len = strlen(str);
    //int len = str.length();
    for(int i=0; i<len; i++){
        sum += (int)str[i]-(int)'0';
        if(i-sum>=0){
            count += (i-sum+1);
            sum += (i-sum+1);
        }
    }
    return count;
}


int main(){
    int n;
    if(!(cin>>n))
        return -1;
    //char s[1000];
    char s[5];
    char* pch;
    int len = 0;
    ofstream fo;
    fo.open("out_a.txt");
    for(int i=0; i<n; i++){
        cin>>s;
        len = atoi(s);
        char ss[len+1];
        cin>>ss;
        //cout<<"string:"<<s<<endl;
        //pch = strtok(s, " ");
        //pch = strtok(NULL, " ");
        cout<<"Case #"<<i+1<<": "<<num_f(ss)<<endl;
        fo<<"Case #"<<i+1<<": "<<num_f(ss)<<endl;
    }
    fo.close();
    return 0;
}
