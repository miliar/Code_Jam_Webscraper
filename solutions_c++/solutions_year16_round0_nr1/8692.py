#include <iostream>
#include <fstream>
using namespace std;

int main () {
    ifstream fi;
    ofstream fo;
    //fi.open ("tinput.txt");
    //fo.open ("toutput.txt");

    //fi.open ("B-small-attempt1.in");B-large
    fi.open ("A-large.in");
    fo.open ("q1__large_output.txt");

    int t,i=0,count=0, j,n,top;

    //char cn, co, s[101];
    fi>>t;                                  //cout<<t<<"\n";
    //fi.getline(s,101);
    while(++i<= t){
        j=0;  top=0;
        int k,c=0;
        long sum = 0;
        int a[50] = {};
        fi>>n;                              //cout<<n<<" ";
        k=n;
        if(n==0) {
            fo<<"Case #"<<i<<": INSOMNIA"<<endl;

        }
        else{
                while(n != 0){
                   a[j]=n%10;
                  // k[a[j]] = 1;
                   sum = sum | (1<<a[j]);
                   j++;
                   top++;
                   n=n/10;
                }


                while(sum != 1023){
                    c=0;
                    a[0]= a[0]+k;                              //cout<<sum<<" ";
                    for(j=0; j<top; j++){
                        a[j]= a[j] +  c;
                        c = a[j]/10;
                        a[j] = a[j]%10;
                        sum = sum | (1<<a[j]);

                    }
                    if(c!=0){
                        a[top]=c;
                        sum = sum | (1<<a[top]);
                        top++;
                        if(top > 90) {
                            fo<<"Case #"<<i<<": INSOMNIA"<<endl;

                        }
                    }

                       //  for(j=top-1; j>=0; j--){  cout<<a[j];}cout<<endl;
                      // cin>>n;
                }                                         // cout<<" "<<sum<<" : ";
               fo<<"Case #"<<i<<": ";
               for(j=top-1; j>=0; j--){
                   fo<<a[j];                                //cout<<a[j];
               }
               fo<<endl;                                   // cout<<endl;

             }//end of one test case
         }
    fi.close();
    fo.close();
    return 0;
}
