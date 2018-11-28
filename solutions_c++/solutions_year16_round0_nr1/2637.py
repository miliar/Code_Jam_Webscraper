#include <iostream>
#include <fstream>

using namespace std;

long int last_num_small(long int);
long int output( long int, int);

int main()
{
    int l=1;
    long int data;
    ifstream infile;
    infile.open("A-large.in");
    infile>>data;
    while(infile){
        infile>>data;
        if(!infile.eof()){
            output(data, l);
        }
        l++;
    }
    infile.close();

    return 0;
}

long int output(long int data, int i){
    ofstream outfile;
    outfile.open("output_file2.txt", ios::out | ios::app);

    if(data<=1000000 && data>=0){
        if(last_num_small(data)== -1){
            outfile<<"Case #" << i << ": "<<"INSOMNIA"<<endl;
        }
        else{
            outfile<<"Case #" << i << ": "<<last_num_small(data)<<endl;
        }
    }
    outfile.close();
}

long int last_num_small(long int num){
    long int  new_num=0, last_num=0, last_digit=0, i=0, j=1, k=0, flag=1, A[10];
    for(i=0;i<10;i++){
        A[i]=0;
    }
    new_num = num*j;
    do{
        new_num = num*j;
        last_num = new_num;
        while(new_num != 0){
            flag = 0;
            last_digit = new_num%10;
            new_num = new_num/10;
            A[last_digit]++;
            for(i=0; i<10; i++){
                if(A[i]==0){
                    flag=1;
                    break;
                }
            }

        }
        j++;
        if(j>100){
            return -1;
        }

    }while(flag==1);

    return last_num;
}

