#include <iostream>
#include <fstream>
#include<string>
using namespace std;
int main()
{
 string line;
   fstream myfile("A-large.in", ios_base::in);
   ofstream out;
out.open("out.txt");
    bool a[10]={false};
    int n,k=0,l=0,t,i=0;
    myfile>>t;
    while(i<t){
    myfile>>n;
    for(int j=0;j<10;j++){
       a[j]=false;
    }
    k=0;
    l=0;
    if(n!=0){
    while(k<10){
       l+=n;
       int x=l;
       while(x>0){
        if(!a[x%10]){
            k++;
            a[x%10]=true;
        }
        x=x/10;
       }
    }
     out<<"case #"<<i+1<<": "<<l<<endl;
    }
    else{
        out<<"case #"<<i+1<<": INSOMNIA"<<endl;
    }
    i++;
    }
    return 0;
}
