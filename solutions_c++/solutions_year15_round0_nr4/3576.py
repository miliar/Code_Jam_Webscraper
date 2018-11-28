#include <fstream>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("D-small-attempt0.in");
    fout.open("D-small-result.txt");

    int T,X,R,C;
    string g="GABRIEL";
    string r="RICHARD";
    fin>>T;
    for(int i=1;i<=T;i++)
    {
    	string winner;
    	fin>>X>>R>>C;
    	switch(X){
    	    case 1: winner = g;
    	    break;

    	    case 2: if(!((R*C)%2)){winner = g;}
    	    else {winner = r;}
            break;

            case 3: if(R==1 || (R==2 && C!=3) || (R==3 && C==1) || (R==4 && C!=3)){winner = r;}
            else{winner=g;}
            break;

            case 4: if(R==1 || R==2 || (R==3 && C!=4) || (R==4 && C<=2)){winner = r;}
            else{winner = g;}
    	}
    	fout<<"Case #"<<i<<": "<<winner<<endl;
	}
	return 0;
}
