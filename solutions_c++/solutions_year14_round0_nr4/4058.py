#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main(){
	ifstream in ("D-large.in");
	ofstream out ("output.out");
	int caso,coso;
	in>>caso;
	for(coso=0;coso<caso;coso++){
		int blocchi,i,j,t1,t2,punti=0,puntib=0;
		in>>blocchi;
		float nao[blocchi],ken[blocchi];
		bool visitato[blocchi],check;
		
		for(i=0;i<blocchi;i++) in>>nao[i];
		for(i=0;i<blocchi;i++) in>>ken[i];
		for(i=0;i<blocchi;i++) visitato[i]=false;
		
		sort(nao,nao+blocchi);
		sort(ken,ken+blocchi);
		
		for(i=0;i<blocchi;i++){
			check = true;
			for(j=0;j<blocchi;j++){
				if(visitato[j]==false && ken[j]>nao[i]){
					visitato[j]=true;
					check=false;
					j=blocchi;
					}
				}
				if(check==true){
					for(j=0;j<blocchi;j++) if(visitato[j]==false) visitato[j]=true;
					punti++;
					}
			}
			
		for(i=blocchi-1,t2=0,t1=blocchi-1; i>=0 ; i--){
				if(ken[i]<nao[t1]){
					puntib++;
					t1--;
					}
				else t2++;
			}


			out<<"Case #"<<coso+1<<": "<<puntib<<" "<<punti<<endl;
		}
	}
