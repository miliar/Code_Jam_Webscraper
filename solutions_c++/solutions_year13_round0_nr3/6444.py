#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

bool palyndrome(char n[],int t);
void cast(int a,int *size,char **result);

int main(int argc,char *argv[]){
    int T;


    int A,B;
    int compte;
    ifstream file("C-small-attempt.in");
    ofstream file2("output.in");
    file >> T;


    if(file){

           for(int ca=1;ca<=T;ca++){
                file >> A ;
                file >> B ;
                compte=0;


                for(int i=A;i<=B;i++){
                    int size;
                    int p=i;
                    char *sq;
                    char *nombre;
                    cast(p,&size,&nombre);

                    if(palyndrome(nombre,size)==true){

                        int sqr=sqrt(p);

                        cast(sqr,&size,&sq);
                        if(sqr*sqr == p){
                            if(palyndrome(sq,size)==true){
                                    compte++;
                             }else
                                    break;

                        }
                    }
                }
                string cas;
                if(file2){
                    cas = "Case #";

                    file2 << cas << ca<<": "<<compte <<endl;
                }
                else
                {
                    cout << "ERROR : ouverture impossible 2";
                    return 0;
                }

            }


    }
    else
    {
        cout << "ERROR : ouverture impossible 1";
        return 0;
    }

}

bool palyndrome(char n[],int t){
    bool pal=true;
    int i=0;
    while(i<(t/2) && pal!=false){
        if(n[i] != n[t-(i+1)])
               pal=false;
        i++;
    }
    return pal;
}
void cast(int a,int *size,char **result){
    char *s=NULL;
    s=new char[101];
    char *sr=NULL;
    sr=new char[100];

    (*result)=new char[101];
    int q=-1,r=-1,i=0;
    while(q!=0){
        q=a/10;
        r=a%10;
        a=q;
        s[i]=r+48;
        i++;

    }

    int j=0;
    *size=i;
    i--;
    while(i>=0){
        sr[j]=s[i];
        i--;
        j++;

    }

       (*result)=sr;

}

