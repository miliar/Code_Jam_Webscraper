#include<iostream>
#include<fstream>
using namespace std;

int a1 = 0, a2 = 0, g1[4][4] = {0}, g2[4][4] = {0}, i = 0, j = 0, f=0, n=0,it=0, fn = 0;
ifstream File("A-small-attempt0.in");
ofstream oFile("output.io");
int main(){
	// oFile<<"Enter the number of testcases: ";
	File>>n;
	for(it=0;it<n;it++){
	    // oFile<<"Enter the first choice: ";
	    File>>a1;
	    // oFile<<"Enter the first grid: ";
	    for(i=0; i<4;i++){
	    	for(j=0;j<4;j++){
	    		File>>g1[i][j];
	    	}
	    }
	    // oFile<<"Enter the second choice: ";
	    File>>a2;
	    // oFile<<"Enter the second grid: ";
	    for(i=0;i<4;i++){
	    	for(j=0;j<4;j++){
	    		File>>g2[i][j];
	    	}
	    }
	    f=0;
	    a1--;
	    a2--;
	    for(i=0;i<4;i++){
	    	// chkD();
	    	for(j=0;j<4;j++){
	    		// oFile<<g1[a1][i]<<"=="<<g2[a2][j]<<endl;
	    		if(g1[a1][i] == g2[a2][j]){
	    			fn = g1[a1][i];
	    			f++;
	    		}
	    	}
	    }
	    // oFile<<endl<<"::"<<f<<endl;
	    oFile<<"Case #"<<it+1<<": ";
	    switch(f){
	    	case 0:
	    		oFile<<"Volunteer cheated!"<<endl;
	    		break;
	    	case 1:
	    		oFile<<fn<<endl;
	    		break;
	    	default:
	    		oFile<<"Bad magician!"<<endl;
	    }
	}
    return 0;
}
