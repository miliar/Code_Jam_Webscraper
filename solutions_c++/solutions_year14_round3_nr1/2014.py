

#include <iostream>
#include<string>
#include<ctime>
#include<fstream>
#include<limits>

#include<cmath>



int main(int argc, const char * argv[])
{   using namespace std;
    ofstream output;
    ifstream input;
   
    string str;
    int t,t1=1;
    input.open("/Users/Deshmukh/Desktop/Udit/codejam/sample");
    output.open("/Users/Deshmukh/Desktop/Udit/codejam/output1.txt");
    input>>t;
    while(t1<=t){
        input>>str;
        int index,flag=0,p=0,q=0,i,i1;
        index=0;
        while(str[index]!='/'){
            index++;
        }
        index--;
        i1=index;
        for(i=0;i<=index;i++){
            p+=(str[i]-48)*pow(10,i1);
            i1--;
        }
        //index=index+2;
        cout<<index<<" "<<str.length()<<endl;
        i1=str.length()-3-index;
        index+=2;
        for(i=index;i<str.length();i++){
            q+=(str[i]-48)*pow(10,i1);
            i1--;
        }
        cout<<p<<endl;
        cout<<q<<endl;
       
        int count=0;
        while(p/q <1){
            if(q%2!=0){
               
                
                flag=1;
                break;
            }
            q/=2;
            
            
            count++;
        }
        while(q!=1){
            if(q%2!=0){
                flag=1;
                
                break;
            }
            q/=2;
        }
        if(flag==0)
        output<<"Case #"<<t1<<": "<<count<<endl;
        if(flag==1)
            output<<"Case #"<<t1<<": impossible"<<endl;
        t1++;
    }
    
    
    return 0;
}