#include <iostream>
#include <fstream>
using namespace std;

int main(){
    ifstream fin;
    ofstream fout;
    fin.open("A-large.in");
    fout.open("A-large.out");
    int e,j,k,n,s,a;
    int b[2502];
    cin>>n;
    for(e=0; e<n; e++){
        for(j=0; j<2501; j++) b[j]=0;
        cin>>s;
        int c[s];
        for(j=0; j<2*s-1; j++){
            for(k=0; k<s; k++){
                cin>>a;
                b[a]++;
            }
        }
        k=0;
        for(j=1; j<2501; j++){
            if(b[j]%2!=0){
                    c[k]=j;
                    b[j]++;
                    k++;
                    //if(k==s-1) break;
            }
        }
        cout<<"Case #"<<e+1<<": ";
        for(j=0; j<s; j++) cout<<c[j]<<" ";
        cout<<endl;
    }
    return 0;
}
