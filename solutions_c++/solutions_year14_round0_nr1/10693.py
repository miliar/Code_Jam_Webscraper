#include <iostream.h>
#include <fstream.h>

using namespace std;

int main()
{

int T=0, ans1=0, ans2=0;
int mat1[4][4] ={0}, mat2[4][4]={0};
int val=0, count=0, i=0, j=0,n=0, val1=0, val2;

ifstream myfile;
ofstream outfile;
myfile.open("A-small-attempt2.in");
outfile.open("D:\progoutput.txt");


while(myfile){

          myfile>>T;
//          int n=T;
          for(n=0;n<T;n++){
                                         count=0;
             myfile>>ans1;                       //first answer
             
             for(i=0;i<4;i++){                           //first arrangement
                 for(j=0;j<4;j++){
                         myfile>>mat1[i][j];
                 }
            }                         
             myfile>>ans2;                               //sec answer
             
             for(i=0;i<4;i++){                                 //sec arranement
                 for(j=0;j<4;j++){
                         myfile>>mat2[i][j];
                 }
            }  
      //                  cout<<"Case #"<<n+1<<":"<<"ans1--"<<ans1<<"  ans2=="<<ans2<<endl;
            for(i=0;i<4;i++){
                                                               val1=mat1[(ans1-1)][i];
                 for(j=0;j<4;j++){

                                  if(mat2[(ans2-1)][j]==val1) { val=val1; count++; }
                                  
                 }
            }                        

            
            outfile<<"Case #"<<n+1<<": ";
            if(count==0) outfile<<"Volunteer cheated!"<<endl;
            if(count==1) outfile<<val<<endl;
            if(count>1) outfile<<"Bad magician!"<<endl;
            
            
          }        
          
          myfile.close();	
          outfile.close();
}
//          myfile.close();	

system("pause");
return 0;

}
