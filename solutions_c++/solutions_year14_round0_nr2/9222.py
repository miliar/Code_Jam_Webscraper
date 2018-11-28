#include <iostream>
#include <stdio.h>
#include <iomanip>

using namespace std;
int interacao=0;
double calcula (double cookies, double x, double c, double f, double producao, double tempocorrido);

int main(int argc, char *argv[]){
    int test;
    cin>>test;

    for (int w=0; w<test;w++){

            double c;
            double x;
            double f;
            double cookies = 0;
            double tempoestimado = 0;
            double tempo = 0;
            double producao = 2;
           // int producaofutura=0;
            double tempofuturo=0;
            double verifica;
            double tempototal = 0;
            double intervalo=1;


             cin>> c;
             cin>>f;
             cin>>x;

             double tempoc;
             double tempon;
             double tempocom;
             double tempo1;
             double tempo2;

             tempoc = x / producao;
             tempon = c / producao;
             tempocom = x / (producao + f);

             tempo1 = tempo + tempoc;
             tempo2 = tempo + tempon + tempocom;

             while (tempo2 < tempo1){
                tempo = tempo + tempon;
                producao = producao + f;
                tempoc = x / producao;
                tempon = c / producao;
                tempocom = x / (producao+f);

                tempo1 = tempo + tempoc;
                tempo2 = tempo + tempon + tempocom;

             }

             cout<<"Case #"<<w+1<<": ";
             //cout<<tempo1<<endl;

cout << setiosflags (ios::fixed) << setprecision (7) << tempo1 << endl;


             /*

4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

3
30.0 1.0 2.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762

             */
          //  double tempocorrido = 0;
  /*  for (double s=0; cookies<x; s=s+intervalo){
                  if (cookies>=x){
                    break;
                }

                if(((cookies-x)<0.01)&& ((cookies-x)>0)){
                        goto fim;
                }
                if(((x-cookies)<0.01)&& ((x-cookies)>0)){
                        goto fim;
                }

                tempoestimado = (x-cookies)/(producao*intervalo);
                tempofuturo = (x-cookies+c)/((intervalo*producao)+f);





              if(cookies>=c){
                    if (tempofuturo<tempoestimado){
                        cookies=cookies-c;
                        tempocorrido=tempocorrido+ (c/producao);
                        producao=producao+f;
                       // return calcula(cookies, x, c, f, producao, tempocorrido);
                    }
                    else{
                        tempocorrido=tempocorrido+((x-cookies)/producao);
                        cookies=x;

                      //  return calcula(cookies, x, c, f, producao, tempocorrido);
                    }
                }
                else{
                    if(x>c){
                            cookies=cookies+c;                         //30 2 100 ---- 70
                            tempocorrido=tempocorrido+(c/producao);
                    }
                    else {
                            cookies=x;
                            tempocorrido=tempocorrido+(x/producao);
                    }

                   // return calcula(cookies, x, c, f, producao, tempocorrido);
                }
               // return calcula(cookies, x, c, f, producao, tempocorrido);

            }

*/








         /*    for (double s=0; cookies<x; s=s+intervalo){

                if (cookies>=x){
                    break;
                }

                if(((cookies-x)<0.0000001)&& ((cookies-x)>0)){
                        goto fim;
                }
                if(((x-cookies)<0.0000001)&& ((x-cookies)>0)){
                        goto fim;
                }

                cookies=cookies+(producao*intervalo);
                tempo=s+1;

                while ((x-cookies)<(producao*intervalo)){
                    intervalo = intervalo / 10;
//                    cout<<"cu: "<<cookies<<" ---- intervalo: " <<intervalo<<" --- prod: "<<producao*intervalo<<endl;
                }



//                cout<<"tempo = "<<tempo<<" ***** cookie = "<<cookies<<endl;
  //              cout<<"x= "<<x<<" ***** cookie = "<<cookies<<endl;

                if (cookies==x){
                    goto fim;
                }

                int aux;

                tempoestimado = (x-cookies)/(producao*intervalo);
                tempofuturo = (x-cookies+c)/((intervalo*producao)+f);
                if(cookies>=c){
                    if (tempofuturo<tempoestimado){
                        cookies=cookies-c;
                        producao=producao+f;
                    }
                }

             }*/






                //cout << setiosflags (ios::fixed) << setprecision (7) << x << endl;
       /*     fim:
             cout<<"Case #"<<w+1<<": ";
             cout<<tempocorrido<<endl;*/
           // cout<<calcula(cookies, x, c, f, producao, tempo)<<endl;
    }
}









/*
double calcula (double cookies, double x, double c, double f, double producao, double tempocorrido){
                double tempoestimado;
                double tempofuturo;
                //double tempocorrido;
                interacao++;

                cout<<"testeeeeeeee "<<interacao<<endl;

                if (cookies == x){
                    return tempocorrido;
                }

                if(((cookies-x)<0.001)&& ((cookies-x)>0)){
                       return tempocorrido;
                }
                if(((x-cookies)<0.001)&& ((x-cookies)>0)){
                        return tempocorrido;
                }

                tempoestimado = (x-cookies)/(producao);
                tempofuturo = (x-cookies+c)/((producao)+f);

                if(cookies>=c){
                    if (tempofuturo<tempoestimado){
                        cookies=cookies-c;
                        tempocorrido=tempocorrido+ (c/producao);
                        producao=producao+f;
                       // return calcula(cookies, x, c, f, producao, tempocorrido);
                    }
                    else{
                        cookies=x-cookies;
                        tempocorrido=tempocorrido+((x-cookies)/producao);
                      //  return calcula(cookies, x, c, f, producao, tempocorrido);
                    }
                }
                else{
                    cookies=cookies+c;
                    tempocorrido=c/producao;
                   // return calcula(cookies, x, c, f, producao, tempocorrido);
                }
                return calcula(cookies, x, c, f, producao, tempocorrido);

}*/

// inicia com 0 cookies, producao de 2 cookies por segundo
// com C cookies se compra uma farm --> extra F cookies por segundo
//quando tiver X cookies, nao gastos com farms, ganha o jogo
//calcular o tempo que demora
/*
c=500.0, f=4.0, x=2000.0
after 250 seconds, can buy a farm by 500 cookies, and it willproduce F=4cookies per second
c=0, producing 6scookies /s
em mais 83,333s, compra outra farm com 500 cookies
c=0, producao 10cu/s


4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0

Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762



*/












