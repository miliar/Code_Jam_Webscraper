#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int input[1000000];
    ofstream op_file;
    op_file.open("output_file");
    int dig10[10];
    int input_count=0, rem;
    //read the input file
    ifstream file_h;
    file_h.open("A-large.in");
    file_h>>input[0];
    for(int i=0; i<input[0]; i++)
    {
     file_h>>input[i+1];
    }
    file_h.close();
    //for(int i=0; i<;i++){
    //cout << input[i]<< endl;
    //}
    for(int i=1; i<input[0]+1; i++){
     if(input[i]==0) {op_file<<"Case #"<<i<<": INSOMNIA\n";
     continue;}
     for(int j=0; j<10; j++) dig10[j]=0;
     int fact=1, cond=0;
     while(cond!=1){
     int orig_um=input[i]*fact, orig;
     orig=orig_um;
     fact++;
     while(orig!=0){
      rem=orig%10;
      orig=orig/10;
      dig10[rem]=1;
     }
     int sm=0;
     for(int k=0; k<10; k++){
     sm=sm+dig10[k];
     }
     if(sm==10) {cond=1; op_file<<"Case #"<<i<<": "<<orig_um<<endl; }

          }

    }
    op_file.close();
    return 0;
}
