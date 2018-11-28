#include  <vector>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <fstream>

using namespace std;
vector <double> ken, naomi,ken2;

bool cmp (double a, double b){
if (a   >   b) return true;

}

int main(){

    ofstream myfile;
    myfile.open("output.txt");
    ios::sync_with_stdio(0);
        int t,n;
        double a,b;
        int point,dpoint;
        int teste;
        int top;
        cin>>t;

        	for (int i = 1; i <= t; ++i){
                point=0;
                dpoint=0;
                teste=0;
        		cin>>n;
        		ken.clear();
        		naomi.clear();
        		ken2.clear();
        		for(int j=0;j<n;j++){
                    cin>>a;
                    naomi.push_back(a);
        		}

                for(int j=0;j<n;j++){
                    cin>>b;
                    ken.push_back(b);
                    ken2.push_back(b);
                }

                sort(naomi.begin(),naomi.end(),cmp);
                sort(ken.begin(),ken.end());

                for(int j=0; j<n;j++){
                    for(int k=0;k<n;k++)
                        if(naomi[j]<ken[k]) {
                                teste=1;
                                ken[k]=-1;
                                k=n;
                    }
                    if(teste==0) point++;
                    teste=0;
                }
                teste=0;
                top=n-1;

                sort(naomi.begin(),naomi.end());
                sort(ken2.begin(),ken2.end());
                for(int j=0; j<n;j++){
                    for(int k=0; k<n;k++)
                        if(naomi[j]>ken2[k] && ken2[k]!=0) {
                            teste++;
                            ken2[k]=0;
                            dpoint++;
                            k=n;
                }

                    if(teste==0) {
                            ken2[top]=0;
                            top--;
                }
                    teste=0;
                }

                myfile<<"Case #"<<i<<": "<<dpoint<<' '<<point<<'\n';
        	}
     myfile.close();
    return 0;
}

