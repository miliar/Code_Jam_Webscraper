#include <fstream>
#include <vector>
#include <iostream>
using namespace std;
int main(){
    int T;
    ifstream in("inputl.txt");
    ofstream out("output.txt");
    in >> T;
    for(int i=0;i<T;i++){
        int N;
        float read;
        int war;
        int cwar;
        vector<float> nao;
        vector<float> ken;
        vector<float> naoc;
        vector<float> kenc;
        in>>N;
        for(int j=0;j<N;j++){
            in>>read;            
            nao.push_back(read);
            naoc.push_back(read);
        }
        for(int j=0;j<N;j++){
            in>>read;            
            ken.push_back(read);
            kenc.push_back(read);
        }
        sort(nao.begin(),nao.end());
        sort(ken.begin(),ken.end());
        sort(naoc.begin(),naoc.end());
        sort(kenc.begin(),kenc.end());
        war=0;
        for(int j=0;j<N;j++){
            int k=0, x=0;
            for(k=0;k<N;k++){
                if(nao[k]!=0){
                    break;
                }
            }
            for(x=0;x<N;x++){
                if(ken[x]>nao[k]){
                    break;
                }
            }
            if(x==N){
                int y=0;
                for(y=0;y<N;y++){
                    if(ken[y]!=0){
                        break;
                    }
                }
                ken[y]=0;
                war++;
            }
            else{
                ken[x]=0;
            }
            nao[k]=0;
        }
//        cout<<war<<endl;
        cwar=0;
        for(int j=0;j<N;j++){
            int k=0,x=0;
            for(k=0;k<N;k++){
                if(naoc[k]!=0){
                    break;
                }
            }
            for(x=0;x<N;x++){
                if(kenc[x]!=0){
                    break;
                }
            }
            if(naoc[k]>kenc[x]){
                cwar++;
                kenc[x]=0;
            }
            else{
                int y=0;
                for(y=N-1;y>=0;y--){
                    if(kenc[y]!=0){
                        break;
                    }
                }
                kenc[y]=0;
            }
            naoc[k]=0;
        }
         out<<"Case #"<<i+1<<": "<<cwar<<" "<<war<<endl;   

    }
}
        
