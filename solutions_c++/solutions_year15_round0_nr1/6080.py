#include<iostream>
#include <fstream>
using namespace std;
int main(){

ofstream output;
output.open("out.txt");
ifstream input;
input.open("A-large.in");

    int u;
	input>>u;
	for(int t=0;t<u;t++){
        int n;
        input>>n;
        char a[n+1];
        input>>a;


        int b[n+1];

       for(int i=0;i<=n;i++){
        int temp=(int)a[i];
        b[i]=temp-48;
        }

        int count= 0;
        int sum=b[0];

        for(int i=1;i<=n;i++){
            if(b[i]!=0){
            if(sum<i){
                int k = i-sum;
                count+=k;
                sum=sum+k+b[i];

            }
            else{ sum+=b[i];}

            }
    }

        output<<"Case #"<<t+1<<": "<<count<<"\n";




}

}
