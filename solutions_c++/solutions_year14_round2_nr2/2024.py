#include<cstdio>
#include<fstream>
using namespace std;
int T,numbers[1025];
int main(){
    
    ifstream fin;
    ofstream fout;
    fin.open("inputB.in");
    fout.open("outputB.txt");
    
    fin>>T;
    for(int i=1;i<=T;++i){
        
        int A,B,K,sum=0;
        fin>>A>>B>>K;
        
        for(int r=0;r<1024;++r) numbers[r]=0;
        
        for(int a=0;a<A;++a){
            for(int b=0;b<B;++b){
                numbers[a&b]++;
            }
        }
        
        for(int k=0;k<K;++k){
            for(int j=0;j<1024;++j){
                if(numbers[j]>0){
                    if((j^k)==0) sum+=numbers[j];
                }
            }
        }
        
        fout<<"Case #"<<i<<": "<<sum<<endl;
        
    }
    
    //scanf("%d",&T);
    return 0;
}
