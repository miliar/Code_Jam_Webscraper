#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;

int jml[10];

int main()
{
    long long int N,K,L=0,tampil,x;
    jml[0]=jml[1]=jml[2]=jml[3]=jml[4]=jml[5]=jml[6]=jml[7]=jml[8]=jml[9]=0;

    int kasus;
        string baris;
        ifstream data;
        data.open ("A-large.in");
        getline(data, baris);
        (istringstream(baris) >> x);
        kasus=x;
    int j=0;
    while(!data.eof() && kasus>j-1)
    {
        if(j!=0){
        getline(data, baris);
        (istringstream(baris) >> x);
        N=x;
        for(long long int i = 1 ; i<1000000 && L<10 ;i++){
            long long int N1=N*i;
            //cout<<N1<<"-->";
            while(N1>0){
                K=N1%10;
                N1=N1/10;
                if(jml[K]==0){
                    L++;
                    jml[K]++;
                }
            }
            tampil=i*N;
        }
        ofstream data1;
        data1.open("A-small-attempt6.out", ios::app);
            if(L==10)
                data1<<"Case #"<<j<<": "<<tampil<<endl;
            else
                data1<<"Case #"<<j<<": INSOMNIA"<<endl;

        L=0;
        jml[0]=jml[1]=jml[2]=jml[3]=jml[4]=jml[5]=jml[6]=jml[7]=jml[8]=jml[9]=0;
        }
        j++;
    }


    return 0;
}
