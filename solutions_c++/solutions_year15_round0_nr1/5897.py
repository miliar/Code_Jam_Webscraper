#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;


int main()
{
    ifstream input("A.in");
    string const out("A.out");
    ofstream output(out.c_str());

    int i=0,s=0,j=0,m,k;
    string T;
    getline(input,T);
    while(T[j]!='\0' && T[j]>='0' && T[j]<='9'){ s=s*10+T[j]-'0';  j++;}

    for(i=1;i<=s;i++){
            getline(input,T);
            m=0;
            j=0;
            while(T[j]!=' ' && T[j]>='0' && T[j]<='9'){ m=m*10+T[j]-'0';  j++;}
            int A[m+1];
            j++;
            for(k=0;k<=m;k++)A[k]=T[j+k]-'0';


            int sortie=0,prec;

            for(k=1;k<=m;k++){
            prec=0;
            for(j=0;j<k;j++) prec=prec+A[j];
                             prec=prec+sortie;
            if(k>prec && T[k]!=0 ) sortie=sortie+k-prec;
                                            }

            output<<"Case #"<<i<<": "<<sortie<<endl;
    }



    return 0;
}

