#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    ifstream fin;
    fin.open("A-large.in");
    ofstream fout;
    fout.open("2.txt");
    fin>>t;
    int orr=1;
    while(t--){
        long long int n;
        fin>>n;
        fout<<"Case #"<<orr<<": ";
        orr++;
        if(n==0){
            fout<<"INSOMNIA\n";
            continue;
        }
        int a[10];
        int z=10;
        for(int i=0;i<10;i++)
            a[i]=0;
        long long int temp=0;
        do{
            temp+=n;
            //cout<<temp;
            long long int q=temp;
            while(q>0){
                if(a[q%10]==0){
                    z--;
                    a[q%10]=1;
                }
                q/=10;
            }
        }while(z);
        fout<<temp<<"\n";
    }
    return 0;
}
