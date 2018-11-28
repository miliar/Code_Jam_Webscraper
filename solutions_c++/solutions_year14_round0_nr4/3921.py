#include <iostream>;
#include <fstream>;
#include <set>;
#include <vector>;
using namespace std;
int main(){
    ifstream in("D-Small.in");
    ofstream out("D-Large.out");
    int tests;
    in >>tests;
    vector<double> naomi;
    vector<double> ken;
    for(int i=0;i<tests;i++){
            int blocks;
            in>>blocks;
            int wins=0;
            int wins2=0;
            for(int j=0;j<blocks;j++){
                    double block;
                    in>>block;
                    naomi.push_back(block);        
            }
            for(int j=0;j<blocks;j++){
                    double block;
                    in>>block;
                    ken.push_back(block);        
            }
            sort(naomi.begin(),naomi.end());
            sort(ken.begin(),ken.end());
            
            vector<double> naomi2=naomi;
            vector<double> ken2=ken;
            
            while(!naomi.empty()){
                double nam=*(naomi.end()-1);
                double ke=*(ken.end()-1);
                if(nam > ke){
                    wins++;
                    naomi.erase(naomi.end()-1); 
                    ken.erase(ken.end()-1); 
                }else{
                    naomi.erase(naomi.begin());
                    ken.erase(ken.end()-1);       
                }
                nam= *(naomi2.end()-1);  
                ke= *(ken2.end()-1);
                
                
                if(nam > ke){
                    wins2++;
                    naomi2.erase(naomi2.end()-1); 
                    ken2.erase(ken2.begin());
                }else{
                    naomi2.erase(naomi2.end()-1); 
                    ken2.erase(ken2.end()-1); 
                }
                           
                          
            }
            
            
            
            
            out<<"Case #"<<(i+1)<<": "<<wins<<" "<<wins2<<"\n";
    }
    
    
}
