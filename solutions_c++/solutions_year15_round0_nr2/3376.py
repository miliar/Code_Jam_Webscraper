#include<iostream>
#include<fstream>
#include<set>
#include<algorithm>
#include<vector>
#include<cstring>
using namespace std;
int inp[2001];
int fun(int num,int w8){

    if(num<=w8) return 0;
    int ret=num/w8;
    if(num%w8==0)
        ret--;
    return ret;

}
int main(){
    ifstream  fin("/Users/anupsing/Desktop/GCJ/input.txt");
    ofstream  fout("/Users/anupsing/Desktop/GCJ/output.txt");



    int T;
    fin>>T;
    int cases=1;
    while(T--) {
            int D;
            fin>>D;
            for(int i=0;i<D;i++)
                fin>>inp[i];

            int ans=10000;
            for(int i=1;i<=1000;i++)
            {
              int temp=i;
              for(int j=0;j<D;j++)
                temp+=fun(inp[j],i);
                if(ans>temp){
                    ans=temp;
                    //cout<<temp<<" "<<i<<endl;
                }
            }

            fout<<"Case #"<<cases++<<": "<<ans<<endl;




    }
    return 0;
}
