#include<cstdio>
#include<fstream>
using namespace std;
int T,cur,row1[5],row2[5],ans,numAns;
int main(){
    ifstream fin;
    fin.open("inputA.in");
    ofstream fout;
    fout.open("output.txt");
    
    fin>>T;
    for(int i=1,cur=0,tmp=0,left=0,ans=0;i<=T;++i){
        numAns=0;
        printf("\nTestcase %d",i);
        fin>>cur;
        left=16-cur*4;
        cur=(cur-1)*4;
        while(cur>0){
            fin>>tmp;
            cur--;
        }
        printf("\nRow1: ");
        for(int j=0;j<4;++j){
            fin>>row1[j];
            printf("%d ",row1[j]);
        }
        while(left>0){
            fin>>tmp;
            left--;
        }
        fin>>cur;
        left=16-cur*4;
        cur=(cur-1)*4;
        while(cur>0){
            fin>>tmp;
            cur--;
        }
        printf("\nRow2: ");
        for(int j=0;j<4;++j){
            fin>>row2[j];
            printf("%d ",row2[j]);
        }
        while(left>0){
            fin>>tmp;
            left--;
        }
        for(int q=0;q<4;++q){
            for(int r=0;r<4;++r){
                if(row1[q]==row2[r]){
                    numAns++;
                    ans=row1[q];
                }
            }
        }
        printf("\nFinal: %d\n",numAns);
        if(numAns==0){
             fout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
        }
        else if(numAns==1){
             fout<<"Case #"<<i<<": "<<ans<<endl;
        }
        else{
             fout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
        }
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
