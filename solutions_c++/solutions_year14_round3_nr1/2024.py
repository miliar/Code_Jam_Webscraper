#include <iostream>
#include<fstream>

using namespace std;

bool ping(long long int *a, long long int num){
    for(int i=0;i<43;i++){
        if(a[i]==num){
            return true;
        }
    }
    return false;
}


int main()
{


    long long int a[43] = {1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648,4294967296,8589934592,17179869184,34359738368,68719476736,137438953472,274877906944,549755813888,1099511627776, 2199023255552, 4398046511104};
//    long long int *arr = new long long int[42];
    int t,tt;
    ifstream f1;
    ofstream f2;
    f1.open("input2.txt");
    f2.open("output.txt");
    long long int p,q;
    f1>>t;
    tt=1;
    char ch;
    int level;
    int found;
    while(tt<=t){
        level=0;
        found=0;
        f1>>p>>ch>>q;
        if(!ping(a,q)){
            f2<<"Case #"<<tt<<": impossible\n";
            tt++;
            continue;
        }
        else{
            for(int i=0;i<40;i++){
                if(p>=q){
                    found=1;
                    break;
                }
                else{
                    p*=2;
                    level++;
                }
            }
            if(found!=0){
                f2<<"Case #"<<tt<<": "<<level<<endl;
            }
        }
        tt++;
    }
    return 0;
}
