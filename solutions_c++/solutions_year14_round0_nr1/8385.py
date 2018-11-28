#include <iostream>
#include<fstream>

using namespace std;

int main()
{
    int t;
    int mat[2][4];
    ifstream mcin("A-small-attempt0.in");
    ofstream mcout("A-small-attempt0.out");
    mcin>>t;
    for(int i=0;i<t;++i){
        int an1;
        mcin>>an1;
        int tmp;
        for(int i1=0;i1<4*(an1-1);++i1)
            mcin>>tmp;
        for(int i2=0;i2<4;++i2){
            mcin>>mat[0][i2];
        }
        for(int i3=4*an1;i3<16;++i3)
            mcin>>tmp;
        int an2;
        mcin>>an2;
        for(int i1=0;i1<4*(an2-1);++i1)
            mcin>>tmp;
        for(int i2=0;i2<4;++i2){
            mcin>>mat[1][i2];
        }
        for(int i3=4*an2;i3<16;++i3)
            mcin>>tmp;
        int coun=0;
        int val;
        for(int j=0;j<4;++j){
            for(int k=0;k<4;++k){
                if(mat[0][j]==mat[1][k]){
                    ++coun;
                    val=mat[0][j];
                    break;
                }
            }
        }
        if(coun==1){
            mcout<<"Case #"<<i+1<<": "<<val<<endl;
        }
        else if(coun==0){
            mcout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        }
        else{
            mcout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }
    }
    mcin.close();
    mcout.close();
    return 0;
}
