#include<iostream>
#include<string>
#include<fstream>
using namespace std;

int main()
{
        ifstream fin ("A-large.in.txt");
    ofstream fout("Alargefinal.out");
    int t;
    fin>>t;
    cout<<t<<endl;
    for(int i=0;i<t;i++){
        int counter=0;
        int c;
        fin>>c;
        cout<<c<<endl;
        int ary[c+1];
        string x;
            fin>>x;
            cout<<x<<endl;
        for(int k=0;k<c+1;k++){
            ary[k]=int(x[k])-48;
        }
        int tot=ary[0];
        for(int k=0;k<c;k++){
            while(k+1>tot){
                counter++;
                tot++;
            }
            tot+=ary[k+1];
        }
        fout<<"Case #"<<i+1<<": "<<counter<<endl;
    }
}
