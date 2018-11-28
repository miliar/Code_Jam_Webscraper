#include<fstream>
#include<iomanip>
using namespace std;
int main(){
    int t,i;
    long double c,f,x,r,fin;
    long double ans;
    ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
    out.setf(ios::fixed);
    in>>t;
    for(i=1;i<=t;i++){
        in>>c>>f>>x;
        ans=0;
        fin=0;
        r=2;
        while(!fin){
        if((x-c)/r<=(x/(r+f))){
            ans+=((long double)x/r);
            fin=1;
        }
        else{
            ans+=((long double)c/r);
            r+=f;
        }
        }
        out<<"Case #"<<i<<": "<<setprecision(7)<<ans<<"\n";
    }
    in.close();
    out.close();
}
