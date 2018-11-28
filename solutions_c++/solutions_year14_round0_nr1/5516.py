#include<iostream>
#include<fstream>
#include<cstdlib>

using namespace std;

void imprime(int[4][4]);
void llena(int[4][4],int[4],int);
int trick(int[4],int[4],int*);

int main(void)
{
    bool flag=false;
    int m[4][4]={0};
    int v1[4],v2[4];
    int cont=0,cont2=0,ans,T,cas,num,i,j,k;
    string c;
    ifstream entr;
    ofstream sali;

    entr.open("A-small-attempt1.in",ios::in);
    sali.open("Output.in",ios::out);

    getline(entr,c,'\n');
    T=atoi(c.c_str());
    for(k=0;k<T;k++){
        getline(entr,c,'\n');
        ans=atoi(c.c_str());
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(cont==3){
                    getline(entr,c,'\n');
                    m[i][j]=atoi(c.c_str());
                }
                else{
                    getline(entr,c,' ');
                    m[i][j]=atoi(c.c_str());
                    cont++;
                }
            }
            cont=0;
        }
        cont2++;
        if(cont2==1){
            llena(m,v1,ans-1);
            k--;
        }
        else if(cont2==2){
            llena(m,v2,ans-1);
            cas=trick(v1,v2,&num);
            switch(cas){
                case 1: sali<<"Case #"<<k+1<<": "<<num<<endl;
                break;
                case 2: sali<<"Case #"<<k+1<<": Bad magician!"<<endl;
                break;
                case 3: sali<<"Case #"<<k+1<<": Volunteer cheated!"<<endl;
                break;
            }
            cont2=0;
        }
    }
    entr.close();
    sali.close();
    return(0);
}

void llena(int m[4][4],int v[4],int ans)
{
    int i;

    for(i=0;i<4;i++){
        v[i]=m[ans][i];
    }
}

int trick(int v1[4],int v2[4],int *num){
    int i,j,cont=0;

    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            if(v1[i]==v2[j]){
                cont++;
                *num=v1[i];
            }
        }
    }
    if(cont==1)
        return(1);
    if(cont>1)
        return(2);
    if(cont==0)
        return(3);
}
