#include<iostream>
#include<fstream>
using namespace std;
int main(){

ofstream output;
output.open("out.txt");
ifstream input;
input.open("A-large.in");
    int t;
	input>>t;
	for(int k=1;k<=t;k++){
        int n;
        input>>n;
        int a[n];
        input>>a[0];

        int max =0;
        long long int sum1=0; // case 1 sum;
        for(int i=1;i<n;i++){
            input>>a[i];
            if ((a[i-1]-a[i])>max){
                max=a[i-1]-a[i];
            }
            if((a[i-1]-a[i])>0){
                sum1+=(a[i-1]-a[i]);
            }

        }
       long long int sum2=0;
        for(int i=0;i<n-1;i++){

            if((max-a[i])>=0){
                sum2+=a[i];
            }
            else if (max-a[i]<0){
                sum2+=max;
            }


        }

        output<<"Case #"<<k<<": "<<sum1<<" "<<sum2 <<"\n";


	}

}
