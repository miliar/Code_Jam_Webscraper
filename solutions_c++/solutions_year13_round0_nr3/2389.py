#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

bool isPalin(long long x){

     long long n = x;
     long long rev = 0;
     while (x > 0)
     {
          int dig = x % 10;
          rev = rev * 10 + dig;
          x = x / 10;
     }
     return n==rev;

}
int midDig(long long x){

     int sum = 0;
     while(x>0){
        sum+=(x%10)*(x%10);
        x/=10;
     }
     return sum;
}

int main(void){

    ifstream fin("fairandsquare.in");
    ofstream fout("fairandsquare-out.out");
    int T;
    fin>>T;

    for(int t=1;t<=T;t++){

        long long a,b;
        int counter = 0;
        fin>>a>>b;

        int x = 1;
        int prod = 0;

        for(;x<10000000;x++){

            long long pal = x;
            int n = x;
            while(n>0){
                pal*=10;
                pal+=n%10;
                n/=10;
            }

            if(midDig(pal)<10){

                if(pal*pal>b)break;
                if(pal*pal>=a){
                //  cout<<t<<" "<<pal*pal<<" "<<pal<<endl;
                    counter++;
                }
            }

        }
        for(x=0;x<10000000;x++){

            for(int y=0;y<10;y++){
                long long pal = x;
                pal*=10;
                pal+=y;
                int n = x;
                while(n>0){
                    pal*=10;
                    pal+=n%10;
                    n/=10;
                }
                bool isd=false;

                if(pal<10){
                    // if(pal==1||pal==4||pal==9)isd = true;

                }
                bool fc=(midDig(pal)<10);

                if(fc){

                    if(pal*pal>b){
                        x=10000000;
                        break;
                    }
                    if(pal*pal>=a){

                     //  cout<<t<<" "<<pal*pal<<" "<<pal<<endl;
                        counter++;
                    }
                }

            }

        }



         fout<<"Case #"<<t<<": "<<counter<<endl;



    }






}
