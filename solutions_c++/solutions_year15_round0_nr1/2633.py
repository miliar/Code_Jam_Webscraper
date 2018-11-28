#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int main(){
#ifndef ONLINE_JUDGE
	freopen("aL.in", "rt", stdin);
	freopen("aL.out", "wt", stdout);
#endif

int nfois;
cin>>nfois;

for(int i=0;i<nfois;i++){

int Sm;

cin>>Sm;
 cin.ignore();
string tab;

 getline(cin,tab);

cout<<"Case #"<<i+1<<": ";
int soe=0,ret=0;
for(int k=0;k<Sm;k++){
char c=tab[k];
//cout<<c<<"\n";
soe+=(int)c -48;
if(soe<k+1){
/*if(c=='0') ret++;
else{*/
ret++;
soe++;
//}
}


}

cout<<ret<<"\n";

}





return 0;
}
