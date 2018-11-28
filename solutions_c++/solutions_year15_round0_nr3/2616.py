#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;

int main(){
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int sistema[4][4];
    sistema[0][0] = 1;
    sistema[0][1] = 2;
    sistema[0][2] = 3;
    sistema[0][3] = 4;
    sistema[1][0] = 2;
    sistema[1][1] = -1;
    sistema[1][2] = 4;
    sistema[1][3] = -3;
    sistema[2][0] = 3;
    sistema[2][1] = -4;
    sistema[2][2] = -1;
    sistema[2][3] = 2;
    sistema[3][0] = 4;
    sistema[3][1] = 3;
    sistema[3][2] = -2;
    sistema[3][3] = -1;
    int i,j,k,x,l,xl,ij;
    string sinRep, conRep;
    int ac1,ac2,ac3,aux;
    int c,casos;
    cin >> casos;
    bool bandera;
    for(c=1;c<=casos;c++){
        aux = 1;
        ac1 = 1;
        ac2 = 1;
        ac3 = 1;
        cin >> l >> x >> sinRep;
        xl = x*l;
        conRep = sinRep;
        while(x-1>0){
            conRep+= sinRep;
            x--;
        }
        int valores[xl];
        for(i=0;i<xl;i++){
        	if(conRep.at(i)=='1'){
        		valores[i] = 1;
        	}else if(conRep.at(i)=='i'){
        		valores[i] = 2;
        	}else if(conRep.at(i)=='j'){
        		valores[i] = 3;
        	}else{
        		valores[i] = 4;
        	}
        }
        bandera = false;
        for(ij=0;ij<xl;ij++){
            aux = sistema[int(abs(ac1)-1)][valores[ij]-1];
            if(ac1<0){
                ac1 = aux * -1;
            }else{
                ac1 = aux;
            }
        }
        if(ac1==-1){
            ac1 = 1;
            for(i=0;i<xl-2;i++){
                aux = sistema[int(abs(ac1)-1)][valores[i]-1];
                if(ac1<0){
                    ac1 = aux * -1;
                }else{
                    ac1 = aux;
                }
                if(ac1==2){
                    for(j=i+1;j<xl-1;j++){
                        aux = sistema[int(abs(ac2)-1)][valores[j]-1];
                        if(ac2<0){
                            ac2 = (aux * -1);
                        }else{
                            ac2 = aux;
                        }
                        if(ac2==3){
                            for(k=j+1;k<xl;k++){
                                aux = sistema[int(abs(ac3)-1)][valores[k]-1];
                                if(ac3 < 0){
                                    ac3 = (aux * -1);
                                }else{
                                    ac3 = aux;
                                }
                                if(ac3==4 && k+1==xl){
                                    bandera = true;
                                }
                            }
                        }
                        if(bandera){
                            break;
                        }
                    }
                }
                if(bandera){
                    break;
                }
            }
        }else{
            bandera = false;
        }
        
        if(bandera){
            cout << "Case #" << c << ": YES\n";
        }else{
            cout << "Case #" << c << ": NO\n";
        }
    }
}