

#include <iostream>
#include<string>
#include<ctime>
#include<fstream>
#include<limits>





int main(int argc, const char * argv[])
{   using namespace std;
    ofstream output;
    ifstream input;
    int t,t1=1,i,j;
    unsigned long long a,b,k,count,c;
    input.open("/Users/deshmukh/Desktop/c/Udit/codejam/sample");
    output.open("/Users/deshmukh/Desktop/c/Udit/codejam/output1.txt");
    input>>t;
    unsigned int z;
    z=3&2;
    //output<<z;
    while(t1<=t){
        count=0;
        input>>a>>b>>k;
        for(i=0;i<a;i++){
            for(j=0;j<b;j++){
                c=i&j;
                if(c<k)
                    count++;
            }
        }
        
        
        output<<"Case #"<<t1<<": "<<count<<endl;
        
        t1++;
        
        
    }
   
    
    
    
    
    
   
    return 0;
}




