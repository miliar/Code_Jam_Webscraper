#include<iostream>
#include<cstdio>
#include<fstream>
#include<cstdlib>
#include<sstream>
#include<cstring>
using namespace std;
ifstream myfile;
ofstream myfile1;
void solve(int n){
    int *c=new int[8];
    int *a=new int[16];
    int *b=new int[16];
    int x,y,i,j,k,nz=0;
    for(i=0;i<8;i++){c[i]=0;}
    myfile>>x;
    for(i=0;i<16;i++){myfile>>a[i];}
    myfile>>y;
    for(i=0;i<16;i++){myfile>>b[i];}
    x=(x-1)*4;y=(y-1)*4;k=0;
    for(i=x;i<x+4;i++){
        for(j=y;j<y+4;j++){
            if(a[i]==b[j]){c[k]=a[i];k++;}
        }
    }
    for(i=0;i<8;i++){
        if(c[i]==0){nz++;}
    }
    if(nz==8){myfile1<<"Case #"<<n<<": Volunteer cheated!\n";}
    else if(nz==7){myfile1<<"Case #"<<n<<": "<<c[0]<<endl;}
    else{myfile1<<"Case #"<<n<<": Bad magician!\n";}

}

int main(){
    int nt,i;
    //.ifstream myfile;
    myfile.open("a.in");
    myfile1.open("b.txt");
    myfile>>nt;
    //cout<<nt;
    for(i=1;i<=nt;i++){
        solve(i);
    }
}
