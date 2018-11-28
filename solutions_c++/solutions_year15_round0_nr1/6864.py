#include<fstream>
using namespace std;

ifstream cin ("a.in");
ofstream cout ("a.out");

//-48
int n,si,st,ego,smax,nom;
char num;


int main(){
cin>>n;
for(int i=1;i<=n;i++){
ego=0;st=0;
cin>>smax;
    for(int j=0;j<=smax;j++){
        cin>>num;
        nom=num-48;
        if(st>=j){
        //imaste ok tsie pernoume ara en kamno kati tsie kamno collect apla
        st+=nom;
        }
        else{
        ego=ego+(j-st);
        st=j+nom;
        }
    }
    cout<<"Case #"<<i<<": "<<ego<<endl;
}

}
