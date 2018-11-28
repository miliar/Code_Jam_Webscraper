#include <iostream>
#include <fstream>

using namespace std;

bool check(int Arr[]){
    for(int i=0;i<10;++i)
        if(Arr[i]==0)
            return false;
    return true;
}

int main()
{
     ifstream in("readTest.txt");
     ofstream out("writeOut.txt");
     int tcase;
     in>>tcase;
     int k=1;
     while(k<=tcase){
        int n=1;
        int Arr[10]={0};
        in>>n;
        int m;
        int r;
        for(int i=1;;i++){
            m=n*i;
            if(m==0){
                out<<"Case #"<<k<<": INSOMNIA"<<endl;
                break;
            }
            int temp=m;
            while(temp){
                r=temp%10;
                Arr[r]++;
                temp=temp/10;
            }
            if(check(Arr)){
                out<<"Case #"<<k<<": "<<m<<endl;
                break;
            }
        }
        k++;
     }

    in.close();
    out.close();

    return 0;
}
