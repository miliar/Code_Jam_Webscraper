#include <iostream>
#include <fstream>
using namespace std;
//#define M 1000000007
ofstream fout ("A-small-attempt3.out");
ifstream fin ("A-small-attempt3.in");



int main()
{
        int z, fi,se;
        int ans=0;
        int ans_n=0;
        int  flag=0;
        fin>>z;
        int f1[5][5],f2[5][5];
        for(int i=0 ; i<z; i++){
                fin>>fi;
                for(int i=1;i<5;i++){
                        for(int j=1; j<5; j++){
                                fin>>f1[i][j];
                        }
                }
                fin>>se;
                for(int i=1;i<5;i++){
                        for(int j=1; j<5; j++){
                                fin>>f2[i][j];
                        }
                }
                for(int i=1; i<5; i++){
                        for(int j=1; j<5; j++){
                              if ( f1[fi][i] == f2[se][j] ){
                                        ans = f1[fi][i] ;
                                        ans_n++;
                              }
                        }
                }
                if(ans_n ==1 ) fout<<"Case #"<<i+1<<": "<<ans<<endl;
                if( ans_n > 1)  fout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
                if(ans_n == 0) fout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
                ans =0; ans_n = 0;
        }


    return 0;
}
