#include <iostream>
#include <string>
#define rondas 13

using namespace std;

string torneos[rondas+1][3]; // número de rondas y ganador.
int     tipos[rondas+1][3][3]; // Gente en cada tipo de torneo

char trad[3]={'P','R','S'};

int main() {

  torneos[0][0]=trad[0];
  torneos[0][1]=trad[1];
  torneos[0][2]=trad[2];

  for(int g=0;g<3;g++)
    for(int j=0;j<3;j++)
      tipos[0][g][j]=(g==j)?1:0;


  for(int i=1; i<rondas; i++){
    for(int g=0; g<3; g++) {
      //primero actualizar tipos.
      for(int j=0; j<3; j++) {
        tipos[i][g][j]=tipos[i-1][g][j]+tipos[i-1][(g+1)%3][j];
      }

      //Luego actualizar los strings
      
      torneos[i][g]=(torneos[i-1][g]<torneos[i-1][(g+1)%3])?
                    (torneos[i-1][g]+torneos[i-1][(g+1)%3]):
                    (torneos[i-1][(g+1)%3]+torneos[i-1][g]);

    }
  }

  int T; cin>>T; int n,r,p,s,g;

  for(int t=1; t<=T; t++) {
    cout<<"Case #"<<t<<": ";
    cin>>n>>r>>p>>s;

    if(p==tipos[n][0][0] && r==tipos[n][0][1] && s==tipos[n][0][2]) g=0;
    else if(p==tipos[n][1][0] && r==tipos[n][1][1] && s==tipos[n][1][2]) g=1;
    else if(p==tipos[n][2][0] && r==tipos[n][2][1] && s==tipos[n][2][2]) g=2;
    else { cout<<"IMPOSSIBLE"<<endl; continue;}
    cout<<torneos[n][g]<<endl;
  }


  return 0;
}

