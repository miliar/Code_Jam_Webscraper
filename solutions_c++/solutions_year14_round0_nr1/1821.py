#include<fstream>
#include<vector>
using namespace std;
int main(){
    int t,i,j,k,l,a,b,n,c;
    vector<int> v;
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    in>>t;
    for(i=1;i<=t;i++){
        in>>a;
        for(j=1;j<5;j++)
            for(k=1;k<5;k++){
                in>>b;
                if(j==a)
                    v.push_back(b);
            }
        in>>a;
        n=0;
        for(j=1;j<5;j++)
            for(k=1;k<5;k++){
                in>>b;
                if(j==a){
                    for(l=0;l<4;l++)
                    if(b==v[l]){
                        n++;
                        c=b;
                        break;
                    }
                }
            }
        out<<"Case #"<<i;
        if(n==0)
            out<<": Volunteer cheated!\n";
        else if(n==1)
            out<<": "<<c<<"\n";
        else
            out<<": Bad magician!\n";
        v.clear();
    }
    in.close();
    out.close();
}
