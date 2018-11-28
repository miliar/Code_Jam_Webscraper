#include <iostream>
#include <fstream>

using namespace std;

bool in_array(int,int *,int);
int arrsize(int *);

int main()
{
    int number, numbers[]={0,0,0,0,0,0,0,0,0,0},nsize = sizeof(numbers)/sizeof(numbers[0]), tests, counts=1;
    ifstream fin("A-large.in");
    ofstream fout("data.out",std::ofstream::trunc);

    fin >> tests;
    while(!fin.eof()&&tests){
        fin >> number;
        tests--;
        if(number==0){
            fout << "Case #"<< counts << ": " << "INSOMNIA" << endl;
            counts++;
        } else {
            int tempnum = 0;
            while(in_array(0,numbers,nsize)){
                tempnum+=number;
                int temp = tempnum;
                while(temp>0){
                    numbers[temp%10]++;
                    temp/=10;
                }
            }
            for(int i=0; i<10;i++){
                numbers[i]=0;
            }
            fout << "Case #"<< counts << ": " << tempnum << endl;
            counts++;
        }
    }
    fin.close();
    fout.close();
    return 0;
}
bool in_array(int needle,int *arr,int arrsize){
    for(int i=0; i<arrsize;i++){
        if(needle==arr[i]) return true;
    }
    return false;
}

