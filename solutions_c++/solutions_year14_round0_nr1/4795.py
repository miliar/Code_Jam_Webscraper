#include  <vector>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
#include <fstream>

using namespace std;

int cards1[5][5], cards2[5][5];
int row1,row2;
int t,c,teste;

int main(){

    ofstream myfile;
    myfile.open("output.txt");
    ios::sync_with_stdio(0);


        cin>>t;

        	for (int i = 1; i <= t; ++i)
        	{   teste=0;
        		cin>>row1;
        		for(int j=0;j<4;j++)
                    for(int k=0;k<4;k++)
                        cin>>cards1[j][k];

                cin>>row2;
        		for(int j=0;j<4;j++)
                    for(int k=0;k<4;k++)
                        cin>>cards2[j][k];

                for(int j=0;j<4;j++)
                    for(int k=0;k<4;k++)
                        if(cards2[row2-1][k]==cards1[row1-1][j]){
                            teste++;
                            c=cards2[row2-1][k];
                }

                if(teste==1) myfile << "Case #"<<i<<": "<<c<<'\n';
                if(teste>1) myfile << "Case #"<<i<<": Bad magician!\n";
                if(teste==0) myfile << "Case #"<<i<<": Volunteer cheated!\n";

        	}
            myfile.close();
            return 0;


        }




