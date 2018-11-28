#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int t,c1,c2,index;
    ifstream in("A-small-attempt1.in");
    ofstream out("Output.out");
    int cards[4][4];
    int aux1[4];
    int aux2[4];
    if (!in) {
        cout << "Cannot open file.\n";
    }
    in>>t;
    int cases=1;
    while(cases<=t){
        in>>c1;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                in>>cards[i][j];
            }
        }
        for(int i=0;i<4;i++){
            aux1[i]=cards[c1-1][i];
        }
        in>>c2;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                in>>cards[i][j];
            }
        }
        for(int i=0;i<4;i++){
            aux2[i]=cards[c2-1][i];
        }
        int contor=0;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(aux1[i]==aux2[j]){
                    contor++;
                    index=i;
                    aux2[j]=-1;
                    break;
                }
            }
        }
        if (contor == 1){
			out << "Case #" << cases << ": " << aux1[index] << endl;
		}
		else if (contor>1){
			out << "Case #" << cases << ": " << "Bad magician!" << endl;
		}
		else if (contor == 0){
			out << "Case #" << cases << ": " << "Volunteer cheated!" << endl;
		}
        cases++;
    }
    return 0;
}
