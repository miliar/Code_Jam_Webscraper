#include <iostream>
#include <string>
#include <fstream>
#include<iomanip>
using namespace std;
int main()
{
	int counter=0;
	int seccounter=0;
	string num;
	float swap=0;
	ifstream jhoom("smallinput1.txt");
	ofstream yo("out.txt");
	cout<<fixed<<setprecision(5);
	float wordi=0;
	int length;
	float nao[1000],ken[1000],nao1[1000],ken1[1000];
	getline(jhoom,num);	
	int total=atoi(num.c_str());
	for(int temp=0;temp<total;temp++)
	{
				jhoom>>length;
				for(int temper=0;temper<length;temper++){
				jhoom>>nao[temper];				
				}
		
				for(int temper=0;temper<length;temper++){
					jhoom>>ken[temper];				
				}

				for(int temper=0;temper<length;temper++){
					for(int tempe=0;tempe<length;tempe++){
						if(nao[tempe]>nao[temper]){
						swap=nao[tempe];
						nao[tempe]=nao[temper];
						nao[temper]=swap;
						}

						if(ken[tempe]>ken[temper]){
						swap=ken[tempe];
						ken[tempe]=ken[temper];
						ken[temper]=swap;
						}

					}
				}





				for(int temper=0;temper<length;temper++){
//				cout<<ken[temper]<<" "<<nao[temper];
				ken1[temper]=ken[temper];
				nao1[temper]=nao[temper];				
				}
//				cout<<endl;

				for(int temper=0;temper<length;temper++){
					for(int temperor=0;temperor<length;temperor++){
					if(ken[temper]!=-1&&nao[temperor]!=-1&&(ken[temper]<nao[temperor])){
					ken[temper]=-1;
					nao[temperor]=-1;
					counter++;
					}

					if(ken1[temper]!=-1&&nao1[temperor]!=-1&&(ken1[temper]>nao1[temperor])){
					ken1[temper]=-1;
					nao1[temperor]=-1;
					seccounter++;
					}

					}
				}
				seccounter=length-seccounter;
				yo<<"Case #"<<temp+1<<": "<<counter<<" "<<seccounter<<endl;				
				counter=0;
				seccounter=0;
	}
		system("pause");
	
}




