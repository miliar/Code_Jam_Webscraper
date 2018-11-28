#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

int counter,digits[10];

bool hashIt(long long num){
     while(num!=0){
                   if(digits[num%10]==0){
                                         counter++;
                             //            cout<<"counter:"<<counter<<endl;
                                         digits[num%10] = 1;
                                         }
                   num/=10;
                   }
     if(counter==10)
                  return 1;
     return 0;
}
          
int main(){
    ofstream myfile;
    ifstream input;
    input.open("input.in");
    myfile.open("output.txt");
    
    int t,i;
    long long n,temp;
    input>>t;
    for(i=1;i<=t;i++){
               memset(digits,0,sizeof(digits));
               counter = 0;
                     
               input>>n;
               temp = n;
               if(n==0){
                        printf("Case #%d: INSOMNIA\n",i);
                        myfile<<"Case #"<<i<<": INSOMNIA\n";
                        continue;
                        }
               while(hashIt(n)==0){
                 n = n + temp;
           //      cout<<"n: "<<n<<endl;
               }                   
               printf("Case #%d: %lld\n",i,n);
               myfile<<"Case #"<<i<<": "<<n<<"\n";
    }
    input.close();
    myfile.close();
    return 0;
}              
