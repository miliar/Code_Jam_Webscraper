#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
using namespace std;
void ins(int inp[],int n,int val) {
    int i=n-2;
    while(inp[i]<val){
        inp[i+1]=inp[i];
        i--;
    }
    inp[i-1]=val;
}
bool cmp (int i,int j) { return (i>j); }
int main()
{
    int T,j=1;
    ofstream out;
    out.open("output.txt");
    ifstream in;
    in.open("input.txt");
    in>>T;
    while(j<=T) {
        int D;
        in>>D;
        int npck[4001],i;
        for(i=0;i<D;i++)
            in>>npck[i];
        int tm=0,cmax=10000,res;
        sort(npck,npck+D,cmp);
        if(npck[0]<4)
            cmax=npck[0];
        else {
            for(i=2;i<=npck[0];i++)
            {
                res=0;
                int k=0;
                while(k<D){
                    if(npck[k]%i==0)
                        res+=(npck[k]/i-1);
                    else
                        res+=npck[k]/i;
                    k++;
                }
                if(cmax>res+i)
                    cmax=res+i;
            }
        }
        out<<"Case #"<<j<<": "<<cmax<<endl;
        j++;
    }
    out.close();
    in.close();
    return 0;
}
