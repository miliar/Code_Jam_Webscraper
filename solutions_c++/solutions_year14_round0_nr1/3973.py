#include<fstream>
#include<iostream>
using namespace std;
std::ifstream input("A-small-attempt6.in");
std::ofstream output("output.out");
int T,rasp1,rasp2,matrice1[4],matrice2[4],bin;
//int debug[16];//----------
int main(){
    input>>T;
    for(int i=1;i<=T;i++){
            input>>rasp1;
    //        getchar();//-------
            for(int j=0;j<rasp1;j++)
                for(int k=0;k<4;k++) input>>matrice1[k];
            for(int j=rasp1;j<4;j++) 
                for(int k=0;k<4;k++) input>>bin;
     //       for(int j=0;j<4;j++)cout<<matrice1[j]<<" ";//-------
     //       cout<<"\n";//-------
            input>>rasp2;
            for(int j=0;j<rasp2;j++)
                for(int k=0;k<4;k++) input>>matrice2[k];
            for(int j=rasp2;j<4;j++) 
                for(int k=0;k<4;k++) input>>bin;
     //       for(int j=0;j<4;j++)cout<<matrice2[j]<<" ";//-------
      //      cout<<"\n";//-------
            int contor;
            contor=0;int valoare;
       //     int ledebug=0;//-----
            for(int j=0;j<4;j++)
                    for(int k=0;k<4;k++){
                            if(matrice1[j]==matrice2[k]){//---!!!!!!!!!!!!! 
                                                         contor++;
                                              //           debug[ledebug]=matrice1[j];
                            //                             debug[ledebug+1]=matrice2[k];
                         //                                ledebug+=2;
                                                           valoare=matrice1[j];
                                                         }
                            
                            }
            if(contor==0) output<<"Case #"<<i<<": Volunteer cheated!\n";
            if(contor>1) output<<"Case #"<<i<<": Bad magician!\n";
            if(contor==1) output<<"Case #"<<i<<": "<<valoare<<"\n";
      //      for(int j=0;j<16;j++)output<<debug[j]<<" ";
      //      output<<"\n";
      //      for(int j=0;j<4;j++)output<<matrice1[j]<<" ";
       //     output<<"\n";
        //    for(int j=0;j<4;j++)output<<matrice2[j]<<" ";
       //     output<<"\n";
            }
    return 0;
}
