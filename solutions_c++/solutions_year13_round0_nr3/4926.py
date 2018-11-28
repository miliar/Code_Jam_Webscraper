#include<iostream>
#include<fstream>

using namespace std;


int main(){
    std::ifstream infile("C:/Users/aman/Desktop/input1.txt");
    std::ofstream output("C:/Users/aman/Desktop/output1.txt");
    //input.open("C:\Users\aman\Desktop\input.txt");
    //output.open("C:\Users\aman\Desktop\output.txt");
    int T;
    infile>>T;
    
    int i;
    int A,B;
    for(i=1;i<=T;i++){

                      infile>>A>>B;
                      int ans = 0;
                      int j;
                      for(j=A;j<=B;j++){
                                 if(j==1 || j==4|| j==9 ||j==121 || j==484)
                                 {
                                         ans+=1;
                                 }
                                 
                                 
                      }       
                      
                      output<<"Case #"<<i<<": "<<ans<<endl;
    }
    
    
    
    return 0;
}
