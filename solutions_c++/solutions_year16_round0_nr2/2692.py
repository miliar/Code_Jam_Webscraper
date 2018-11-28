#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
using namespace std;
void flip(char*);
void swap_values(char*, char*);
int result(char *);
void out_file(int,int);
int main(){

    int i=0;
    ifstream infile;
    infile.open("B-large.in");
    string data;
    infile>>data;
    while(infile){
        infile>>data;
        if(!infile.eof()){
            i++;
            char *new_data = &data[0];
            out_file(result(new_data),i);
        }
    }
    infile.close();
    return 0;
}

void out_file(int a,int i){
    ofstream outfile;
    outfile.open("output_file.txt", ios::out | ios::app);
    outfile<<"Case #"<<i<<": "<<a<<endl;
    outfile.close();
}

void flip(char *a){
    a[0] = (a[0]=='+')?'-':'+';
}

void swap_values(char *a, char *b){
    char temp;
    temp = a[0];
    a[0] = b[0];
    b[0] = temp;
}

int result(char *data){
    int len,i=0,j=-1,k=0,flag=0,check=1,check2=0,l=0;
    len = strlen(data);
    for(i=len-1; i>=0; i--){
        check=1;
        for(j=0;j<len;j++){
            if(data[j]!='+'){
                check=0;
                break;
            }
        }
        if(check==1){
            break;
        }
        if(data[i]=='+'){
            continue;
        }
        k=0;
        j=-1;
        for(j=0; data[j]=='+'; j++){
            flip(&data[j]);
        }
        if(j>0){
            //cout<<data<<endl;
            flag++;
        }

        if(data[i]=='-'){
            if(i%2==0){
                for(j=0;j<=(i/2);j++){
                    swap_values(&data[j], &data[i-j]);
                    flip(&data[j]);
                    flip(&data[i-j]);
                }
                flip(&data[i/2]);
            }
            else{
                for(j=0;j<=(i/2);j++){
                    swap_values(&data[j], &data[i-j]);
                    flip(&data[j]);
                    flip(&data[i-j]);
                }
            }
            //cout<<data<<endl;
            flag++;
        }

        check=1;
        for(j=0;j<len;j++){
            if(data[j]!='+'){
                check=0;
                break;
            }
        }
        if(check==1){
            break;
        }

        l=0;
        check2=0;
        for(j=0;j<i;j++){
            if(data[j]=='-'){
                if(l==1){
                    check2=1;
                }
            }
            else{
                l=1;
            }
        }


        if(check2==0){
            for(j=0;data[j]=='-';j++){
                flip(&data[j]);
            }
            //cout<<data<<endl;
            flag++;
        }

    }
    return flag;
}
