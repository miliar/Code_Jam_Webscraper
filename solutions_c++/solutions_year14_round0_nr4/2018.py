#include<fstream>

using namespace std;

int main() {
    float naomi[1000],ken[1000],temppitch1[1000][3],temppitch2[1000][3];
    int N,y,z,j,k,T;
    ofstream writeoutput;
    ifstream readinput;
    writeoutput.open("Output_d_large.txt",ios::out);
    readinput.open("D-large.in",ios::in);
    readinput.precision(10);
    writeoutput.precision(10);
    readinput>>T;
    for(int i=1;i<=T;i++) {
        N=y=z=0;
        readinput>>N;
        for(j=0;j<N;j++)
            readinput>>naomi[j];
        for(j=0;j<N;j++)
            readinput>>ken[j];
        for(j=0;j<N;j++) {
            temppitch1[j][0]=temppitch2[j][0]=naomi[j];
            temppitch1[j][1]=temppitch2[j][1]=ken[j];
        }
        for(j=0;j<N;j++) {
            for(k=j;k<N;k++) {
                if((temppitch1[j][0]>temppitch1[j][1])&&(temppitch1[j][1]>temppitch1[k][1]&&temppitch1[j][0]>temppitch1[k][1])) {
                    float temp=temppitch1[j][1];
                    temppitch1[j][1]=temppitch1[k][1];
                    temppitch1[k][1]=temp;
                }
                if((temppitch1[j][0]>temppitch1[j][1])&&(temppitch1[j][1]<temppitch1[k][1]&&temppitch1[j][0]<temppitch1[k][1])) {
                    float temp=temppitch1[j][1];
                    temppitch1[j][1]=temppitch1[k][1];
                    temppitch1[k][1]=temp;
                }
                if((temppitch1[j][0]<temppitch1[j][1])&&(temppitch1[j][1]>temppitch1[k][1]&&temppitch1[k][1]>temppitch1[j][0])) {
                    float temp=temppitch1[j][1];
                    temppitch1[j][1]=temppitch1[k][1];
                    temppitch1[k][1]=temp;
                }   
            }
        }
        for(j=0;j<N;j++) {
            for(k=j;k<N;k++) {
                if((temppitch2[j][1]>temppitch2[j][0])&&(temppitch2[j][0]<temppitch2[k][0]&&temppitch2[k][0]>temppitch2[j][1])) {
                    float temp=temppitch2[j][0];
                    temppitch2[j][0]=temppitch2[k][0];
                    temppitch2[k][0]=temp;
                }   
                if((temppitch2[j][1]>temppitch2[j][0])&&(temppitch2[j][0]>temppitch2[k][0]&&temppitch2[k][0]<temppitch2[j][1])) {
                    float temp=temppitch2[j][0];
                    temppitch2[j][0]=temppitch2[k][0];
                    temppitch2[k][0]=temp;
                }       
                if((temppitch2[j][1]<temppitch2[j][0])&&(temppitch2[j][0]>temppitch2[k][0]&&temppitch2[k][0]>temppitch2[j][1])) {
                    float temp=temppitch2[j][0];
                    temppitch2[j][0]=temppitch2[k][0];
                    temppitch2[k][0]=temp;
                }
            }
        }
        for(j=0;j<N;j++) {
            if(temppitch1[j][0]>temppitch1[j][1])
                z++;
            if(temppitch2[j][0]>temppitch2[j][1])
                y++;
        }
        writeoutput<<"Case #"<<i<<": "<<y<<" "<<z<<endl;
    }
    return 0;
}
