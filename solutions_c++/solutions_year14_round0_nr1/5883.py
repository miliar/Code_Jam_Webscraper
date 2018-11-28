#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream arch;
	ofstream arch2;
	arch.open("A-small-attempt1.in");
	arch2.open("res.txt");

	int n,r1,r2,aux;
	arch >> n;

	for(int s=0; s<n; s++){
        vector<int> res1, res2;
        arch >> r1;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                arch >> aux;
                if(r1==i+1){
                    res1.push_back(aux);
                }
            }
        }
        arch >> r2;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                arch >> aux;
                if(r2==i+1){
                    res2.push_back(aux);
                }
            }
        }
        vector<bool>respuestas(4,false);
        int respuestaBuena;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                if(res1[i]==res2[j]){
                    respuestas[i]=true;
                    respuestaBuena=res1[i];
                }
            }
        }
        int cont=0;
        for(int i=0; i<4; i++){
            if(respuestas[i]) cont++;
        }

        arch2 << "Case #" << s+1 << ": ";
        if(cont==0){
            arch2 << "Volunteer cheated!" << endl;
        } else if(cont==1){
            arch2 << respuestaBuena << endl;
        } else {
            arch2 << "Bad magician!" << endl;
        }
	}

	arch.close();
	arch2.close();

	return 0;
}


