#include<bits/stdc++.h>
using namespace std;

int main(){

    int t;
    ofstream out;
    ifstream in;
    out.open("OutLarge.txt");
    in.open("B-large.in");
    in>>t;
    for(int i=0;i<t;i++){

        int count=0;
        int strcount=0;
        string input, newstr="";
        in>>input;

        for(int j=0;j<input.size()-1;j++){

                if(input[j]!=input[j+1]){
                    newstr += input[j];
                    strcount++;
                }
//
        }
        newstr+=input[input.size()-1];
        input="";
        input=newstr;

        if(input=="-"){
                    count=1;

            }

        for(int j=0;j<input.size()-1;j++){

            if(input[j]==input[j+1])
                continue;
            else{
                if(input[j]=='-'){
                 count++;
                }else{
                    count+=2;j++;
                }
            }
        }
        out<<"Case #"<<i+1<<": "<<count<<endl;
    }
    return 0;
}
