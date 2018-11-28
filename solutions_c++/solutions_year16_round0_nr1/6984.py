#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.txt");
    int T,count=0,l=0;
    int a[10];
    long long int num,dfind,digit,k=1,temp;
    fin>>T;
    while(l<T){
        fin>>num;
        if(num==0){
           fout<<"Case #"<<l+1<<": INSOMNIA\n";
        }
        else{
            while(count!=10){
                dfind=k*num;
                temp=dfind;
                while(temp){
                    digit=temp%10;
                    if(a[digit]==0){
                        a[digit]=1;
                        count++;
                    }
                    temp=temp/10;
                    }
                    if(count==10){
                        fout<<"Case #"<<l+1<<": "<<dfind<<"\n";
                }
                k++;
            }

        }
        l++;
        k=1;
    count=0;

    for(int i=0;i<10;i++){
        a[i]=0;
    }
    }
    return 0;
}
