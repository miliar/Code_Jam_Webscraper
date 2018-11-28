#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
int main()
{
    long long int t,n;
    ifstream fin;
    ofstream fout;
    fin.open("input1.in");
    fout.open("output1.txt");
    fin>>t;
    for(int i=1;i<=t;i++){
        long long int count = 0,p = 1,rem=0,z=0,c=0;
        fin>>n;
        if(n==0){
             if(i==1)
                fout<<"Case #"<<i<<": "<<"INSOMNIA";
            else
                fout<<"\nCase #"<<i<<": "<<"INSOMNIA";
        }else{
        long long int a[10] = {0};
        long long int d=n;
        while(count<10){
        count=0;
            n=d*p;
            z=n;
            //cout<<z<<" ";
            while(n!=0){
                rem = n%10;
                n=n/10;
                a[rem] = 1;
               // cout<<a[rem]<<" ";

            }

            for(int j=0;j<10;j++){
                if(a[j]==1){
                    count++;
                }
            }
            p++;

        }
        if(i==1)
        fout<<"Case #"<<i<<": "<<(p-1)*d;
        else
            fout<<"\nCase #"<<i<<": "<<(p-1)*d;
        }
    }
    //return 0;
}
