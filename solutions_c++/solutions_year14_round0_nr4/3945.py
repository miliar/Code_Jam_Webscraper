#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;
int main() {
	ifstream myfile("D-large.in");
	ofstream outfile;
	outfile.open ("result.txt");
	string data;
	int T, n, count=1;
	getline(myfile, data);
	stringstream(data)>>T;
	do {
		myfile>>n;
		double A[n], B[n];
		for(int i=0; i<n; i++) {
			myfile>>A[i];
		}
		for(int i=0; i<n; i++) {
			myfile>>B[i];
		}
        sort(A, A + sizeof A / sizeof A[0], greater<double>());
        sort(B, B + sizeof B / sizeof B[0], greater<double>());
        double copyB1[n];
        for(int i=0; i<n; i++) {
                copyB1[i]=B[i];        
        }
        //Optimal war logic
        int optiWar = 0;
        for(int i=0; i<n; i++) {
                int flag=0;
                for(int j=n-1; j>=0; j--) {
                        if(copyB1[j] != 0) {
                              if(A[i]<copyB1[j]) {
                                      copyB1[j]=0;
                                      flag=1;
                                      break;              
                              }  
                        }
                        
                }
                if(flag==0) {
                            optiWar++;
                            //find the smallest number in B
                            for(int j=n-1; j>=0; j--) {
                                    if(copyB1[j] !=0) {
                                            copyB1[j]=0;
                                            break;
                                    }
                            }
                                        
                }
        }
        
        int decWar=0;
        for(int i=n-1;i>=0;i--) {
                for(int j=n-1; j>=0; j--) {
                           if(B[i]<A[j]) {
                                         decWar++;
                                         A[j]=0;
                                         break;              
                           }          
                }        
        }
        
        outfile<<"Case #"<<count<<": "<<decWar<<" "<<optiWar<<"\n";
        count++;
		T--;
	} while(T!=0);
	outfile.close();
	return 0;
}
