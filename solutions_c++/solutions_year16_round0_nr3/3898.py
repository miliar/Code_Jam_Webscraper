//Testa primalidade, fatora e mostra divisores de números entre 10^7 e 10^14
#include <iostream>
#include <math.h>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
using namespace std;

int C[100000001], P[10000001], rq, nf, np, nd;
long long int n, q, F[50], D[10000];
bool teste;

void GeraCrivo (int n)
{    int i, rq, t, d;
     for (i=1; i<=n; i++)   C[i] = i;
     for (i=2; i<=n; i+=2)  C[i] = 2;
     rq = sqrt(n);
     for (i=3; i<=rq; i+=2)
     {   if (C[i] == i)
         {   t = i*i;  d = i+i;
             while(t<=n)
             {   if (C[t] == t) C[t] = i;
                 t = t+d;
             }
         }
     }
}
void GeraPrimos (int rq)
{    np=0;
     for (int i=2; i<=rq; i++)
         if (C[i]==i)  P[++np]= i;
}

bool TestaPrimo (long long int q)
{    bool primo = true;
     for (int i=1; i<=np; i++)
     {   if ((q % P[i]) == 0)
         {   if (q != P[i]) primo = false;
             break;
         }
     }
     return (primo);
}

void Fatora (long long int q)
{    nf = 0;
     for (int i=1; i<=np; i++)
     {   while((q % P[i]) == 0)
         {   F[++nf] = P[i];  q = q/P[i];
         }
         if (q == 1) break;
     }
     if (q != 1) F[++nf] = q;
}

void Divisores(long long int q)
{    int nda;long long int k;
     F[0] = 1;  nd = 1;  D[1] = 1;  nda = 1;
     for (int i=1; i<=nf; i++)
     {   if (F[i] == F[i-1]) k = k*F[i];
         else
         {    nda = nd;  k = F[i];
         }
         for (int j=1; j<=nda; j++)
             D[++nd] = k*D[j];
     }
}

long long potencia(int n, int p){
    long long res = 1;
    for(int i = 0 ; i < p ; i++){
        res*=n;
    }
    return res;
}

long long to_base_n(char s[], int tam, int n){
    long long nova_base = 0;
    for(int i = tam-1, j = 0 ; i >= 0 ; i--){
        nova_base += ((s[i]-'0')*potencia(n, j++));
    }
    return nova_base;
}



int main()
{   rq = 100000100;  n = rq;  n = n*n;
    GeraCrivo(rq);
    GeraPrimos(rq);
    //cout << "np = " << np << endl << endl;
    char q1[50];
    int t_entrada, n_entrada, j_entrada, dr_tam, cases=1;
    vector<string> respostas;
    vector<vector< long long> > divisores_respostas;
    scanf("%d", &t_entrada);
    while(t_entrada--)
    {
        scanf("%d %d", &n_entrada, &j_entrada);
        divisores_respostas.resize(j_entrada);
        dr_tam = 0;
        for(int i = 0 ; i < n_entrada ; i++)
            q1[i] = '0';
        q1[n_entrada] = '\0';
        q1[0] = '1'; q1[n_entrada-1] = '1';
        for(int i = 0 ; i < (1 << (n_entrada-2)) ; i++){ /// testando todas as possibilidades para a string
            for(int j = 0 ; j < n_entrada-2 ; j++){
                q1[j+1] = i&(1 << j) ? '1' : '0';
            }
            //printf("q1: %s\n\n", q1);
            int bases = 2;
            //printf("oi\n");
            teste = false;
            while(bases <= 10){
                q = to_base_n(q1, n_entrada, bases);
                //printf("q = %lld, base: %d\n", q, bases);
                bases++;
                teste |= TestaPrimo(q);
                if(!teste){
                    Fatora(q);
                    Divisores(q);
                    for (int i_nd=1; i_nd<=nd; i_nd++){
                        if(D[i_nd] != 1 && D[i_nd] != q){
                            divisores_respostas[dr_tam].push_back(D[i_nd]);
                            break;
                        }
                    }
                }
                //if (teste)  cout << q << " eh primo"     <<endl <<endl;
                //else        cout << q << " nao eh primo" <<endl <<endl;
                //Fatora(q);
                //cout << "nf = " << nf <<endl << "Fatores: ";
                //for (int i=1; i<=nf; i++) cout << F[i] << " ";  cout << endl << endl;
                //Divisores(q);
                //cout << "nd = " << nd <<endl << "Divisores: ";
                //for (int i=1; i<=nd; i++) cout << D[i] << " ";  cout << endl <<endl <<endl;
            }
            if(!teste){
                //printf("%s\n", q1);
                respostas.push_back(string(q1));
                dr_tam++;
                if(respostas.size() == j_entrada)
                    break;
            }
            else{
                divisores_respostas[dr_tam].clear();
            }
        }
        printf("Case #%d:\n", cases++);
        for(int i = 0 ; i < respostas.size() ; i++){
            printf("%s", respostas[i].c_str());
            for(int j = 0 ; j < divisores_respostas[i].size() ; j++)
                printf(" %d", divisores_respostas[i][j]);
            printf("\n");
        }
    }
    return 0;
}
