# include <math.h>
# include <iostream>
# include <cstdio>
# include <sstream>
# define MAX 100000

using namespace std;



bool is_palin(int num){

stringstream ss;
ss << num;
string str = ss.str();
int len=str.size();
for(int i=0;i<len/2;i++){
    if(str[i]!=str[len-i-1]){
        return false;
        break;
    }

}
return true;
}

int main (){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int kase,a,b,k=1;
    cin>>kase;
    while(kase--){
    cin>>a>>b;
        int cnt=0;
        for(int i=a;i<=b;i++){

                  int sq=sqrt(i);
                  if(sq*sq==i){
                    if(is_palin(i)){
                        if( is_palin(sq)){
                             cnt++;
                        }

                    }


            }
        }

      cout<<"Case #"<<k++<<": "<<cnt<<endl;


    }


return 0;
}
