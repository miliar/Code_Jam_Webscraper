#include<iostream>
#include<fstream>
#include<cstdlib>

using namespace std;

void ordenaN(double*,int);
void copia(double*,double*,int);
int war(double*,double*,int);
int d_war(double*,double*,int);

int main()
{
    int T,N,i,j,k,aux,w,dw;
    double *Naomi,*Ken;
    string c;
    ifstream entr;
    ofstream sali;

    entr.open("D-large.in",ios::in);
    sali.open("Output.in",ios::out);

    getline(entr,c,'\n');
    T=atoi(c.c_str());

    for(k=0;k<T;k++){
        getline(entr,c,'\n');
        aux=atoi(c.c_str());
        Naomi=new double[aux];
        Ken=new double[aux];
        for(i=0;i<aux;i++){
            if(i==(aux-1)){
                getline(entr,c,'\n');
                Naomi[i]=atof(c.c_str());
            }
            else{
                getline(entr,c,' ');
                Naomi[i]=atof(c.c_str());
            }
        }
        for(i=0;i<aux;i++){
            if(i==(aux-1)){
                getline(entr,c,'\n');
                Ken[i]=atof(c.c_str());
            }
            else{
                getline(entr,c,' ');
                Ken[i]=atof(c.c_str());
            }
        }
        ordenaN(Naomi,aux);
        ordenaN(Ken,aux);
        w=war(Naomi,Ken,aux);
        ordenaN(Naomi,aux);
        ordenaN(Ken,aux);
        dw=d_war(Naomi,Ken,aux);
        sali<<"Case #"<<k+1<<": "<<dw<<" "<<w<<endl;
        delete[]Naomi;
        delete[]Ken;
    }
    entr.close();
    sali.close();
}

void ordenaN(double *Naomi,int n)
{
    int i,j;
    float aux;

    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(Naomi[i]<Naomi[j]){
                aux=Naomi[i];
                Naomi[i]=Naomi[j];
                Naomi[j]=aux;
            }
        }
    }
}

int war(double *Naomi,double *Ken,int n)
{
    int i,j,pn=0;
    double *N,*K;

    N=new double[n];
    K=new double[n];

    copia(Naomi,N,n);
    copia(Ken,K,n);

    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(K[j]>N[i]&&N[i]!=0.0){
                K[j]=0.0;
                N[i]=0.0;
                break;
            }
        }
    }
    for(i=0;i<n;i++){
        if(N[i]!=0.0)
            pn++;
    }
    delete[]N;
    delete[]K;
    return(pn);
}

int d_war(double *Naomi,double *Ken,int n)
{
    int i,j,pn=0;
    double *N,*K;

    N=new double[n];
    K=new double[n];

    copia(Naomi,N,n);
    copia(Ken,K,n);

    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(N[j]>K[i]&&K[i]!=0.0){
                N[j]=0.0;
                K[i]=0.0;
                break;
            }
        }
    }
    for(i=0;i<n;i++){
        if(N[i]==0.0)
            pn++;
    }
    delete[]N;
    delete[]K;
    return(pn);
}

void copia(double *V1,double *V2,int n)
{
    int i;
    for(i=0;i<n;i++){
        V2[i]=V1[i];
    }
}
