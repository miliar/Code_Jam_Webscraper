/*Find the greatest product of five consecutive digits in the 1000-digit number.*/

#include<iostream>
#include<math.h>
#include<fstream>
#include<string>
using namespace std;



int main(int argc, char** argv){
  
char file1[100]; sprintf(file1, "output.txt");     ofstream parOP(file1);

int line=0;
int case_total_number=0;
int case_number=0;
int i=0;
int j=0;

int * three_space=new int[3];
int * first_arrange=new int[16];
int * second_arrange=new int[16];
int first_row=0;
int second_row=0;
int same=0;
int same_number=0;
ifstream myReadFile;
 myReadFile.open("A-small-attempt0.in");
string output;
 
 if (myReadFile.is_open()) {
   while (!myReadFile.eof()) { 
    getline(myReadFile,output);
     line=line+1;
   //parOP<<output.size()<<endl;

     if(line==1){case_total_number=(int)(output[0]-'0');}
    
     if(line==2){first_row=0;first_row=(int)(output[0]-'0');}
     if(line>2&&line<7){i=0;
       for(j=0;j<output.size();j++){
       if((int)(output[j]-'0')<0){three_space[i]=j;i=i+1;}
        }
        
     if(three_space[0]==1){first_arrange[(line-3)*4]=(int)(output[0]-'0');}
     if(three_space[0]==2){first_arrange[(line-3)*4]=10*(int)(output[0]-'0')+(int)(output[1]-'0');}
     
     if(three_space[1]-three_space[0]==2){first_arrange[(line-3)*4+1]=(int)(output[three_space[0]+1]-'0');}
     if(three_space[1]-three_space[0]==3){first_arrange[(line-3)*4+1]=10*(int)(output[three_space[0]+1]-'0')+(int)(output[three_space[0]+2]-'0');}
     
     if(three_space[2]-three_space[1]==2){first_arrange[(line-3)*4+2]=(int)(output[three_space[1]+1]-'0');}
     if(three_space[2]-three_space[1]==3){first_arrange[(line-3)*4+2]=10*(int)(output[three_space[1]+1]-'0')+(int)(output[three_space[1]+2]-'0');}
     
     if(output.size()-three_space[2]==2){first_arrange[(line-3)*4+3]=(int)(output[three_space[2]+1]-'0');}
     if(output.size()-three_space[2]==3){first_arrange[(line-3)*4+3]=10*(int)(output[three_space[2]+1]-'0')+(int)(output[three_space[2]+2]-'0');}
      //parOP<<first_arrange[(line-3)*4+1]<<" test"<<endl;
    }
    
     if(line==7){second_row=0;second_row=(int)(output[0]-'0');}
     if(line>7&&line<12){
       i=0;
       for(j=0;j<output.size();j++){
       if((int)(output[j]-'0')<0){three_space[i]=j;i=i+1;}
        }
        
     if(three_space[0]==1){second_arrange[(line-8)*4]=(int)(output[0]-'0');}
     if(three_space[0]==2){second_arrange[(line-8)*4]=10*(int)(output[0]-'0')+(int)(output[1]-'0');}
     
     if(three_space[1]-three_space[0]==2){second_arrange[(line-8)*4+1]=(int)(output[three_space[0]+1]-'0');}
     if(three_space[1]-three_space[0]==3){second_arrange[(line-8)*4+1]=10*(int)(output[three_space[0]+1]-'0')+(int)(output[three_space[0]+2]-'0');}
     
     if(three_space[2]-three_space[1]==2){second_arrange[(line-8)*4+2]=(int)(output[three_space[1]+1]-'0');}
     if(three_space[2]-three_space[1]==3){second_arrange[(line-8)*4+2]=10*(int)(output[three_space[1]+1]-'0')+(int)(output[three_space[1]+2]-'0');}
     
     if(output.size()-three_space[2]==2){second_arrange[(line-8)*4+3]=(int)(output[three_space[2]+1]-'0');}
     if(output.size()-three_space[2]==3){second_arrange[(line-8)*4+3]=10*(int)(output[three_space[2]+1]-'0')+(int)(output[three_space[2]+2]-'0');}
        //  parOP<<second_arrange[(line-8)*4+1]<<" test"<<endl;

     }
    
    // Start to find the card    
if(line==11){
  case_number+=1;
  same=0;same_number=0;
for(i=0;i<4;i++){
  for(j=0;j<4;j++){
    //parOP<<"second_arrange[(second_row-1)*4+j]"<<second_arrange[(second_row-1)*4+j]<<endl;
    if(first_arrange[(first_row-1)*4+i]-second_arrange[(second_row-1)*4+j]==0)
    {same=same+1;
      same_number=second_arrange[(second_row-1)*4+j];}
  }
}    
   if(same==0){
     parOP<<"Case #"<<case_number<<": "<<"Volunteer cheated!"<<endl;   //outputtheresult 
    }
    if(same>1){
     parOP<<"Case #"<<case_number<<": "<<"Bad magician!"<<endl;   //outputtheresult 
    } 
    
    if(same==1){
     parOP<<"Case #"<<case_number<<": "<<same_number<<endl;   //outputtheresult 
    } 
 
 line=1;}
   }
  myReadFile.close();
}

parOP.close();
  return 0;
}



