#include <iostream>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;


int main()
{
    ofstream archout("A-small-attempt4.out");
    ifstream archin("A-small-attempt4.in");

    int n,a1[4][4],a2[4][4],i=1,f,f2,j=0,x,l=0,num;
    char c[100],*p;
    archin.getline(c,100);
    n=atoi(c);
    while(n!=0){
        archin.getline(c,100);
        f=atoi(c)-1;
        x=4;
        j=0;
        l=0;
        while(x!=0){
            archin.getline(c,100);
            p=strtok(c," ");
            j=0;
            while(p!=NULL){
                a1[l][j]=atoi(p);
                p=strtok(NULL," ");
                j++;
            }
            l++;
            x--;
        }
        j=0;
        archin.getline(c,100);
        f2=atoi(c)-1;
        x=4;
        l=0;
        while(x!=0){
            archin.getline(c,100);
            p=strtok(c," ");
            j=0;
            while(p!=NULL){
                a2[l][j]=atoi(p);
                p=strtok(NULL," ");
                j++;
            }
            l++;
            x--;
        }
        int cont=0;
        for(int m=0;m<4;m++){
            for(int n=0;n<4;n++){
                if(a1[f][m]==a2[f2][n]){
                    cont++;
                    num=a1[f][m];
                }
            }
        }
        archout<<"Case #" << i <<": ";
        if(cont==1)
            archout<<num<<endl;
        if(cont>1)
            archout<<"Bad magician!"<<endl;
        if(cont==0)
            archout<<"Volunteer cheated!"<<endl;

        i++;
        n--;

    }

    cout<<"exit";
    archout.close();
    archin.close();
    return 0;
}
