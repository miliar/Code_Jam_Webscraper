#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
    int n,g,m;
  
    //déclraration de mes 2 fichiers
    string const nomFichier("output.out");    
    ifstream monFlux1("A-small-attempt1.in");
    ofstream monFlux(nomFichier.c_str());
    
    monFlux1 >> n; 
    
    if(monFlux)
    {
        //cout <<n<<endl;                 
        for(int p=0;p<n;p++)
        {
		 	//lecture des g ;	
            monFlux1 >> g;    
            int t1[4];
			int t2[4];    
            
            for(int j=1;j<=4;j++)
            {		
					if(g==j){
							for(int i=0;i<4;i++) 
									monFlux1>>t1[i];
					}else{
						  for(int i=0;i<4;i++)	
                    		monFlux1>>m;
					}                    
            }   
            monFlux1 >> g;
            //lecture des g ;
            for(int j=1;j<=4;j++)
            {		
					if(g==j){
							for(int i=0;i<4;i++)
									monFlux1>>t2[i];
					}else{
					for(int i=0;i<4;i++)	
                    		monFlux1>>m;
					}
					                   
            }		
            int eq=0,r;
            //traitement
            for(int j=0;j<4;j++)
            {
                    for(int k=0;k<4;k++){
                            if(t1[j]==t2[k]){ eq++; r=t1[j];}
                    }                                  
            } 
            if(eq==1)
            		 monFlux<<"Case #"<<p<<": "<< r<<endl;
            else
            	if(eq>0) monFlux<<"Case #"<<p<<": "<< "Bad magician"<<endl;
            	else monFlux<<"Case #"<<p<<": "<< "Volunteer cheated!"<<endl;
            cout<<endl;       
                
        }
    }
    else
    {
        cout << "ERREUR: Impossible d'ouvrir le fichier." << endl;
    }
         
    system("pause");
    return 0;
}
