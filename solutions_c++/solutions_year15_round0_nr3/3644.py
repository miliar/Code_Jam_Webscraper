#include <iostream>

using namespace std;
void multiplicar(char A,char B,char* resultado,int*S){
if (A=='i'){
    switch (B){
    case 'i' : (*resultado)='1';(*S)=-(*S);break;
    case 'j' : (*resultado)='k';(*S)=(*S);break;
    case 'k' : (*resultado)='j';(*S)=-(*S);break;
    }
}
else {
    if (A=='j'){
        switch (B){
        case 'i' : (*resultado)='k';(*S)=-(*S);break;
        case 'j' : (*resultado)='1';(*S)=-(*S);break;
        case 'k' : (*resultado)='i';(*S)=(*S);break;
        }
    }
    else {
        switch (B){
        case 'i' : (*resultado)='j';(*S)=(*S);break;
        case 'j' : (*resultado)='i';(*S)=-(*S);break;
        case 'k' : (*resultado)='1';(*S)=-(*S);break;
        }
    }

}

}
int main()
{   int T,aux;
    char cadenas[10050];
    int long long L,X;
    int Signo=1;
    char actual='1';
    bool iOk=false,jOk=false,kOk=false;
    cin >>T;
    aux=T;
    while (T--){
        iOk=false;jOk=false;kOk=false;
        Signo=1;
        actual='1';
        cin >>L>>X>>cadenas;
        for (int long long i=0;i< L*X;i++){
           if (!iOk){
                if (actual=='1'){
                        actual=cadenas[i%L];
                }
                else {
                    multiplicar(actual,cadenas[i%L],&actual,&Signo);
                }
                if (actual=='i'){
                    iOk=true;
                    actual='1';
                }

           }//si iOk false
           else {
                if (!jOk){
                        if (actual=='1'){
                        actual=cadenas[i%L];
                    }
                    else {
                        multiplicar(actual,cadenas[i%L],&actual,&Signo);
                    }
                    if (actual=='j'){
                        jOk=true;
                        actual='1';
                    }

                } //si jOk false
                else {
                    if (actual=='1'){
                        actual=cadenas[i%L];
                    }
                    else {
                        multiplicar(actual,cadenas[i%L],&actual,&Signo);
                    }
                    if ((actual=='k') && (i== (L*X) -1)){

                        kOk=true;
                        actual='1';
                    }



                }

           }
           }//FOR
           cout <<"Case #"<<aux-T<<": "<<( ((iOk)&&(jOk)&&(kOk) && (Signo==1))?"YES":"NO" )<<endl;
        }//WHILE

    return 0;
}
