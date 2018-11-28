
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>  
using namespace std;
 
int main(int argc, char** argv){

    ofstream fout (argv[1]);
    fout<<"Case #1:"<<endl;

    int tmp[1024][10];
    int num =0;
 
        for(int i1=0; i1<2; i1++){
            for(int i2=0; i2<2; i2++){
               for(int i3=0; i3<2; i3++){
                  for(int i4=0; i4<2; i4++){
                     for(int i5=0; i5<2; i5++){
                          for(int i6=0; i6<2; i6++){
                              for(int i7=0; i7<2; i7++){
                                  for(int i8=0; i8<2; i8++){
                                       for(int i9=0; i9<2; i9++){
                                          for(int i10=0; i10<2; i10++){
                                                tmp[num][0] = i1;
                                                tmp[num][1] = i2;
                                                tmp[num][2] = i3;
                                                tmp[num][3] = i4;
                                                tmp[num][4] = i5;
                                                tmp[num][5] = i6;
                                                tmp[num][6] = i7;
                                                tmp[num][7] = i8;
                                                tmp[num][8] = i9;
                                                tmp[num][9] = i10;
                                                num ++;
                                            } 
                                        }
                                    } 
                                }
                            }
                        } 
                    } 
                }
            } 
        }

    
    for(int i=0; i<500; i++){
       fout<<"10000";
       for(int j=9;j>=0;j--) fout<<tmp[i][j];
       fout<<"1";
       fout<<"10000";
       for(int j=9;j>=0;j--) fout<<tmp[i][j];
       fout<<"1 ";
       
       for(int j=1;j<10;j++){
          long long sol = 1+tmp[i][0]*(j+1)+tmp[i][1]*pow(j+1,2)+tmp[i][2]*pow(j+1,3)+tmp[i][3]*pow(j+1,4)+tmp[i][4]*pow(j+1,5)+tmp[i][5]*pow(j+1,6)+
                      tmp[i][6]*pow(j+1,7)+tmp[i][7]*pow(j+1,8)+tmp[i][8]*pow(j+1,9)+tmp[i][9]*pow(j+1,10)+pow(j+1,15);
          fout<<sol;
          if(j!=9) fout<<" ";
       }
       fout<<endl; 
    }  
   fout.close();
}
